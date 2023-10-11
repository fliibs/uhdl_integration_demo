module top
	(input 				clk, 
	input                           rst_n,
	input [DATA WIDTH-1:0]          data conf, 
	input                           data_valid, 
	input [7:0]                     data_v, 
	input [7:0]                     rdatahs_0, 
	input [7:0]                     rxdatahs_1, 
	input                           stopstatedata_0, 
	output [DATA_WIDTH-1:0]         csi_data, 
	output                          data_en, 
	output                          header_en, 
	output [5:0]                    data_type, 
	output [7:0]                    eco, 
	output [5:0]                    word_count, 
	input                           subsys3or1_to_subsys2_ddd_10bit, 
	input                           subsys_pclk_d1, 
	input                           subsys_presetn_d2, 
	input  [9:0]                    subsys_paddr_d1, 
	input  [1:0]                    subsys_psel_d1, 
	input                           subsys_penable_d1, 
	input                           subsys_pwrite_d1,
	input  [31:0]                   subsys_pwdata_d1, 
	output                          subsys_pready_d1, 
	output                          subsys_pslverr_d1,
	input                           subsys_pelk_d2, 
	input                           subsys_presetn_d2, 
	input [9:0]                     subsys_paddr_d2, 
	input [1:0]                     subsys_psel_d2, 
	input                           subsys_penable_d2,
	input                           subsys_pwrite_d2, 
	input [31:0]                    subsys_pwdata_d2, 
	output                          subsys_pready_d2, 
	output                          subsys_pslverr_d2,
	input                           subsys_pelk_d3, 
	input                           subsys_presetn_d3, 
	input [9:0]                     subsys_paddr_d3, 
	input [1:0]                     subsys_psel_d3, 
	input                           subsys_penable_d3, 
	input                           subsys_pwrite_d3, 
	input [31:0]                    subsys_pwdata_d3, 
	output                          subsys_pready_d3, 
	output                          subsys_pslverr_d3
);

subsys1 #(DATA_WIDTH (DATA_WIDTH) DATA_TYPE (DATA_TYPE)) u_subsys1 (
.clk (clk)
.rst n(rst n)
.rxdatahs_e(rxdatahs_0_unconnect)
.rxdatahs_1 (rxdatahs_1)
.stopstatedata_O(stopstatedata_0)
.data_type (data_type)
.ecc (ecc)
.word_count (word count)
.subsysl_to_subsys2_ecc(subsys1_to_subsys2_ecc) 
.subsysl_to_subsys2_dav(subsysl_to_subsys2_dav)
.subsys3orl_to_subsys2_ddd(subsys3orl to subsys2 ddd) //[9:5] tie subsys1 ,[4:0] tie subsys3(subsys3) l101 tie top 
.subsys_to_subsys1ro2_biu(subsys_to_subsyslro2_biu)
.subsys2_to_subsys1_ming(subsys2_to_subsysi ming)
.subsys2_to_subsys3_ting(subsys2_to_subsys3_ting) 
.subsys2_to_subsys1or3_d(subsys2_to_subsys1or3d)
.subsys2_tie_constant (subsys2_tie_constant)
.subsys2_open (subsys2_open)
.subsys1_pclk (pclk)
.subsys1_preset (presetn)
.subsysl_paddr (paddr) 
.subsysl_psel (psel)
.subsysl_penable (penable)
.subsys1_pwrite (pwrite)
.subsysl_pwdata (pwdata)
.subsysl_pready (pready)
.subsys1_pslverr(pslverr)
);







































