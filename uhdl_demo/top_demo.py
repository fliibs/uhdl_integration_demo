import sys
from uhdl.uhdl import *
import re



class top_demo(Component):
    def __init__(self):
        super().__init__()

        # define io of top
        # input clk
        self.clk             = Input(UInt(1))
        self.rst_n           = Input(UInt(1))
        self.top_demo_signal = Output(UInt(1))
        self.top_axi_awready = Output(UInt(1))
        self.inout_demo_slv  = Inout(UInt(1))
        self.inout_demo_mst  = Inout(UInt(1))

        # instantiated axi_slave and axi_master
        self.u_slv = VComponent(top='axi_slave' ,file='rtl_repo/axi_slave.v',   DATA_WIDTH=32, \
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
        self.u_mst = VComponent(top='axi_master' ,file='rtl_repo/axi_master.v', DATA_WIDTH=32, \
                                                                                AWADDR_WIDTH=32, \
                                                                                ARADDR_WIDTH=32, \
                                                                                AWID_WIDTH=4, \
                                                                                BID_WIDTH=7, \
                                                                                ARID_WIDTH=9, \
                                                                                RID_WIDTH=7, \
                                                                                AWUSER_WIDTH=5, \
                                                                                WUSER_WIDTH=5, \
                                                                                BUSER_WIDTH=5, \
                                                                                ARUSER_WIDTH=5, \
                                                                                RUSER_WIDTH=5 )

        self.u_demo_inout = VComponent(top='demo_inout',file='rtl_repo/demo_inout.v')

        # assign u_slv_clk = clk
        self.u_slv.clk   += self.clk
        self.u_slv.rst_n += self.rst_n

        self.u_mst.clk   += self.clk
        self.u_mst.rst_n += self.rst_n

        # assign u_slv_s_axi_awid = {3'b0, u_mst_m_axi_awid};       assign u_slv_s_axi_arid = u_mst_m_axi_arid[6:0];
        self.u_slv.s_axi_awid += Combine(UInt(self.u_slv.s_axi_awid.width-self.u_mst.m_axi_awid.width,0), self.u_mst.m_axi_awid)
        self.u_slv.s_axi_arid += self.u_mst.m_axi_arid[self.u_slv.s_axi_arid.width-1:0]

        # get io list
        mst_list = self.u_mst.get_io('m_')
        slv_list = self.u_slv.get_io('s_')
        top_list = self.u_slv.get_io('top_')
        inout_list = self.u_demo_inout.io_list
        print(inout_list)

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
        # self.expose_io()
    

    # Override parent class function to modify io name of top
    def expose_io(self, io_list):
        for io in io_list:
            sub_inst = io._father
            if self != sub_inst._father:
                raise Exception()
            new_io_name = 'HEAD_%s_%s' % (sub_inst.name, io.name)
            new_io = self.set(new_io_name, io.template())

            if isinstance(new_io, Input):
                io += new_io
            elif isinstance(new_io, Output):
                new_io += io
            elif isinstance(new_io, Inout):
                new_io += io
            else:
                raise Exception()

    def exclude_io(self, io_list, exclude_list):
        pattern = '|'.join(exclude_list)
        for io in io_list:
            if re.search(pattern, io.name):
                io_list.remove(io)


if __name__=="__main__":
    u_test = top_demo()
    u_test.run_lint()
    # u_test.generate_filelist()
    u_test.generate_verilog()