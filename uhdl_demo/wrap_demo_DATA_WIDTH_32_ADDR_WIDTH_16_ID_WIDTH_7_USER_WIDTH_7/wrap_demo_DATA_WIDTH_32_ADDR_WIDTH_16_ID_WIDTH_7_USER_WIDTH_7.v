//==========================================================================================================================
//Key is used to ensure the consistency of file version and content, and cannot be modified.
//Version Control is the version number written when the file is generated and cannot be modified.
//ToolMessage is used to record related information of any tool that has processed the file and cannot be manually modified.
//UserMessage is used by the user to write any information, which can be modified in any way.
//Content is the actual payload of the file.
//Parameter is the additional parameter information carried by the file and cannot be modified in any way.

//Key is generated by the hash of Version Control, Content and Parameter to ensure the consistency of the file.
//These three parts do not allow any individual modification
//==========================================================================================================================


//[UHDL]Key Start [md5:713a1c1a3a5a19093aa62340c12db4ea]
//Version Control Hash: 3accddf64b1dd03abeb9b0b3e5a7ba44
//Content Hash: 99137e4d78feb6eea33c966c222545fd
//Parameter Hash: d41d8cd98f00b204e9800998ecf8427e
//[UHDL]Key End [md5:713a1c1a3a5a19093aa62340c12db4ea]

//[UHDL]Version Control Start [md5:3accddf64b1dd03abeb9b0b3e5a7ba44]
//[UHDL]Version Control Version:1.0.1
//[UHDL]Version Control End [md5:3accddf64b1dd03abeb9b0b3e5a7ba44]

//[UHDL]Tool Message Start [md5:12d89bc3a7a394204b64466868dd5f97]
//Written by UHDL in 2023-07-07 01:18:50
//[UHDL]Tool Message End [md5:12d89bc3a7a394204b64466868dd5f97]

//[UHDL]User Message Start [md5:d41d8cd98f00b204e9800998ecf8427e]

//[UHDL]User Message End [md5:d41d8cd98f00b204e9800998ecf8427e]

