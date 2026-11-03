## 零零碎碎看到的东西

- vscode里面的文件配置是干什么？json文件是什么？

    .vscode 文件夹：VSCode 支持项目级别的配置，可以在项目根目录下创建一个 .vscode 文件夹，存放配置文件，例如：

    settings.json: 自定义项目的设置。
    launch.json: 配置调试选项。
    tasks.json: 配置自动化任务。

- `#include` 报错，提示更新 includePath

    先分清是 VSCode 的红线，还是编译器真的报错。`includePath` 给编辑器做补全 / 检查用；编译时找头文件用的是编译器默认路径和 `-I`。

    例如 `gcc -Iinclude main.c -o main`。编辑器不报错，不代表这条编译命令就能找到头文件。

- 各种报错信息

    - `No such file or directory`：先看缺的是哪个文件、路径相对谁。
    - `undefined reference`：通常已经编译到链接阶段，检查实现文件有没有一起编译、库有没有链接。
    - `Segmentation fault`：运行时非法访存，先看数组越界、空指针和已经 free 的内存。

    多文件例子：`gcc main.c func.c -o main`。只编 `main.c`，即使 include 了 `func.h`，也不会自动把 `func.c` 的实现加进来。

- [搜：gcc gnu g++ ……](https://blog.csdn.net/weixin_41973774/article/details/120219649)

- [意面代码、圈复杂度](https://blog.csdn.net/msc1211/article/details/120446642)

- [gcc](https://blog.csdn.net/qq_42965223/article/details/122739839), [gcc-better](https://blog.csdn.net/b_ingram/article/details/118946166)

- [python多线程](https://blog.csdn.net/qq_42475711/article/details/106956460)

- C++ 模块化开发

    头文件写对外的声明，`.cpp` 写实现，编译后再链接。头文件不是“自动帮你找实现”的东西。

    [大程序结构](../pl/C/09-program-structure.md)讲的是这个基本流程；C++20 的 modules 是另一套语言机制，不是单纯把文件分开就叫 modules。

- 端口

    IP 找到设备，端口找到服务。HTTP 常见是 80，HTTPS 是 443；本地开发的 3000 / 8000 等由程序自己设置。

    `127.0.0.1:8000`：只访问自己这台电脑。服务只监听 `127.0.0.1` 时，另一台电脑不能靠换成你的局域网 IP 就访问到它。

    [网络与端口命令](../tools/shell.md)里查 `ss` / `lsof`，先确认谁在监听，再看地址、防火墙、代理。

- 搜索：大程序结构文件夹命名

    [程序员的自我修养（各种东西）](https://leohxj.gitbooks.io/a-programmer-prepares/content/code-review/code-review-list.html)

    [文件命名超全](https://zhuanlan.zhihu.com/p/161640510)



- GitBook

    把文档组织成网站的一种工具 / 服务。它和 Git 不是一回事，Git 管版本，GitBook 管文档展示。


## 知识

- [cmake](https://blog.csdn.net/Torres_10/article/details/80371425)

- [makefile](https://blog.csdn.net/ruglcc/article/details/7814546/)

- [用vscode编写大project-2](https://docs.pingcode.com/ask/272978.html)，[1](https://www.cnblogs.com/Roboduster/p/15315817.html)

- 快捷键：先记常用的几个，查[这里](shortcuts.md)，不用一下背完整张表。

- **嵌入式开发先分清几件事**

    - 程序在目标板上运行，电脑负责编辑、编译、下载和调试。
    - GPIO 控制引脚高低电平，UART 做串口通信，I²C / SPI 常用来接传感器。
    - 先跑通 LED、串口，再接一个传感器；每一步都能看到结果，比较容易定位问题。

- [chat with deekseek](https://chat.deepseek.com/a/chat/s/156b1d31-b891-4384-9c6c-f8dcf4872e06)