from uhdl.uhdl import *
# from PerfectAssign import *
from Bus_def import *
class sys_top(Component):
    def __init__(self):
        super().__init__()
        MultiFileScope(globals=globals(), locals=locals())
        MultiFileExec('top.py')
        MultiFileExec('Bus_def.py')
        MultiFileExec('subsys1.py')
        MultiFileExec('subsys2.py')
        MultiFileExec('subsys3.py')
        single_assign(self.u_subsys1.subsys2_to_subsys1_ming, self.u_subsys2.subsys2_to_subsys1_ming[3:0])

        
if __name__=="__main__":
    u_test = sys_top()
    u_test.output_dir = 'build'
    u_test.run_lint(lint_all=True)
    u_test.generate_verilog()
    u_test.generate_filelist(abs_path=True)
