from submodules.uhdl import *

class wrap_demo(Component):
    
    def __init__(self, DATA_WIDTH, ADDR_WIDTH, ID_WIDTH, USER_WIDTH):
        super().__init__()

        self.u_slv = VComponent(top='axi_slave' ,file='/workspaces/uhdl_integration_demo/uhdl_demo/rtl_demo/axi_slave.v', \
                                                 DATA_WIDTH=DATA_WIDTH, \
                                                 ADDR_WIDTH=ADDR_WIDTH, \
                                                 ID_WIDTH=ID_WIDTH, \
                                                 USER_WIDTH=USER_WIDTH)

        self.expose_io(self.u_slv.get_io('s_'))
        self.expose_io(self.u_slv.get_io('top_'))
        self.expose_io(self.u_slv.get_io('clk'))
        self.expose_io(self.u_slv.get_io('rst_n'))
        


if __name__ == "__main__":
    u_slv = wrap_demo(32, 16, 7, 7)
    u_slv.run_lint()
    u_slv.generate_verilog()
