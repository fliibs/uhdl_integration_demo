self.expose_io([self.u_subsys1.clk],has_prefix=False)
self.expose_io([self.u_subsys1.rst_n],has_prefix=False)
self.expose_io([self.u_subsys1.data_conf],has_prefix=False)
self.expose_io([self.u_subsys1.data_valid],has_prefix=False)
self.expose_io([self.u_subsys1.data_v],has_prefix=False)
self.expose_io([self.u_subsys1.rxdatahs_0],has_prefix=False)
self.expose_io([self.u_subsys1.rxdatahs_1],has_prefix=False)
self.expose_io([self.u_subsys1.stopstatedata_0],has_prefix=False)
self.expose_io([self.u_subsys1.csi_data],has_prefix=False)
self.expose_io([self.u_subsys1.data_en],has_prefix=False)
self.expose_io([self.u_subsys1.header_en],has_prefix=False)
self.expose_io([self.u_subsys1.data_type],has_prefix=False)
self.expose_io([self.u_subsys1.ecc],has_prefix=False)
self.word_count_nnn     =        Output(UInt(3))
self.word_cnt_wire = Wire(UInt(2))
single_assign(self.word_count_nnn, self.u_subsys1.word_count)
single_assign(self.u_subsys1.subsys1_to_subsys2_ddd, Combine(self.word_cnt_wire, self.u_subsys2.subsys3orl_to_subsys2_ddd[9:8], self.u_subsys2.subsys3orl_to_subsys2_ddd[7:6], UInt(2,0x1), self.u_subsys3.subsys3_to_subsys2_biu[1], UInt(2,0x0)))
self.u_subsys2.subsys3orl_to_subsys2_ddd += UInt(11,0)
single_assign(self.u_subsys1.subsys2_to_subsys1_ming, self.u_subsys2.subsys2_to_subsys1_ming[3:0])
single_assign(self.u_subsys1.subsys2_to_subsys1_d, self.u_subsys2.subsys2_to_subsyslor2_d)
single_assign(self.u_subsys1.subsys1_tie_constant, UInt(7,0xd))
unconnect_port(self, self.u_subsys1.subsys1_open) # output
unconnect_port(self, self.u_subsys1.subsys1_pclk_d) # input
perfect_assign(self.u_subsys1, self.u_subsys2, apb.io_list, ["pclk" , "pready"], src_prefix='subsys1_',  dst_prefix='subsys2_',src_suffix='_d', dst_suffix='_d')
perfect_assign(self.u_subsys1, self.u_subsys3, apb.io_list, [], src_prefix='subsys13_',  dst_prefix='subsys3_',src_suffix='_d', dst_suffix='_d')

self.word_cnt_wire += self.u_subsys2.word_count

