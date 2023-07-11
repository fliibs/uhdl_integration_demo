# define io of top
# input clk
self.clk             = Input(UInt(1))
self.rst_n           = Input(UInt(1))
self.top_demo_signal = Output(UInt(1))
self.top_axi_awready = Output(UInt(1))
self.inout_demo_slv  = Inout(UInt(1))
self.inout_demo_mst  = Inout(UInt(1))