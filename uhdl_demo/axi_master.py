from submodules.uhdl import *

class axi_master(Component):
    
    def __init__(self, DATA_WIDTH, ADDR_WIDTH, ID_WIDTH, USER_WIDTH):
        super().__init__()

        self.u_slv = VComponent(top='axi_master' ,file='/workspaces/uhdl_integration_demo/uhdl_demo/axi_master.v', \
                                                 DATA_WIDTH=DATA_WIDTH, \
                                                 ADDR_WIDTH=ADDR_WIDTH, \
                                                 ID_WIDTH=ID_WIDTH, \
                                                 USER_WIDTH=USER_WIDTH)

        self.expose_io(self.u_slv.get_io('m_'))
        self.expose_io(self.u_slv.get_io('clk'))
        self.expose_io(self.u_slv.get_io('rst_n'))
        


if __name__ == "__main__":
    u_slv = axi_master(32, 16, 7, 7)
    u_slv.run_lint()
    u_slv.generate_verilog()