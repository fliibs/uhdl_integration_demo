
from uhdl.uhdl import *
from PerfectAssign import *


class sys_top(Component):
    def __init__(self):
        super().__init__()
        MultiFileScope(globals=globals(), locals=locals())

        
        
        MultiFileExec('sub1_slv.py')
        MultiFileExec('sub2_mst.py')
        MultiFileExec('sub3_inst.py')

        

if __name__=="__main__":
    u_test = sys_top()
    u_test.output_dir = 'build'
    u_test.run_lint()
    
    u_test.generate_verilog()
    u_test.generate_filelist()