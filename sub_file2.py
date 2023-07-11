
self.u_slv = VComponent(top='axi_slave' ,file='../uhdl_demo/rtl_repo/axi_slave.v',   DATA_WIDTH=32, \
                                                                                     AWADDR_WIDTH=32, \
                                                                                     ARADDR_WIDTH=32, \
                                                                                     AWID_WIDTH=7, \
                                                                                     BID_WIDTH=7, \
                                                                                     ARID_WIDTH=7, \
                                                                                     RID_WIDTH=7, \
                                                                                     AWUSER_WIDTH=5, \
                                                                                     WUSER_WIDTH=5, \
                                                                                     BUSER_WIDTH=5, \
                                                                                     ARUSER_WIDTH=5, \
                                                                                     RUSER_WIDTH=5 )
self.u_mst = VComponent(top='axi_master' ,file='../uhdl_demo/rtl_repo/axi_master.v', DATA_WIDTH=32, \
                                                                                     AWADDR_WIDTH=32, \
                                                                                     ARADDR_WIDTH=32, \
                                                                                     AWID_WIDTH=7, \
                                                                                     BID_WIDTH=7, \
                                                                                     ARID_WIDTH=7, \
                                                                                     RID_WIDTH=7, \
                                                                                     AWUSER_WIDTH=5, \
                                                                                     WUSER_WIDTH=5, \
                                                                                     BUSER_WIDTH=5, \
                                                                                     ARUSER_WIDTH=5, \
                                                                                     RUSER_WIDTH=5 )

 # assign u_slv_clk = clk
self.u_slv.clk   += self.clk
self.u_slv.rst_n += self.rst_n

self.u_mst.clk   += self.clk
self.u_mst.rst_n += self.rst_n

