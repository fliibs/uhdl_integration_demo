# assign u_slv_s_axi_awid = {3'b0, u_mst_m_axi_awid};       assign u_slv_s_axi_arid = u_mst_m_axi_arid[6:0];
self.u_slv.s_axi_awid += Combine(UInt(self.u_slv.s_axi_awid.width-self.u_mst.m_axi_awid.width,0), self.u_mst.m_axi_awid)
self.u_slv.s_axi_arid += self.u_mst.m_axi_arid[self.u_slv.s_axi_arid.width-1:0]

# get io list
mst_list = self.u_mst.get_io('m_')
slv_list = self.u_slv.get_io('s_')
top_list = self.u_slv.get_io('top_')

# remove io which name contains arid or awid from mst_list and slv_list

self.exclude_io(mst_list, ['arid','awid'])
self.exclude_io(slv_list, ['arid','awid'])
self.exclude_io(top_list, ['awready'])

# combinational logic operation in top module
self.top_demo_signal += And(self.u_mst.m_axi_awvalid, Equal(self.u_mst.m_axi_awid, UInt(self.u_mst.m_axi_awid.width, 1)))
self.top_axi_awready += Or(self.u_slv.top_axi_awready, self.top_demo_signal)

# connect remain io in list
SmartAssign(mst_list, slv_list)

# expose io to top
self.expose_io(top_list)