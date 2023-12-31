module axi_master #(
		parameter DATA_WIDTH  =32,
		parameter AWADDR_WIDTH=32,
		parameter ARADDR_WIDTH=32,
		parameter AWID_WIDTH  =7,
		parameter BID_WIDTH   =7,
		parameter ARID_WIDTH  =7,
		parameter RID_WIDTH   =7,
		parameter AWUSER_WIDTH=5,
		parameter WUSER_WIDTH =5,
		parameter BUSER_WIDTH =5,
		parameter ARUSER_WIDTH=5,
		parameter RUSER_WIDTH =5
	)(
		input                                             clk,
		input                                             rst_n,

		output   [AWID_WIDTH-1 : 0]                       m_axi_awid,
		output   [AWADDR_WIDTH-1 : 0]                     m_axi_awaddr,
		output   [7 : 0]                                  m_axi_awlen,
		output   [2 : 0]                                  m_axi_awsize,
		output   [1 : 0]                                  m_axi_awburst,
		output                                            m_axi_awlock,
		output   [3 : 0]                                  m_axi_awcache,
		output   [2 : 0]                                  m_axi_awprot,
		output   [3 : 0]                                  m_axi_awqos,
		output   [AWUSER_WIDTH-1 : 0]                     m_axi_awuser,
		output                                            m_axi_awvalid,
		input                                             m_axi_awready,
		output   [DATA_WIDTH-1 : 0]                       m_axi_wdata,
		output   [DATA_WIDTH/8-1 : 0]                     m_axi_wstrb,
		output                                            m_axi_wlast,
		output   [WUSER_WIDTH-1 : 0]                      m_axi_wuser,
		output                                            m_axi_wvalid,
		input                                             m_axi_wready,
		input    [BID_WIDTH-1 : 0]                        m_axi_bid,
		input    [1 : 0]                                  m_axi_bresp,
		input    [BUSER_WIDTH-1 : 0]                      m_axi_buser,
		input                                             m_axi_bvalid,
		output                                            m_axi_bready,
		output   [ARID_WIDTH-1 : 0]                       m_axi_arid,
		output   [ARADDR_WIDTH-1 : 0]                     m_axi_araddr,
		output   [7 : 0]                                  m_axi_arlen,
		output   [2 : 0]                                  m_axi_arsize,
		output   [1 : 0]                                  m_axi_arburst,
		output                                            m_axi_arlock,
		output   [3 : 0]                                  m_axi_arcache,
		output   [2 : 0]                                  m_axi_arprot,
		output   [3 : 0]                                  m_axi_arqos,
		output   [ARUSER_WIDTH-1 : 0]                     m_axi_aruser,
		output                                            m_axi_arvalid,
		input                                             m_axi_arready,
		input    [RID_WIDTH-1 : 0]                        m_axi_rid,
		input    [DATA_WIDTH-1 : 0]                       m_axi_rdata,
		input    [1 : 0]                                  m_axi_rresp,
		input                                             m_axi_rlast,
		input    [RUSER_WIDTH-1 : 0]                      m_axi_ruser,
		input                                             m_axi_rvalid,
		output                                            m_axi_rready
	);


endmodule