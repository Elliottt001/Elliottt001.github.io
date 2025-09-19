## 计算器分类

- PC
- 服务器
- 超级计算器：高端计算的服务器
- 嵌入式：环境 / 电源要求 / 屏幕 / 芯片等要求

## 计算机中有什么？

- 硬件
- 操作系统（管理硬件，做一些底层的东西）
    - 底层存储：0 / 1
    - 底层运算：与 / 或
- 系统软件
- 应用软件

## 编程语言

高级语言

高级语言，经过编译器，翻译成汇编语言，在经过汇编器，翻译成机器码

- c / cpp / Java 


汇编语言 Assembly language

- 把机器码转换成符号（注记），和机器码很接近
- `add` `ld` `sd`，分别是加法，load，store
- `x6` `x5` x几代表寄存器

机器码

- 指令：在 RISC-V 中，一条指令就是32位二进制数

## 计算机体系结构（基本组成）

五个部分（冯诺依曼结构）

- 输入设备 input
- 输出设备 output
- 内存
- 控制器 control unit
- 运算器 / 数据通路

CPU 中包含：控制器 + 运算器 / 数据通路

## 一些硬件设备

PC 主板 motherboard

- PCI 总线插槽：全部设备通过总线相连，是可扩展的（比如说加一块硬盘）
- CPU 插座（CPU 是一种芯片chip）
- 内存条

触摸屏

- 原理：电容式 capacity 是手指接触产生电容变化

显示器 LCD screen

- 分辨率：屏幕就是一个巨大的像素点阵，每一个点都用 RGB 三原色显示颜色，每一个颜色都用 1 Byte 表示（8位，0~255），所以一个像素点就是 3 Byte，对应的存储是 **显存**（屏幕缓冲器，不在内存里面）
- 刷新率：硬件读取显存的频率，屏幕每秒钟刷新的次数，60Hz 就是每秒钟刷新60次

CPU中包含：

- 控制器 control unit
- 数据通路
- Cache memory
    - 是什么：比主存速度高的存储器
    - 也叫 SRAM 存储器（静态随机存取存储器）（内存是 DRAM，动态随机存取存储器，不停的刷新）

ISA（Instruction Set Architecture，指令集架构）

- CPU 中的指令集（汇编/机器码）：底层硬件给软件提供的接口（内部封装，给外部提供接口）
- 流派：x86（Intel / AMD） / ARM（手机） / RISC-V
- 就是一种抽象：根据接口，硬件工程师设计硬件，软件工程师设计软件

有关存储器

- 易失的 volatile / 非易失的 non-volatile

    - 易失的：断电数据丢失，速度快，价格便宜
        - 寄存器 register
        - Cache
        - 主存 memory / RAM
    - 非易失的：断电数据不丢失，速度慢，价格贵
        - 硬盘 disk / SSD
        - 光盘 CD / DVD
        - U 盘 USB flash drive

网络

- 局域网 / 广域网

    - 局域网 LAN：学校 / 公司
    - 广域网 WAN：互联网


## 关于性能

响应时间

- 定义：系统对外部请求做出反应所需的时间（ how long it takes to do a task）
- 对交互系统，最好在一秒钟做出
- 主要对用户来说
- 影响因素：
    - 硬件性能：CPU、内存、存储速度等
    - 软件效率：算法复杂度、代码优化等
    - 网络延迟：数据传输时间、带宽等

吞吐率

- 定义：单位时间内系统处理的任务数量（ how many tasks can be processed per unit time）
- 主要对服务器来说

关联：当任务数量多于吞吐率，新任务进来响应时间变长

影响因素：

- CPU 主频（时钟频率）4G / 2G

评判标准：执行同样任务所用时间的倒数

$$Performance = 1 / Execution Time$$

$$Performance_x / Performance_y = Execution Time_y / Execution Time_x$$

时间的影响因素：

- CPU 计算时间：重点关注
    - 操作系统所用时间
    - 应用程序所用时间
- 数据访问时间
    - 与内存有关（内存性能 / 大小），内存小得放硬盘上，慢
    - 与 Cache 有关（Cache 性能 / 大小），Cache 小得放内存上，慢
- 外部设备（网络等）时间

CPU 时钟（CPU clocking）

- 2G：2GHz：250ps：250皮秒：250×10^-12秒

- 时钟频率 = 1 / 时钟周期

例如加法器，在时钟周期开始时读取两个输入，因为门电路有延迟等待信号稳定，到时钟周期末尾算出来，且信号稳定，给下一个单元

CPU 时间

- 简化：假设只有一个程序在运行

$$CPU Time = CPU Clock Cycles × Clock Cycle Time = CPU Clock Cycles  / Clock Rate$$

提高性能的方法：

- 减少时钟周期数（怎么减少？为什么能减少？）
    - 改变硬件设计
- 提高主频：减少时钟周期时间（提高时钟频率）
    - 近几年很难提高了

在做优化时候，增加 A 因素，无法做到 B 因素不变


时钟周期数 & CPI

- 影响因素：

    - 指令数（机器码指令）
    - 每条指令的平均时钟周期数 CPI（Cycles Per Instruction）

$$Clock Cycles = Instruction Count × CPI$$

$$CPU Time = Instruction Count × CPI × Clock Cycle Time = Instruction Count × CPI / Clock Rate$$

影响因素：

- 硬件工艺
- 指令集
- 编译器
- 高级语言
- 算法

x86 指令集：复杂指令集体系结构

RISC 指令集：精简指令集体系结构

- 目标：每条指令一个时钟周期
- 复杂操作：汇编语言编程时候写多条指令

