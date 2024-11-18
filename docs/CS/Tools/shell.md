>from MIT Missing Semester of Your CS Education

- terminal: 呈现shell的地方

- bash: the most widely used shell on linux

- prompt: 命令提示符，就这个东西

![alt text](image.png)

在命令提示符后面，你输入的是：程序名称 + 参数

And, use spaces to seprate the arguments, and if your need to include space in one argument, use \ before the space or "" or ''.

```shell
date
echo hello\ world
mkdir "my photes" # the right way
mkdir my photos # you might create 2 directory(my and photos)
# 其中：echo and date and mkdir 是程序名称，后面的是参数，即这里shell执行的就是带参数的程序
```

## enviroment variable
How does the shell know what to do when you type the "echo" or somethong else?

环境变量：设置好的，shell启动时就会自动设置的东西，bash下环境变量其实就是一个编程语言，So, in fact, we can run not only the program with arguments, but also things in programming language, like defining functions, while loops and so on, which is called shell scripting(编写shell脚本)

```shell
echo $PATH
# show all the path, shell就是在这些里面搜索程序的；被冒号分隔
```
本质上，输入程序名称，shell会遍历这些path然后找到名称与我输入的命令相匹配的那个

```shell
which <程序名称>
# 查看我输入这个程序名称后运行的是哪个程序
```

## 路径
win: 由“\”开始(win的根目录为\\)，且每个分区（驱动器）都有一个根目录("\\"), 例如C:\

linux/macos: 由“/”开始(其根目录为/),且所有都在一个根目录下

绝对路径：能完全确定文件位置的完整路径

相对路径：相当于你当前处于的路径来说

例如，用cd改变路径就可以相对 or 绝对路径
![alt text](image-1.png)
```shell
pwd # 打印当前所处绝对路径
cd # 改变路径
# 几个特殊的目录：
. 当前的目录
.. 父目录
.. # 可回到父目录
../../ or ../.. # 回到上上级目录，etc.
~ 代表home/ruizhe
cd - # 切换回上一次所在的目录
```
想要在任何目录下运行程序例如echo, 要么只给出程序名，要么给出绝对路径（相对路径不行）

```shell
ls <目录名> # 可以列出ls后面的参数（目录）下的文件
# 例如：
ls ..
```
其他标志和选项：


| **区别点**   | **标志（Flags）**                | **选项（Options）**             |
|--------------|----------------------------------|---------------------------------|
| **格式**     | 通常是 `-f` 或 `--flag`          | 通常是 `-o value` 或 `--option=value` |
| **参数**     | 通常不需要额外的值               | 通常需要指定一个值              |
| **功能**     | 控制简单开关功能                 | 提供更详细的设置                |
| **组合性**   | 可以组合，例如 `-abc`            | 不能组合，需单独指定            |


查看详细用法：
```shell
ls --help
```
常用
```shell
ls -l # 列出文件的详细信息
```

??? info "detailed info by ChatGPT"

    执行 `ls -l` 命令后，会以**长格式**列出目录或文件的详细信息。每一行代表一个文件或目录，输出内容分为以下几个字段（从左到右）：  

    **1. 文件类型与权限**
    ```bash
    -rw-r--r--
    ```
    - 第一位：文件类型：
    - `-`：普通文件（regular file）
    - `d`：目录（directory）
    - `l`：符号链接（symbolic link）
    - `b`：块设备文件（block device）
    - `c`：字符设备文件（character device）
    - `p`：命名管道（pipe）
    - `s`：套接字（socket）

    - 接下来的9位：文件权限，分为三组，每组三位，分别表示**所有者**、**所在组**、**其他用户**的权限：
    - **r**（read）：可读
    - **w**（write）：可写
    - **x**（execute）：可执行
    - 如果没有权限，用 `-` 表示。

    **示例**：
    ```bash
    -rw-r--r--  # 表示：普通文件，所有者有读写权限，组和其他用户仅有读权限。
    drwxr-xr-x  # 表示：目录，所有者有读、写、执行权限，组和其他用户有读和执行权限。
    ```

    ---

    **2. 链接数**
    ```bash
    2
    ```
    - 表示硬链接的数量，即有多少路径指向该文件。
    - 对于目录，表示该目录中包含的子目录（包括 `.` 和 `..`）。

    ---

    **3. 所有者（User）**
    ```bash
    user
    ```
    - 文件的所有者名称，表示谁创建或拥有该文件。

    ---

    **4. 所属组（Group）**
    ```bash
    group
    ```
    - 文件所属的用户组，组内成员共享该文件的组权限。

    ---

    **5. 文件大小**
    ```bash
    4096
    ```
    - 文件的大小（以字节为单位）。  
    - 对于目录，显示的是目录元数据占用的大小，而非其内容大小。  
    - 如果需要更直观的显示大小，可以使用 `-h`（human-readable）选项：  
    ```bash
    ls -lh
    ```

    ---

    **6. 修改时间**
    ```bash
    2024-11-18 10:30
    ```
    - 文件最近的**修改时间**，格式是 `年月日 时:分`。  
    - 如果文件的修改时间超过半年，则显示年份而不是时间。  

    ---

    **7. 文件名**
    ```bash
    example.txt
    ```
    - 文件或目录的名称。
    - 如果是符号链接，会显示指向的目标路径，例如：
    ```bash
    mylink -> /path/to/target
    ```

    ---

    **完整示例**
    执行 `ls -l` 输出如下：
    ```bash
    -rw-r--r--  1 user group  1024 2024-11-18 10:30 example.txt
    drwxr-xr-x  2 user group  4096 2024-11-18 10:00 my_directory
    ```

    **逐字段解释**：
    1. `-rw-r--r--`：普通文件，所有者有读写权限，组和其他用户仅有读权限。
    2. `drwxr-xr-x`：目录，所有者有读、写、执行权限，组和其他用户有读和执行权限。
    3. `1` 和 `2`：硬链接数量。
    4. `user`：所有者名称。
    5. `group`：所属组名称。
    6. `1024` 和 `4096`：文件或目录大小（字节数）。
    7. 时间：最后修改时间。
    8. `example.txt` 和 `my_directory`：文件名或目录名。

    ---

    常见扩展选项
    - **`-h`**：以易读格式显示文件大小。
    - **`-a`**：显示所有文件，包括隐藏文件（以 `.` 开头）。
    - **`-t`**：按修改时间排序。
    - **`-S`**：按文件大小排序。  

    综合使用这些选项可以更方便地查看文件信息。





words

    argument: 参数
    variable: 变量
    prompt: 命令提示符