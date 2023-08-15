from uhdl.uhdl import *


class top_demo(Component):
    def __init__(self):
        super().__init__()

        self.clk             = Input(UInt(1))
        self.rst_n           = Input(UInt(1))

        # instantiated axi_slave and axi_master
        self.u_slv = VComponent(top='axi_slave',filelist='rtl_repo/filelist.f', DATA_WIDTH=32, \
                                                                                AWADDR_WIDTH=32, \
                                                                                ARADDR_WIDTH=32, \
                                                                                AWID_WIDTH=7, \
                                                                                BID_WIDTH=7, \
                                                                                ARID_WIDTH=7, \
                                                                                RID_WIDTH=7 )
        
        self.u_mst = VComponent(top='axi_master',filelist='rtl_repo/filelist.f',DATA_WIDTH=32, \
                                                                                AWADDR_WIDTH=32, \
                                                                                ARADDR_WIDTH=32, \
                                                                                AWID_WIDTH=4, \
                                                                                BID_WIDTH=7, \
                                                                                ARID_WIDTH=9, \
                                                                                RID_WIDTH=7 )
        
        self.u_slv.clk   += self.clk
        self.u_slv.rst_n += self.rst_n

        self.u_mst.clk   += self.clk
        self.u_mst.rst_n += self.rst_n

        self.u_slv.s_axi_awid += Combine(UInt(self.u_slv.s_axi_awid.width-self.u_mst.m_axi_awid.width,0), self.u_mst.m_axi_awid)
        self.u_slv.s_axi_arid += self.u_mst.m_axi_arid[self.u_slv.s_axi_arid.width-1:0]

        mst_list = self.u_mst.get_io('m_')
        slv_list = self.u_slv.get_io('s_')
        top_list = self.u_slv.get_io('top_')

        SmartAssign(self.exclude_io(mst_list, ['arid','awid']), self.exclude_io(slv_list, ['arid','awid']))
        self.expose_io(self.exclude_io(top_list, ['awready']))

if __name__=="__main__":
    u_test = top_demo()
    u_test.output_dir = 'build'
    u_test.run_lint()
    
    u_test.generate_verilog()
    u_test.generate_filelist()