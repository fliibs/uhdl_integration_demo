from uhdl.uhdl import *


class integration_inout(Component):
    def __init__(self):
        super().__init__()

        self.demo_inout = VComponent(top="demo_inout", file="rtl_repo/demo_inout.v")
        self.expose_io(self.demo_inout.io_list)

    def expose_io(self, io_list):
        for io in io_list:
            sub_inst = io._father
            if self != sub_inst._father:
                raise Exception()
            new_io_name = '%s' % (io.name)
            new_io = self.set(new_io_name, io.template())

            if isinstance(new_io, Input):
                io += new_io
            elif isinstance(new_io, Output):
                new_io += io
            elif isinstance(new_io, Inout):
                new_io += io
            else:
                raise Exception()


u_test = integration_inout()
u_test.run_lint()
u_test.generate_verilog()

    