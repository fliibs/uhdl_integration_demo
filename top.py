self.u_subsys1 = VComponent(top='subsys1' ,file='rtl_repo/subsys1.v ', DATA_WIDTH=32, \
                                                                                        DATA_TYPE=5)
self.u_subsys2 = VComponent(top='subsys2' ,file='rtl_repo/subsys2.v', DATA_WIDTH=32, \
                                                                                       DATA_TYPE=5, \
                                                                                       DATA_TYPE2=5, \
                                                                                       DATA_TYPE1=5)
self.u_subsys3 = VComponent(top='subsys3' ,file='rtl_repo/subsys3.v', )

self.u_demo_inout_0 = VComponent(top="demo_inout", file="rtl_repo/demo_inout.v")
self.u_demo_inout_1 = VComponent(top="demo_inout", file="rtl_repo/demo_inout_2.v")
single_assign(self.u_demo_inout_0.data_io, self.u_demo_inout_1.data_io_2)
single_assign(self.u_demo_inout_0.data_io, self.u_demo_inout_1.data_io_2)
single_assign(self.u_demo_inout_1.data_io_2, self.u_demo_inout_0.data_io)
