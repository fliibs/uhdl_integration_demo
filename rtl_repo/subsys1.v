module subsys1 #(parameter DATA_WIDTH =32,
		 parameter DATA_TYPE=5)
		(input				clk,
		 input                          rst_n,
		 input [DATA_WIDTH-1:0]         data_conf,
		 input                          data_valid,
		 input [7:0]                    data_v,
		 input [7:0]                    rxdatahs_0,
		 input [7:0]                    rxdatahs_1,
		 input                          stopstatedata_0, 
		 output [DATA_WIDTH-1:0]        csi_data,
		 output                         data_en,
		 output                         header_en,
		 output [5:0]                   data_type,
		 output [7:0]                   ecc,
		 output  [2:0]                  word_count,
		 output [2:0]                   subsys1_to_subsys2_ecc,
		 output [1:0]                   subsys1_to_subsys2_dav,
		 input [10:0]                  subsys1_to_subsys2_ddd,
		 input [3:0]                    subsys2_to_subsys1_ming,
		 input [7:0]                    subsys2_to_subsys1_d,
		 input[6:0]                     subsys1_tie_constant,
		 output [7:0]                   subsys1_open,
		 input                          subsys1_pclk_d,
                 output                          subsys1_presetn_d,
                 output [9:0]                    subsys1_paddr_d,
                 output [1:0]                    subsys1_psel_d,
                 output                          subsys1_penable_d,
                 output                          subsys1_pwrite_d,
                 output [31:0]                   subsys1_pwdata_d,
                 input                         subsys1_pready_d,
                 input                         subsys1_pslverr_d,
				 output 	                        subsys13_pclk_d,
                 output                          subsys13_presetn_d,
                 output	[9:0]                   subsys13_paddr_d,
                 output  [1:0]                   subsys13_psel_d, 
                 output    subsys13_penable_d,
                 output    subsys13_pwrite_d,
                 output	[31:0]                  subsys13_pwdata_d,
                 input                         subsys13_pready_d,
                 input                         subsys13_pslverr_d

);

endmodule






































