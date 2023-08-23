import sys
from uhdl.uhdl import *
import re
# from MultiFileCooperation import exclude_io
from PerfectAssign import *


class top_demo(Component):
    def __init__(self):
        super().__init__()

        # define io of top
        # input clk
        self.clk             = Input(UInt(1))
        self.rst_n           = Input(UInt(1))

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


        single_assign(self.clk, self.u_slv.clk)
        single_assign(self.clk, self.u_mst.clk)
        single_assign(self.rst_n, self.u_slv.rst_n)
        single_assign(self.rst_n, self.u_mst.rst_n)

        single_assign(Combine(UInt(self.u_slv.s_axi_awid.width-self.u_mst.m_axi_awid.width,0), self.u_mst.m_axi_awid), self.u_slv.s_axi_awid)
        single_assign(self.u_mst.m_axi_arid[self.u_slv.s_axi_arid.width-1:0], self.u_slv.s_axi_arid)

        perfect_assign(self.u_mst, self.u_slv, axi_intf.io_list, axi_intf.ignore_list, src_prefix='m_', dst_prefix='s_', src_suffix='', dst_suffix='')

        self.expose_io(self.u_slv.get_io('top_'))
    



if __name__=="__main__":
    u_test = top_demo()
    u_test.output_dir = 'build'
    u_test.run_lint()
    
    u_test.generate_verilog()
    u_test.generate_filelist()