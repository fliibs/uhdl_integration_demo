from submodules.uhdl import *


class operation_demo(Component):

    def __init__(self):
        super().__init__()

        self.clk    = Input(UInt(1))
        self.rst_n  = Input(UInt(1))

        self.A = Input(UInt(2))
        self.B = Input(UInt(2))
        self.C = Input(UInt(4))
        self.E = Output(UInt(1))


        # Cut operation : []
        self.Cut_LowerBit_A = Wire(UInt(1))
        self.Cut_LowerBit_A += self.A[0]

        self.Cut_TwoBit_C = Wire(UInt(2))
        self.Cut_TwoBit_C += self.C[1:0]

        # Logic operation: || && ! 
        self.A_Or_B = Wire(UInt(1))
        self.A_Or_B += Or(self.A[0], self.B[1])
        
        self.A_And_B = Wire(UInt(1))
        self.A_And_B += And(self.A[0], self.B[1])

        self.Not_A = Wire(UInt(1))
        self.Not_A += Not(self.A)

        # Bitwise operation: | & ~
        self.A_BitOr_B = Wire(UInt(2))
        self.A_BitOr_B += BitOr(self.A, self.B)
        
        self.A_BitAnd_B = Wire(UInt(2))
        self.A_BitAnd_B += BitAnd(self.A, self.B)

        self.Inverse_A = Wire(UInt(2))
        self.Inverse_A += Inverse(self.A)

        # Combine Operation: {}
        self.A_Combine_B = Wire(UInt(4))
        self.A_Combine_B += Combine(self.A, self.B)

        # Assign: Use Assign(A,B) or Use A+=B
        Assign(self.E, UInt(1,0))

        
        # combinational logic block and sequential logic block
        self.demo_w = Wire(UInt(1))
        eptw = EmptyWhen()
        eptw.when(Equal(self.A, self.B)).then(self.C[1]).otherwise(self.C[0])
        self.demo_w += eptw

        self.demo_r = Reg(UInt(1,0), self.clk, self.rst_n)
        self.demo_r += eptw




if __name__=="__main__":

    u_demo = operation_demo()
    u_demo.run_lint()
    u_demo.generate_verilog()
    u_demo.generate_filelist()
