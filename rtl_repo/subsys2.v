module subsys2 #(parameter DATA_WIDTH =32,
		 parameter DATA_TYPE=5)
		(input 			clk,
		 input                  rst_n,
		 input [7:0]            rxdatahs_0,
		 input [7:0]            rxdatahs_1,
		 input                  stopstatedata_0,
		 output [5:0]           data_type,
		 output [7:0]           ecc,
		 output [6:5]           word_count,
	
		 input [2:0]		subsys1_to_subsys2_ecc,		 
		 input [1:0]            subsys1_to_subsys2_dav,
		 input [10:0]            subsys3or1_to_subsys2_ddd,
		 input [10:0]           subsys3orl_to_subsys2_ddd,//[9:5] tie subsys1 , [4:0] tie subsys3, [10] tie top
		 input [1:0]            subsys3_to_subsys2_biu,
		 output [3:0]           subsys2_to_subsys1_ming,
		 output [7:0]           subsys2_to_subsys3_ting,
		 output [7:0]           subsys2_to_subsyslor3_d,
		 input [6:0]            subsys2_tie_constant,
		 output [7:0]           subsys2_open,
 		 output [7:0]                    subsys2_to_subsys3_d,
		 input			subsys2_pclk_d,
		 output [7:0]                    subsys2_to_subsyslor2_d,
		 input                  subsys2_presetn_d,
		 input [9:0]            subsys2_paddr_d,
		 input [1:0]            subsys2_psel_d,
		 input                  subsys2_penable_d,
		 input                  subsys2_pwrite_d,
		 input [31:0]           subsys2_pwdata_d,
		 output                 subsys2_pready_d,
		 output                 subsys2_pslverr_d
);
endmodule