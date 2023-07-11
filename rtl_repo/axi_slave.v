module axi_slave #(
	parameter DATA_WIDTH=32,
	parameter AWADDR_WIDTH=32,
	parameter ARADDR_WIDTH=32,
	parameter AWID_WIDTH=7,
	parameter BID_WIDTH=7,
	parameter ARID_WIDTH=7,
	parameter RID_WIDTH=7,
	parameter AWUSER_WIDTH=5,
	parameter WUSER_WIDTH=5,
	parameter BUSER_WIDTH=5,
	parameter ARUSER_WIDTH=5,
	parameter RUSER_WIDTH=5 
)(		
		input                   clk,
        input                   rst_n,

		input    [AWADDR_WIDTH-1 : 0]                top_axi_awaddr,
		input    [2 : 0]                             top_axi_awprot,
		input                                        top_axi_awvalid,
		output                                       top_axi_awready,
		input    [DATA_WIDTH-1 : 0]                  top_axi_wdata,
		input    [DATA_WIDTH/8-1 : 0]              	 top_axi_wstrb,
		input                                        top_axi_wvalid,
		output                                       top_axi_wready,
		output   [1 : 0]                             top_axi_bresp,
		output                                       top_axi_bvalid,
		input                                        top_axi_bready,
		input    [ARADDR_WIDTH-1 : 0]                top_axi_araddr,
		input    [2 : 0]                             top_axi_arprot,
		input                                        top_axi_arvalid,
		output                                       top_axi_arready,
		output   [DATA_WIDTH-1 : 0]                  top_axi_rdata,
		output   [1 : 0]                             top_axi_rresp,
		output                                       top_axi_rvalid,
		input                                        top_axi_rready,

		input   [AWID_WIDTH-1 : 0]                     s_axi_awid,
		input   [AWADDR_WIDTH-1 : 0]                   s_axi_awaddr,
		input   [7 : 0]                                s_axi_awlen,
		input   [2 : 0]                                s_axi_awsize,
		input   [1 : 0]                                s_axi_awburst,
		input                                          s_axi_awlock,
		input   [3 : 0]                                s_axi_awcache,
		input   [2 : 0]                                s_axi_awprot,
		input   [3 : 0]                                s_axi_awqos,
		input   [AWUSER_WIDTH-1 : 0]                   s_axi_awuser,
		input                                          s_axi_awvalid,
		output                                         s_axi_awready,
		input   [DATA_WIDTH-1 : 0]                     s_axi_wdata,
		input   [DATA_WIDTH/8-1 : 0]                   s_axi_wstrb,
		input                                          s_axi_wlast,
		input   [WUSER_WIDTH-1 : 0]                    s_axi_wuser,
		input                                          s_axi_wvalid,
		output                                         s_axi_wready,
		output    [BID_WIDTH-1 : 0]                    s_axi_bid,
		output    [1 : 0]                              s_axi_bresp,
		output    [BUSER_WIDTH-1 : 0]                  s_axi_buser,
		output                                         s_axi_bvalid,
		input                                          s_axi_bready,
		input   [ARID_WIDTH-1 : 0]                     s_axi_arid,
		input   [ARADDR_WIDTH-1 : 0]                   s_axi_araddr,
		input   [7 : 0]                                s_axi_arlen,
		input   [2 : 0]                                s_axi_arsize,
		input   [1 : 0]                                s_axi_arburst,
		input                                          s_axi_arlock,
		input   [3 : 0]                                s_axi_arcache,
		input   [2 : 0]                                s_axi_arprot,
		input   [3 : 0]                                s_axi_arqos,
		input   [ARUSER_WIDTH-1 : 0]                    s_axi_aruser,
		input    										s_axi_arvalid,
		output     										s_axi_arready,
		output    [RID_WIDTH-1 : 0] 					s_axi_rid,
		output    [DATA_WIDTH-1 : 0] 					s_axi_rdata,
		output    [1 : 0] 								s_axi_rresp,
		output     										s_axi_rlast,
		output    [RUSER_WIDTH-1 : 0] 					s_axi_ruser,
		output     										s_axi_rvalid,
		input    										s_axi_rready
);


endmodule