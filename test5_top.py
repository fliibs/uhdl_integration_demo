
from uhdl.uhdl import *
from MultiFileCooperation import *
from PerfectAssign import *


class sys_top(Component):
    def __init__(self):
        super().__init__()
        add_scope(globals=globals(), locals=locals())

        self.clk = Input(UInt(1))
        self.rst_n = Input(UInt(1))

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

        exec_file('sub1_slv.py')
        exec_file('sub2_mst.py')

        

if __name__=="__main__":
    u_test = sys_top()
    u_test.output_dir = 'build'
    u_test.run_lint()
    
    u_test.generate_verilog()
    u_test.generate_filelist()