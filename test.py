from uhdl.uhdl import *
from MultiFileCooperation import *


class test(Component):
    def __init__(self):
        super().__init__()
        add_scope(globals=globals(), locals=locals())

        exec_file('sub_file1.py')
        exec_file('sub_file2.py')
        exec_file('sub_file3.py')


class demo(Component):
    def __init__(self):
        super().__init__()
        self.clk = Input(UInt(1))
        self.rst_n = Input(UInt(1))
        
        self.u_slv = VComponent(top='axi_slave' ,file='/workspaces/uhdl_integration_demo/uhdl_demo/rtl_repo/axi_slave.v',   DATA_WIDTH=32, \
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
        self.u_mst = VComponent(top='axi_master' ,file='/workspaces/uhdl_integration_demo/uhdl_demo/rtl_repo/axi_master.v', DATA_WIDTH=32, \
                                                                                                                            AWADDR_WIDTH=34, \
                                                                                                                            ARADDR_WIDTH=30, \
                                                                                                                            AWID_WIDTH=7, \
                                                                                                                            BID_WIDTH=7, \
                                                                                                                            ARID_WIDTH=7, \
                                                                                                                            RID_WIDTH=7, \
                                                                                                                            AWUSER_WIDTH=5, \
                                                                                                                            WUSER_WIDTH=5, \
                                                                                                                            BUSER_WIDTH=5, \
                                                                                                                            ARUSER_WIDTH=5, \
                                                                                                                            RUSER_WIDTH=5 )

        self.u_slv.clk   += self.clk
        self.u_slv.rst_n += self.rst_n

        Assign(self.u_mst.clk, self.clk)
        Assign(self.u_mst.rst_n, self.rst_n)


        SmartAssign(self.u_mst.get_io('m_'), self.u_slv.get_io('s_'))

        self.expose_io(self.u_slv.get_io('top_'))

    
if __name__=="__main__":
    u_test = test()
    u_test.run_lint()
    # u_test.generate_filelist()
    u_test.generate_verilog()
    
    
    
