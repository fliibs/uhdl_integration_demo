self.u_slv.clk   += self.clk
self.u_slv.rst_n += self.rst_n

Assign(self.u_mst.clk, self.clk)
Assign(self.u_mst.rst_n, self.rst_n)


SmartAssign(self.u_mst.get_io('m_'), self.u_slv.get_io('s_'))

self.expose_io(self.u_slv.get_io('top_'))