self.subsys2_clk             = Input(UInt(1))
single_assign(self.subsys2_clk, self.u_subsys2.clk)
self.subsys2_rst_n             = Input(UInt(1))
single_assign(self.subsys2_rst_n, self.u_subsys2.rst_n)
self.subsys2_rxdatahs_0     =        Input(UInt(8))
single_assign(self.subsys2_rxdatahs_0, self.u_subsys2.rxdatahs_0)
self.subsys2_rxdatahs_1     =        Input(UInt(8))
single_assign(self.subsys2_rxdatahs_1, self.u_subsys2.rxdatahs_1)
self.subsys2_stopstatedata_0             = Input(UInt(1))
single_assign(self.subsys2_stopstatedata_0, self.u_subsys2.stopstatedata_0)
self.subsys2_data_type     =        Output(UInt(6))
single_assign(self.subsys2_data_type, self.u_subsys2.data_type)
self.subsys2_ecc     =        Output(UInt(8))
single_assign(self.subsys2_ecc, self.u_subsys2.ecc)
single_assign(self.u_subsys2.subsys1_to_subsys2_ecc, self.u_subsys1.subsys1_to_subsys2_ecc)
single_assign(self.u_subsys2.subsys1_to_subsys2_dav, self.u_subsys1.subsys1_to_subsys2_dav)
self.subsys3or1_to_subsys2_ddd_9bit = Input(UInt(1))
self.subsys3or1_to_subsys2_ddd_4bit = Input(UInt(1))
self.subsys3or1_to_subsys2_ddd_0bit = Input(UInt(2))
single_assign(self.u_subsys2.subsys3or1_to_subsys2_ddd, Combine(self.subsys3or1_to_subsys2_ddd_9bit, UInt(1,0x1), self.u_subsys1.subsys1_to_subsys2_ddd[1:0], UInt(2,0x1), self.subsys3or1_to_subsys2_ddd_4bit, self.u_subsys3.subsys3_to_subsys2_ddd[1:0], self.subsys3or1_to_subsys2_ddd_0bit))
single_assign(self.u_subsys2.subsys3_to_subsys2_biu, self.u_subsys3.subsys3_to_subsys2_biu)
single_assign(self.u_subsys2.subsys2_tie_constant, UInt(7,0xb))
