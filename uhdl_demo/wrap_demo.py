from uhdl.uhdl import *

class wrap_demo(Component):
    
    def __init__(self, DATA_WIDTH):
        super().__init__()

        self.u_slv = VComponent(top='axi_slave' ,file='rtl_repo/axi_slave.v', \
                                                 DATA_WIDTH=DATA_WIDTH)

        self.expose_io(self.u_slv.get_io('s_'))
        self.expose_io(self.u_slv.get_io('top_'))
        self.expose_io(self.u_slv.get_io('clk'))
        self.expose_io(self.u_slv.get_io('rst_n'))
        





if __name__ == "__main__":
    u_slv = wrap_demo(64)
    u_slv.run_lint()
    u_slv.generate_verilog()
