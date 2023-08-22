single_assign(self.u_slv.s_axi_awid, Combine(UInt(3,0), self.u_mst.m_axi_awid))
single_assign(self.u_slv.s_axi_arid, self.u_mst.m_axi_arid[6:0])

perfect_assign(self.u_mst, self.u_slv, axi_intf.io_list, axi_intf.ignore_list, src_prefix='m_', dst_prefix='s_')