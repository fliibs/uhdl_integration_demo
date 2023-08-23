from uhdl.uhdl import *
import warnings

class axi_intf():
    io_list = [
        'axi_awid',     
        'axi_awaddr',   
        'axi_awlen',    
        'axi_awsize',   
        'axi_awburst',  
        'axi_awlock',   
        'axi_awcache',  
        'axi_awprot',   
        'axi_awqos',    
        'axi_awuser',   
        'axi_awvalid',  
        'axi_awready',  
        'axi_wdata',    
        'axi_wstrb',    
        'axi_wlast',    
        'axi_wuser',    
        'axi_wvalid',   
        'axi_wready',   
        'axi_bid',      
        'axi_bresp',    
        'axi_buser',    
        'axi_bvalid',   
        'axi_bready',   
        'axi_arid',         
        'axi_araddr',   
        'axi_arlen',    
        'axi_arsize',   
        'axi_arburst',  
        'axi_arlock',   
        'axi_arcache',  
        'axi_arprot',   
        'axi_arqos',    
        'axi_aruser',   
        'axi_arvalid',  
        'axi_arready',  
        'axi_rid',      
        'axi_rdata',    
        'axi_rresp',    
        'axi_rlast',    
        'axi_ruser',    
        'axi_rvalid',   
        'axi_rready'   
        ]

    ignore_list = [
        'axi_awid',
        'axi_arid'
    ]
    def __init__(self) -> None:
        pass



def perfect_assign(src, dst, io_list, ignore_list=[], src_prefix='', dst_prefix=''):
    src_list = []
    dst_list = []
    for suffix in io_list:
        if suffix not in ignore_list:
            src_intf = src.get_io(src_prefix+suffix)
            dst_intf = dst.get_io(dst_prefix+suffix)

            if src_intf == [] : warnings.warn('Interface \'%s\' Was Not Found'% (src_prefix+suffix));continue
            elif dst_intf == [] : warnings.warn('Interface \'%s\' Was Not Found'% (dst_prefix+suffix));continue

            src_list.append(src_intf)
            dst_list.append(dst_intf)

    SmartAssign(src_list, dst_list)


def single_assign(op1, op2):
    if isinstance(op1, Inout) and isinstance(op2, Inout):
        op1 += op2
    elif isinstance(op1, (Input, Output)) and isinstance(op2, (Input, Output)):
        SmartAssign(op1, op2)
    
    elif isinstance(op1, (Input, Output)):
        op1_component = op1.father_until(Component)
        if isinstance(op1_component, VComponent):
            if isinstance(op1, Input):
                op1 += op2
            else:
                op2 += op1
        elif isinstance(op1_component, Component):
            if isinstance(op1, Input):
                op2 += op1
            else:
                op1 += op2
        else:
            raise Exception("Hierachy Error, there is a bug")
        
    elif isinstance(op2, (Input, Output)):
        op2_component = op2.father_until(Component)
        if isinstance(op2_component, VComponent):
            if isinstance(op2, Input):
                op2 += op1
            else:
                op1 += op2
        elif isinstance(op2_component, Component):
            if isinstance(op2, Input):
                op1 += op2
            else:
                op2 += op1 
        else:
            raise Exception("Hierachy Error, there is a bug")
        
    else:
        raise Exception("Both op1 and op2 are Wire or One op is not Inout")




