import sys
from submodules.uhdl import *


class TEST(Component):
    def __init__(self):
        super().__init__()

        self.clk = Input(UInt(1))
        self.rst_n = Input(UInt(1))

        self.u_slv = VComponent(top='axi_slave' ,file='/workspaces/uhdl_integration_demo/uhdl_demo/axi_slave.v', DATA_WIDTH=32, ADDR_WIDTH=12, ID_WIDTH=8)
        self.u_mst = VComponent(top='axi_master' ,file='/workspaces/uhdl_integration_demo/uhdl_demo/axi_master.v', DATA_WIDTH=32, ADDR_WIDTH=12, ID_WIDTH=8)

        self.u_slv.clk   += self.clk
        self.u_slv.rst_n += self.rst_n

        Assign(self.u_mst.clk, self.clk)

        SmartAssign(self.rst_n, self.u_mst.rst_n)

        SmartAssign(self.u_mst.get_io('m_'), self.u_slv.get_io('s_'))
        self.expose_io(self.u_slv.get_io('s0_'))


if __name__=="__main__":

    u_test = TEST()
    u_test.run_lint()
    u_test.generate_verilog()