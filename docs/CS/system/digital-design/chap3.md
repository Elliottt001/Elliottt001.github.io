组合电路

定义：m个输入n个输出，输出仅由输入决定

有n个表达式，m个输入分别控制输出

## 组合电路分析

![alt text](image-15.png)

**方法**

1. 分层

    - 非不算

2. 分层写表达式

    - 分层标注节点，写“过程式”
    - 认电路符号

3. 展开化简

    - 异或按照定义变与或非
    - 化简

4. 画真值表
5. 推出功能

![alt text](image-13.png)

## 组合电路设计

![alt text](image-14.png)
![alt text](image-16.png)

**方法**

![alt text](image-17.png)

**示例**

![alt text](image-18.png)

- 设计真值表：考虑需求 / 定义的值 0/1 的含义
- 根据真值表写最小项之和

![alt text](image-19.png)

（奇函数天然优化）

![alt text](image-20.png)

```verilog
module lamp_control(s1,s2,s3,F );
input s1,s2,s3;
output F;
wire s1,s2,s3,f;

assign F= (~s3&~s2&s1) | (~s3&s2&~s1) | (s3&~s2&~s1) | (s3&s2&s1) ;
endmodule
``` 

**示例2**

表 1 其实就是真值表，用上自由项

W X Y Z 分别有几个 1 ，对应 ABCD 分别是什么

![alt text](image-21.png)
![alt text](image-22.png)

卡诺图优化

联合优化：四个一起看，提取公因式

![alt text](image-23.png)
![alt text](image-24.png)

输入多：分层法

eg：9输入分成 3 * 3 再加一个合并这三个的第四个

![alt text](image-25.png)

## 技术参数

![alt text](image-26.png)

fan-in：栅入参数，即input个数

fan-out：能带几个负载

### fan-in

每个门上面有压降（如下左图），不是0电阻，所以太多的话影响电压

fan-in 是 ：输出为正确的情况下最多的input个数，$（最大识别为1的电压 - 最小识别为1的电压） / 每个门处压降$

![alt text](image-27.png)

### fan-out

**标准负载**：1输入1输出的非门

**计算**：看的是带几个标准负载，不同负载与标准负载成倍数

**转换时间**： $t_{LH} $ 和 $t_{HL}$，开始变到最后变化之间的时间

**有fanout原因**：从0到1，给电容式负载充电，负载多充电能力下降，电平转换时间延长，电路要求工作速度，最大电平转换时间对应的是fan-out

![alt text](image-28.png)

### 传播延迟时间 propagation delay

**定义**：输入端变化到输出端变化之间的延迟时间 $t_{PHL}$ $t_{PLH}$，端到端时间差

**别和转换时间混掉**

- 转换时间：每个门上的电平变化时间
- 传播延迟时间：端到端的电平变化时间



计算：

- 控制变量法：将其他输入都开绿灯
    - 那么与非门变成一个非门，因为另一路输入规定 = 1
- 反向推导：从输出（高到低/低到高）一个一个往前推，找变化原因
- 最后每个加和

- 有时取 $t_{PHL}$ 和 $t_{PLH}$ 的最大值/平均值作为每个门的传播延迟时间，一般是平均

**读波形图**：取中点时间差

![alt text](image-29.png)

**例题**：

![alt text](image-43.png)

#### transport delay 传输延时 

就是延迟时间，推后一定时间

#### inertial delay 阻尼延时

电容会滤波，小的毛刺信号会被吸收，例如拒绝时间 = 5ns，小于他则无法传输

以上是两种传播延时的模型

#### 实际计算

传输延时 + 标准负载数 * 标准负载延时

![alt text](image-44.png)

## 基本功能模块设计

### 使能

相当于开关

![alt text](image-30.png)

**分类**：按中间的门类型

- 与使能：使能信号为1则“开”，即显示X信号；为0则“关”，即输出信号恒0，不显示X
- 或使能：基本同上

三态门使能与其不同

- 三态门disabe之后输出是高阻状态，没有信号
- 这个的disabe之后输出常量

### 解码器 / 译码器decoder

- 输入；编码压缩信号，连续的
- 输出：离散信号，用于控制

**输入少输出多**

要求：输入 < 输出

![alt text](image-31.png)

!

m输入n输出的译码器：m个非门和n个m输入的与门，但是m大之后与门的fan-in太大

优化：

![alt text](image-33.png)

递归分解的思想，类似归并排序

#### 三八译码器

法一：

![](image-32.png)

对fan-in要求高，不行

法二：

递归分解思想

![alt text](image-45.png)


![](image-34.png)

多层电路

- 好处：输入被复用，门输入代价低
- 坏处：传输延迟时间大

再加一个使能信号，一般用与使能

![alt text](image-35.png)

如果将使能信号看作输入，将 a/b 看成通道选择，变成信号分离器

功能是将 a/b 的输入分离开在不同端输出

用两个24译码器也可以组成38译码器：自底向上设计

高位作为使能信号

![alt text](image-36.png)

#### 用途

实现任何函数：对应的最小项最后或起来

![alt text](image-37.png)

七段数码管：原理是每一个输出管理一个发光二极管，两种接法（共阳极/共阴极），亮/不亮给的电平不一样

![alt text](image-39.png)

![alt text](image-40.png)

### encoder 编码器

多输入少输出

输入为独热码的编码器读取表达式的方法

!!! info ""

    don't care 太多了，不能用之前的方案来办

!!! success "特征位组合法"

    每个最小项都拿输入为1的那些个（特征位）看，将他们加起来即可

![alt text](image-48.png)

![alt text](image-47.png)
![alt text](image-46.png)

![alt text](image-49.png)

!!! warning ""

    这不一定是最优表达式

输入不是只一个为1的情况，即非独热码

**优先级编码器**


输出反映最高优先级位的信号情况，则编码时只编最高有效位上的

方案：

加一个输出V位，它1则这个输出有效

![alt text](image-51.png)
![alt text](image-52.png)

!!! warning ""

    下标大的优先级大

还是看最小项，跟独热码读取的不同点是要带上优先级比他高的位的非


### 多路选择器 multiplexer

![alt text](image-53.png)

2选1 MUX

![alt text](image-54.png)

S为选择信号，等价于一个使能信号，通过使能来控制选择功能

![alt text](image-56.png)

64选1 MUX

![alt text](image-55.png)

输入向量（输入宽度扩展）

方案：先来一个译码器，将信号的位分开，再接好几个编码器，分别处理每一位上的数据

![alt text](image-57.png)

可以用三态门

![alt text](image-58.png)



### 信号分配器
