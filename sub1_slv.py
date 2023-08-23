self.expose_io(self.u_slv.get_io('top_'), has_prefix=False)

self.clk = Input(UInt(1))
self.rst_n = Input(UInt(1))




single_assign(self.clk, self.u_slv.clk)
single_assign(self.clk, self.u_mst.clk)
single_assign(self.rst_n, self.u_slv.rst_n)
single_assign(self.rst_n, self.u_mst.rst_n)