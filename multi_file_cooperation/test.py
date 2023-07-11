from uhdl.uhdl import *
from MultiFileCooperation import *


class test(Component):
    def __init__(self):
        super().__init__()
        add_scope(globals=globals(), locals=locals())

        exec_file('sub_file1.py')
        exec_file('sub_file2.py')
        exec_file('sub_file3.py')


 # Override parent class function to modify io name of top
    def expose_io(self, io_list):
        for io in io_list:
            sub_inst = io._father
            if self != sub_inst._father:
                raise Exception()
            new_io_name = 'HEAD_%s_%s' % (sub_inst.name, io.name)
            new_io = self.set(new_io_name, io.template())

            if isinstance(new_io, Input):
                io += new_io
            elif isinstance(new_io, Output):
                new_io += io
            elif isinstance(new_io, Inout):
                new_io += io
            else:
                raise Exception()

    def exclude_io(self, io_list, exclude_list):
        pattern = '|'.join(exclude_list)
        for io in io_list:
            if re.search(pattern, io.name):
                io_list.remove(io)

    
if __name__=="__main__":
    u_test = test()
    u_test.run_lint()
    # u_test.generate_filelist()
    u_test.generate_verilog()
    
    
    
