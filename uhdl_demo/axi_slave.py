from submodules.uhdl import *

class axi_slave(Component):
    
    def __init__(self, WIDTH, ADDRWD):
        super().__init__()

        self.u_slv = VComponent(top='axi_slave' ,file='/workspaces/uhdl_integration_demo/uhdl_demo/axi_slave.v', WIDTH=WIDTH, ADDRWD=ADDRWD)

        self.expose_io(self.u_slv.get_io('_s'))
        self.expose_io(self.u_slv.get_io('clk'))
        self.expose_io(self.u_slv.get_io('rst_n'))
        


if __name__ == "__main__":
    u_slv = axi_slave(32, 16)
    u_slv.run_lint()
    u_slv.generate_verilog()
