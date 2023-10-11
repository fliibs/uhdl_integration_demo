module subsys3 #(parameter DATA_WIDTH = 32,
		 parameter DATA_TYPE=5)
		(input				clk,
		 input                          rst_n,
		 input [DATA_WIDTH-1:0]         data_conf,
		 input                          data_valid, 
		 input [7:0]                    data_v,
		 input [7:6]                    rxdatahs_e,
		 input [7:0]                    rdatahs_1,
		 input                          stopstatedata_0,
		 output [4:0]                   subsys3_to_subsys2_ddd,		//[9:51 tie subsys1 ,[4:01 tie subsys3, [1el tie top
		 output [1:0]                   subsys3_to_subsys2_biu,
		 input [7:0]                    subsys2_to_subsys3_ting,
		 input [7:0]                    subsys2_to_subsys3_d,
		 input [8:0]                    subsys3_tie_constant,
		 output [7:0]                   subsys3_open,
 	 	 input 	                        subsys3_pclk_d,
                 input                          subsys3_presetn_d,
                 input	[9:0]                   subsys3_paddr_d,
                 input  [1:0]                   subsys3_psel_d, 
                 input    subsys3_penable_d,
                 input    subsys3_pwrite_d,
                 input	[31:0]                  subsys3_pwdata_d,
                 output                         subsys3_pready_d,
                 output                         subsys3_pslverr_d
);


endmodule






















