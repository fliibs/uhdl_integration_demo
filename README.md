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
from MultiFileCooperation import *
```

### 1.2 创建module
用该工具集成所创建的module都需要以python的类来存在，并且都需要继承```Component```.

比如需要创建一个名为sys_top的顶层 (除了需要对class的名字进行改动外，其他的都可以作为创建module的必要字符串存在)
```python
class sys_top(Component):
    def __init__(self):
        super().__init__()
        add_scope(globals=globals(), locals=locals())
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
#### 3.1.1 单信号Assign

#### 3.1.2 批量信号Assign


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
expose_io(io_list, )
```