//[UHDL]Content Start [md5:99137e4d78feb6eea33c966c222545fd]
module wrap_demo_DATA_WIDTH_32_ADDR_WIDTH_16_ID_WIDTH_7_USER_WIDTH_7 (
	input  [6:0]  D_u_slv_s_axi_awid     ,
	input  [15:0] D_u_slv_s_axi_awaddr   ,
	input  [7:0]  D_u_slv_s_axi_awlen    ,
	input  [2:0]  D_u_slv_s_axi_awsize   ,
	input  [1:0]  D_u_slv_s_axi_awburst  ,
	input         D_u_slv_s_axi_awlock   ,
	input  [3:0]  D_u_slv_s_axi_awcache  ,
	input  [2:0]  D_u_slv_s_axi_awprot   ,
	input  [3:0]  D_u_slv_s_axi_awqos    ,
	input  [6:0]  D_u_slv_s_axi_awuser   ,
	input         D_u_slv_s_axi_awvalid  ,
	output        D_u_slv_s_axi_awready  ,
	input  [31:0] D_u_slv_s_axi_wdata    ,
	input  [3:0]  D_u_slv_s_axi_wstrb    ,
	input         D_u_slv_s_axi_wlast    ,
	input  [6:0]  D_u_slv_s_axi_wuser    ,
	input         D_u_slv_s_axi_wvalid   ,
	output        D_u_slv_s_axi_wready   ,
	output [6:0]  D_u_slv_s_axi_bid      ,
	output [1:0]  D_u_slv_s_axi_bresp    ,
	output [6:0]  D_u_slv_s_axi_buser    ,
	output        D_u_slv_s_axi_bvalid   ,
	input         D_u_slv_s_axi_bready   ,
	input  [6:0]  D_u_slv_s_axi_arid     ,
	input  [15:0] D_u_slv_s_axi_araddr   ,
	input  [7:0]  D_u_slv_s_axi_arlen    ,
	input  [2:0]  D_u_slv_s_axi_arsize   ,
	input  [1:0]  D_u_slv_s_axi_arburst  ,
	input         D_u_slv_s_axi_arlock   ,
	input  [3:0]  D_u_slv_s_axi_arcache  ,
	input  [2:0]  D_u_slv_s_axi_arprot   ,
	input  [3:0]  D_u_slv_s_axi_arqos    ,
	input  [6:0]  D_u_slv_s_axi_aruser   ,
	input         D_u_slv_s_axi_arvalid  ,
	output        D_u_slv_s_axi_arready  ,
	output [6:0]  D_u_slv_s_axi_rid      ,
	output [31:0] D_u_slv_s_axi_rdata    ,
	output [1:0]  D_u_slv_s_axi_rresp    ,
	output        D_u_slv_s_axi_rlast    ,
	output [6:0]  D_u_slv_s_axi_ruser    ,
	output        D_u_slv_s_axi_rvalid   ,
	input         D_u_slv_s_axi_rready   ,
	input  [15:0] D_u_slv_top_axi_awaddr ,
	input  [2:0]  D_u_slv_top_axi_awprot ,
	input         D_u_slv_top_axi_awvalid,
	output        D_u_slv_top_axi_awready,
	input  [31:0] D_u_slv_top_axi_wdata  ,
	input  [3:0]  D_u_slv_top_axi_wstrb  ,
	input         D_u_slv_top_axi_wvalid ,
	output        D_u_slv_top_axi_wready ,
	output [1:0]  D_u_slv_top_axi_bresp  ,
	output        D_u_slv_top_axi_bvalid ,
	input         D_u_slv_top_axi_bready ,
	input  [15:0] D_u_slv_top_axi_araddr ,
	input  [2:0]  D_u_slv_top_axi_arprot ,
	input         D_u_slv_top_axi_arvalid,
	output        D_u_slv_top_axi_arready,
	output [31:0] D_u_slv_top_axi_rdata  ,
	output [1:0]  D_u_slv_top_axi_rresp  ,
	output        D_u_slv_top_axi_rvalid ,
	input         D_u_slv_top_axi_rready ,
	input         D_u_slv_clk            ,
	input         D_u_slv_rst_n          );
	wire        u_slv_clk            ;
	wire        u_slv_rst_n          ;
	wire [15:0] u_slv_top_axi_awaddr ;
	wire [2:0]  u_slv_top_axi_awprot ;
	wire        u_slv_top_axi_awvalid;
	wire        u_slv_top_axi_awready;
	wire [31:0] u_slv_top_axi_wdata  ;
	wire [3:0]  u_slv_top_axi_wstrb  ;
	wire        u_slv_top_axi_wvalid ;
	wire        u_slv_top_axi_wready ;
	wire [1:0]  u_slv_top_axi_bresp  ;
	wire        u_slv_top_axi_bvalid ;
	wire        u_slv_top_axi_bready ;
	wire [15:0] u_slv_top_axi_araddr ;
	wire [2:0]  u_slv_top_axi_arprot ;
	wire        u_slv_top_axi_arvalid;
	wire        u_slv_top_axi_arready;
	wire [31:0] u_slv_top_axi_rdata  ;
	wire [1:0]  u_slv_top_axi_rresp  ;
	wire        u_slv_top_axi_rvalid ;
	wire        u_slv_top_axi_rready ;
	wire [6:0]  u_slv_s_axi_awid     ;
	wire [15:0] u_slv_s_axi_awaddr   ;
	wire [7:0]  u_slv_s_axi_awlen    ;
	wire [2:0]  u_slv_s_axi_awsize   ;
	wire [1:0]  u_slv_s_axi_awburst  ;
	wire        u_slv_s_axi_awlock   ;
	wire [3:0]  u_slv_s_axi_awcache  ;
	wire [2:0]  u_slv_s_axi_awprot   ;
	wire [3:0]  u_slv_s_axi_awqos    ;
	wire [6:0]  u_slv_s_axi_awuser   ;
	wire        u_slv_s_axi_awvalid  ;
	wire        u_slv_s_axi_awready  ;
	wire [31:0] u_slv_s_axi_wdata    ;
	wire [3:0]  u_slv_s_axi_wstrb    ;
	wire        u_slv_s_axi_wlast    ;
	wire [6:0]  u_slv_s_axi_wuser    ;
	wire        u_slv_s_axi_wvalid   ;
	wire        u_slv_s_axi_wready   ;
	wire [6:0]  u_slv_s_axi_bid      ;
	wire [1:0]  u_slv_s_axi_bresp    ;
	wire [6:0]  u_slv_s_axi_buser    ;
	wire        u_slv_s_axi_bvalid   ;
	wire        u_slv_s_axi_bready   ;
	wire [6:0]  u_slv_s_axi_arid     ;
	wire [15:0] u_slv_s_axi_araddr   ;
	wire [7:0]  u_slv_s_axi_arlen    ;
	wire [2:0]  u_slv_s_axi_arsize   ;
	wire [1:0]  u_slv_s_axi_arburst  ;
	wire        u_slv_s_axi_arlock   ;
	wire [3:0]  u_slv_s_axi_arcache  ;
	wire [2:0]  u_slv_s_axi_arprot   ;
	wire [3:0]  u_slv_s_axi_arqos    ;
	wire [6:0]  u_slv_s_axi_aruser   ;
	wire        u_slv_s_axi_arvalid  ;
	wire        u_slv_s_axi_arready  ;
	wire [6:0]  u_slv_s_axi_rid      ;
	wire [31:0] u_slv_s_axi_rdata    ;
	wire [1:0]  u_slv_s_axi_rresp    ;
	wire        u_slv_s_axi_rlast    ;
	wire [6:0]  u_slv_s_axi_ruser    ;
	wire        u_slv_s_axi_rvalid   ;
	wire        u_slv_s_axi_rready   ;
	assign D_u_slv_s_axi_awready = u_slv_s_axi_awready;
	
	assign D_u_slv_s_axi_wready = u_slv_s_axi_wready;
	
	assign D_u_slv_s_axi_bid = u_slv_s_axi_bid;
	
	assign D_u_slv_s_axi_bresp = u_slv_s_axi_bresp;
	
	assign D_u_slv_s_axi_buser = u_slv_s_axi_buser;
	
	assign D_u_slv_s_axi_bvalid = u_slv_s_axi_bvalid;
	
	assign D_u_slv_s_axi_arready = u_slv_s_axi_arready;
	
	assign D_u_slv_s_axi_rid = u_slv_s_axi_rid;
	
	assign D_u_slv_s_axi_rdata = u_slv_s_axi_rdata;
	
	assign D_u_slv_s_axi_rresp = u_slv_s_axi_rresp;
	
	assign D_u_slv_s_axi_rlast = u_slv_s_axi_rlast;
	
	assign D_u_slv_s_axi_ruser = u_slv_s_axi_ruser;
	
	assign D_u_slv_s_axi_rvalid = u_slv_s_axi_rvalid;
	
	assign D_u_slv_top_axi_awready = u_slv_top_axi_awready;
	
	assign D_u_slv_top_axi_wready = u_slv_top_axi_wready;
	
	assign D_u_slv_top_axi_bresp = u_slv_top_axi_bresp;
	
	assign D_u_slv_top_axi_bvalid = u_slv_top_axi_bvalid;
	
	assign D_u_slv_top_axi_arready = u_slv_top_axi_arready;
	
	assign D_u_slv_top_axi_rdata = u_slv_top_axi_rdata;
	
	assign D_u_slv_top_axi_rresp = u_slv_top_axi_rresp;
	
	assign D_u_slv_top_axi_rvalid = u_slv_top_axi_rvalid;
	
	assign u_slv_clk = D_u_slv_clk;
	
	assign u_slv_rst_n = D_u_slv_rst_n;
	
	assign u_slv_top_axi_awaddr = D_u_slv_top_axi_awaddr;
	
	assign u_slv_top_axi_awprot = D_u_slv_top_axi_awprot;
	
	assign u_slv_top_axi_awvalid = D_u_slv_top_axi_awvalid;
	
	assign u_slv_top_axi_wdata = D_u_slv_top_axi_wdata;
	
	assign u_slv_top_axi_wstrb = D_u_slv_top_axi_wstrb;
	
	assign u_slv_top_axi_wvalid = D_u_slv_top_axi_wvalid;
	
	assign u_slv_top_axi_bready = D_u_slv_top_axi_bready;
	
	assign u_slv_top_axi_araddr = D_u_slv_top_axi_araddr;
	
	assign u_slv_top_axi_arprot = D_u_slv_top_axi_arprot;
	
	assign u_slv_top_axi_arvalid = D_u_slv_top_axi_arvalid;
	
	assign u_slv_top_axi_rready = D_u_slv_top_axi_rready;
	
	assign u_slv_s_axi_awid = D_u_slv_s_axi_awid;
	
	assign u_slv_s_axi_awaddr = D_u_slv_s_axi_awaddr;
	
	assign u_slv_s_axi_awlen = D_u_slv_s_axi_awlen;
	
	assign u_slv_s_axi_awsize = D_u_slv_s_axi_awsize;
	
	assign u_slv_s_axi_awburst = D_u_slv_s_axi_awburst;
	
	assign u_slv_s_axi_awlock = D_u_slv_s_axi_awlock;
	
	assign u_slv_s_axi_awcache = D_u_slv_s_axi_awcache;
	
	assign u_slv_s_axi_awprot = D_u_slv_s_axi_awprot;
	
	assign u_slv_s_axi_awqos = D_u_slv_s_axi_awqos;
	
	assign u_slv_s_axi_awuser = D_u_slv_s_axi_awuser;
	
	assign u_slv_s_axi_awvalid = D_u_slv_s_axi_awvalid;
	
	assign u_slv_s_axi_wdata = D_u_slv_s_axi_wdata;
	
	assign u_slv_s_axi_wstrb = D_u_slv_s_axi_wstrb;
	
	assign u_slv_s_axi_wlast = D_u_slv_s_axi_wlast;
	
	assign u_slv_s_axi_wuser = D_u_slv_s_axi_wuser;
	
	assign u_slv_s_axi_wvalid = D_u_slv_s_axi_wvalid;
	
	assign u_slv_s_axi_bready = D_u_slv_s_axi_bready;
	
	assign u_slv_s_axi_arid = D_u_slv_s_axi_arid;
	
	assign u_slv_s_axi_araddr = D_u_slv_s_axi_araddr;
	
	assign u_slv_s_axi_arlen = D_u_slv_s_axi_arlen;
	
	assign u_slv_s_axi_arsize = D_u_slv_s_axi_arsize;
	
	assign u_slv_s_axi_arburst = D_u_slv_s_axi_arburst;
	
	assign u_slv_s_axi_arlock = D_u_slv_s_axi_arlock;
	
	assign u_slv_s_axi_arcache = D_u_slv_s_axi_arcache;
	
	assign u_slv_s_axi_arprot = D_u_slv_s_axi_arprot;
	
	assign u_slv_s_axi_arqos = D_u_slv_s_axi_arqos;
	
	assign u_slv_s_axi_aruser = D_u_slv_s_axi_aruser;
	
	assign u_slv_s_axi_arvalid = D_u_slv_s_axi_arvalid;
	
	assign u_slv_s_axi_rready = D_u_slv_s_axi_rready;
	
	axi_slave #(
		.DATA_WIDTH(32),
		.ADDR_WIDTH(16),
		.ID_WIDTH(7),
		.USER_WIDTH(7))
	u_slv (
		.clk(u_slv_clk),
		.rst_n(u_slv_rst_n),
		.top_axi_awaddr(u_slv_top_axi_awaddr),
		.top_axi_awprot(u_slv_top_axi_awprot),
		.top_axi_awvalid(u_slv_top_axi_awvalid),
		.top_axi_awready(u_slv_top_axi_awready),
		.top_axi_wdata(u_slv_top_axi_wdata),
		.top_axi_wstrb(u_slv_top_axi_wstrb),
		.top_axi_wvalid(u_slv_top_axi_wvalid),
		.top_axi_wready(u_slv_top_axi_wready),
		.top_axi_bresp(u_slv_top_axi_bresp),
		.top_axi_bvalid(u_slv_top_axi_bvalid),
		.top_axi_bready(u_slv_top_axi_bready),
		.top_axi_araddr(u_slv_top_axi_araddr),
		.top_axi_arprot(u_slv_top_axi_arprot),
		.top_axi_arvalid(u_slv_top_axi_arvalid),
		.top_axi_arready(u_slv_top_axi_arready),
		.top_axi_rdata(u_slv_top_axi_rdata),
		.top_axi_rresp(u_slv_top_axi_rresp),
		.top_axi_rvalid(u_slv_top_axi_rvalid),
		.top_axi_rready(u_slv_top_axi_rready),
		.s_axi_awid(u_slv_s_axi_awid),
		.s_axi_awaddr(u_slv_s_axi_awaddr),
		.s_axi_awlen(u_slv_s_axi_awlen),
		.s_axi_awsize(u_slv_s_axi_awsize),
		.s_axi_awburst(u_slv_s_axi_awburst),
		.s_axi_awlock(u_slv_s_axi_awlock),
		.s_axi_awcache(u_slv_s_axi_awcache),
		.s_axi_awprot(u_slv_s_axi_awprot),
		.s_axi_awqos(u_slv_s_axi_awqos),
		.s_axi_awuser(u_slv_s_axi_awuser),
		.s_axi_awvalid(u_slv_s_axi_awvalid),
		.s_axi_awready(u_slv_s_axi_awready),
		.s_axi_wdata(u_slv_s_axi_wdata),
		.s_axi_wstrb(u_slv_s_axi_wstrb),
		.s_axi_wlast(u_slv_s_axi_wlast),
		.s_axi_wuser(u_slv_s_axi_wuser),
		.s_axi_wvalid(u_slv_s_axi_wvalid),
		.s_axi_wready(u_slv_s_axi_wready),
		.s_axi_bid(u_slv_s_axi_bid),
		.s_axi_bresp(u_slv_s_axi_bresp),
		.s_axi_buser(u_slv_s_axi_buser),
		.s_axi_bvalid(u_slv_s_axi_bvalid),
		.s_axi_bready(u_slv_s_axi_bready),
		.s_axi_arid(u_slv_s_axi_arid),
		.s_axi_araddr(u_slv_s_axi_araddr),
		.s_axi_arlen(u_slv_s_axi_arlen),
		.s_axi_arsize(u_slv_s_axi_arsize),
		.s_axi_arburst(u_slv_s_axi_arburst),
		.s_axi_arlock(u_slv_s_axi_arlock),
		.s_axi_arcache(u_slv_s_axi_arcache),
		.s_axi_arprot(u_slv_s_axi_arprot),
		.s_axi_arqos(u_slv_s_axi_arqos),
		.s_axi_aruser(u_slv_s_axi_aruser),
		.s_axi_arvalid(u_slv_s_axi_arvalid),
		.s_axi_arready(u_slv_s_axi_arready),
		.s_axi_rid(u_slv_s_axi_rid),
		.s_axi_rdata(u_slv_s_axi_rdata),
		.s_axi_rresp(u_slv_s_axi_rresp),
		.s_axi_rlast(u_slv_s_axi_rlast),
		.s_axi_ruser(u_slv_s_axi_ruser),
		.s_axi_rvalid(u_slv_s_axi_rvalid),
		.s_axi_rready(u_slv_s_axi_rready));

endmodule
//[UHDL]Content End [md5:99137e4d78feb6eea33c966c222545fd]

//[UHDL]Parameter Start [md5:d41d8cd98f00b204e9800998ecf8427e]

//[UHDL]Parameter End [md5:d41d8cd98f00b204e9800998ecf8427e]

