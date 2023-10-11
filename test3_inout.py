from uhdl.uhdl import *

class test_inout(Component):
    def __init__(self):
        super().__init__()
        
        self.u_demo_inout_0 = VComponent(top="demo_inout", file="rtl_repo/demo_inout.v")
        self.u_demo_inout_1 = VComponent(top="demo_inout", file="rtl_repo/demo_inout.v")
        self.u_demo_inout_2 = VComponent(top="demo_inout", file="rtl_repo/demo_inout.v")

        self.u_demo_inout_0.data_io += self.u_demo_inout_1.data_io
        # self.u_demo_inout_1.data_tx += self.u_demo_inout_0.data_rx

        # lst_0 = self.u_demo_inout_0.io_list
        # lst_1 = self.u_demo_inout_1.io_list

        # self.expose_io(self.exclude_io(lst_0, ['io','rx']))
        # self.expose_io(self.exclude_io(lst_1, ['io','tx']))
        # self.expose_io(self.u_demo_inout_2.io_list)



u_test = test_inout()
u_test.output_dir= 'build'
u_test.run_lint()

u_test.generate_verilog()
u_test.generate_filelist()

