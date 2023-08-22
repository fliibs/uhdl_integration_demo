# uhdl_integration_demo

## 0. Setup
### 0.1 install gcc-11 g++-11
```shell
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt install gcc-11 g++-11
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 100
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 100
```

### 0.2 install and compile slang
具体见 ![sv-lang](https://sv-lang.com/building.html)
```shell
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt install gcc-11 g++-11
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 100
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 100

git clone https://github.com/MikePopoloski/slang.git
git submodule update --init --recursive

mkdir build && cd build
cmake -DCMAKE_CXX_COMPILER=g++-11 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local/bin ..
make -j8

ctest
sudo make install

# 添加环境变量 export PATH=$PATH:/usr/local/bin/bin
```

测试slang是否可用
```shell
gcc -v 
g++ -v
slang --version
```

### 0.3 拉取uhdl_integration并拉去submodule
```shell
git clone https://github.com/fliibs/uhdl_integration_demo.git
git submodule update --init --recursive
```

## 1. 定义Component
与verilog中的module类似，UHDL中电路的最小集合为Component，在开始描述电路前，要声明一个Component。

### 1.1 声明Component前的Preparation
在声明Component前需要导入必要的Package，例如：

```python
from uhdl.uhdl import *
from PerfectAssign import *
from MultiFileCooperation import *
```

### 1.2 创建module
用该工具集成所创建的module都需要以python的类来存在，并且都需要继承```Component```.

比如需要创建一个名为sys_top的顶层 (除了需要对class的名字进行改动外，其他的都可以作为创建module的必要字符串存在)
```python
class sys_top(Component):
    def __init__(self):
        super().__init__()
        MultiFileScope(globals=globals(), locals=locals())
```

## 2. 实例化模块
通过调用```VComponent```对已有的rtl进行实例化。

```python
VComponent(top, file, filelist, instance, parameter)

# top为例化module的名字
# file为对应rtl的路径
# filelist为对应filelist文件的路径（file和filelist仅需要填一个即可，建议填file）
# instance模块例化的名称（如果模块不需要重复例化则可不填）
# parameter为rtl模块对应的参数
```

比如需要在sys_top中进行子模块的实例化
```python
self.u_slv = VComponent(top='axi_slave' ,file='rtl_repo/axi_slave.v',   DATA_WIDTH=32, \
                                                                                AWADDR_WIDTH=32, \
                                                                                ARADDR_WIDTH=32, \
                                                                                AWID_WIDTH=7, \
                                                                                BID_WIDTH=7, \
                                                                                ARID_WIDTH=7, \
                                                                                RID_WIDTH=7, \
                                                                                AWUSER_WIDTH=5, \
                                                                                WUSER_WIDTH=5, \
                                                                                BUSER_WIDTH=5, \
                                                                                ARUSER_WIDTH=5, \
                                                                                RUSER_WIDTH=5 )
```

## 3. IO连接及位操作
### 3.1 IO连接
#### 3.1.1 单信号single_assign
单信号的连接，可以自动匹配两个信号方向进行连接。
```python
single_assign(Signal_A, Signal_B)

# 这里要求Signal_A和Signal_B的位宽相匹配
```

#### 3.1.2 批量信号perfect_assign
多信号连接，对确定的一组信号，可以自动匹配方向并对每个信号一对一连接。
```python
perfect_assign(src, dst, io_list=[], ignore_list=[], src_prefix='', dst_prefix='')
# src：子模块1
# dst：子模块2
# io_list: 需要从子模块1和子模块2中抓出的信号（不需要信号的全称，比如说io_list中包含axi_awvalid,则会把子模块中带有'axi_awvalid'的信号抓出来进行连接）。
# ignore_list：从io_list中剔除ignore_list中的元素，剔除的元素将不会被抓出。
# src_prefix：会在io_list的每个信号加上该prefix，然后再去子模块1中抓取信号（即如果prefix为'm_'，则会抓取'm_axi_awvalid'信号）。
# dst_prefix: 同理。
```
```io_list```和```ignore_list```准备：
下面为包含axi aw和ar的io list，需要ignore的信号为axi_awid和axi_arid。
```python
class axi_intf():
    io_dict = [
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
        'axi_arready'  
        ]

    ignore_list = [
        'axi_awid',
        'axi_arid'
    ]
    def __init__(self) -> None:
        pass
```

demo中的例子：
```python
perfect_assign(self.u_mst, self.u_slv, axi_intf.io_list, axi_intf.ignore_list, src_prefix='m_', dst_prefix='s_')
```


### 3.2 位操作
#### 3.2.1 补位操作（Combine）
通过```Combine```来将Signal_A和Signal_B进行拼接
```python
Combine(Signal_A, Signal_B)

# 例如
# 这里要求C的位宽与A+B的位宽相匹配
C = Combine(A, B)
# 对应到rtl：assign C = {A，B};
```

#### 3.2.2 截位操作（[]）
通过截位符([])进行截位操作
```python
Signal_B = Signal_A[B_Width-1:0]

# 例如
# 这里要求A截位后位宽与B相匹配
# 假设B的位宽位width
B = A[width-1:0]
# 对应到rtl：assign B = A[width-1:0];
```

### 3.3 将子模块的接口直接暴露到top层接口
这里用```expose_io```进行接口的向上暴露
```python
expose_io(io_list, has_prefix=False)

# io_list: 数据类型为list类型，为需要暴露到顶层的io列表
# has_prefix：如果不需要加子模块的例化名前缀，需要设置为False
```

这里一般会和```get_io```一同使用。```get_io(str)```会抓取模块中带有指定字符串的接口，并返回一个io_list。

如果需要抓取self.u_slv中带有'm_'的接口。
```python
self.u_slv.get_io('m_')
```

## 4. 多人协作
如果需要将一个顶层文件拆成多个python文件进行操作，如```test5_top.py```所示，则需要调用```MultiFileExec```将子文件sub1_slv.py和sub2_mst.py导入top文件中执行：
```python
MultiFileExec('sub1_slv.py')
MultiFileExec('sub2_mst.py')
```


