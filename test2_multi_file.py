from uhdl.uhdl import *
from MultiFileCooperation import *


class test_multi_file(Component):
    def __init__(self):
        super().__init__()
        add_scope(globals=globals(), locals=locals())

        exec_file('sub_file1.py')
        exec_file('sub_file2.py')
        exec_file('sub_file3.py')

        
if __name__=="__main__":
    u_test = test_multi_file()
    u_test.output_dir = 'build'
    u_test.run_lint()
    
    u_test.generate_verilog()
    u_test.generate_filelist()


    
    
    
