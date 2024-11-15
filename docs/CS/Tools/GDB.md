Here are some of the most frequently needed GDB commands:
break [file:] [function|line]
    Set a breakpoint at function or line (in file).
run [arglist]
    Start your program (with arglist, if specified).
bt  Backtrace: display the program stack.
print expr
    Display the value of an expression.
c   Continue running your program (after stopping, e.g. at a breakpoint).
next
    Execute next program line (after stopping); step over any function calls in the line.
edit [file:]function
	look at the program line where it is presently stopped.
list [file:]function
    type the text of the program in the vicinity of where it is presently stopped.
step
    Execute next program line (after stopping); step into any function calls in the line.
help [name]
    Show information about GDB command name, or general information about using GDB.
quit
exit
    Exit from GDB.

断点

在使用 GDB（GNU Debugger）时，可以通过命令行来设置、查看、删除（消除）断点。以下是一些常用的 GDB 命令来管理断点：

1. **设置断点**：
   - `break main`：在 `main` 函数的开始处设置一个断点。
   - `break filename.c:linenumber`：在指定文件的指定行号处设置一个断点。

2. **查看所有断点**：
   - `info breakpoints`：列出所有断点及其详细信息。

3. **删除（消除）单个断点**：
   - `delete breakpoints编号`：删除指定编号的断点。编号是 GDB 分配给每个断点的唯一标识符，可以通过 `info breakpoints` 命令查看。
   - `clear filename.c:linenumber`：删除指定位置的断点。

4. **删除所有断点**：
   - `delete`：删除所有断点。
   - `delete all`：删除所有断点。

5. **禁用断点**：
   - `disable breakpoints编号`：禁用指定编号的断点。
   - `disable all`：禁用所有断点。

6. **启用断点**：
   - `enable breakpoints编号`：启用指定编号的断点。
   - `enable all`：启用所有断点。

7. **临时更改断点状态**：
   - `break filename.c:linenumber if condition`：设置一个条件断点，只有当 `condition` 为真时，程序才会在该断点处暂停。

8. **查看断点命令**：
   - `commands`：列出与指定断点关联的命令。
   - `commands number`：为指定编号的断点设置一系列命令，当程序在该断点处暂停时，这些命令将自动执行。

### 示例操作：

假设你已经启动了 GDB 并加载了程序：

```bash
gdb myprogram
```

1. **设置断点**：
   ```gdb
   break main
   ```

2. **查看所有断点**：
   ```gdb
   info breakpoints
   ```

3. **删除断点**：
   - 假设你想删除编号为 1 的断点：
     ```gdb
     delete breakpoints 1
     ```

4. **删除所有断点**：
   ```gdb
   delete
   ```

5. **禁用和启用断点**：
   - 禁用编号为 1 的断点：
     ```gdb
     disable breakpoints 1
     ```
   - 启用编号为 1 的断点：
     ```gdb
     enable breakpoints 1
     ```

6. **清除特定位置的断点**：
   ```gdb
   clear filename.c:100
   ```

通过这些命令，你可以有效地管理 GDB 中的断点，以便更精确地控制程序的调试过程。



在 GDB 中，`list` 命令用于显示当前断点处或指定位置的源代码。如果你想要从头开始打印程序的源代码，你可以按照以下步骤操作：

1. **启动 GDB**：
   启动 GDB 并加载你的程序：
   ```bash
   gdb myprogram
   ```

2. **设置断点**（可选）：
   如果你想从程序的入口点（通常是 `main` 函数）开始，可以设置一个断点：
   ```gdb
   break main
   ```

3. **运行程序**（可选）：
   运行程序直到它达到断点：
   ```gdb
   run
   ```

4. **从头开始打印**：
   要从头开始打印程序的源代码，你需要知道源文件的名称。使用 `list` 命令，后面跟上文件名和行号，例如：
   ```gdb
   list filename.c:1
   ```
   这将显示从指定文件的第一行开始的源代码。

5. **使用 `list` 命令**：
   如果你已经在程序的入口点设置了断点并运行了程序，你现在可以使用 `list` 命令来显示当前位置的源代码：
   ```gdb
   list
   ```
   不带参数的 `list` 命令将显示当前断点或当前执行行的源代码。

6. **向前打印源代码**：
   如果你想继续向前打印源代码，可以逐行单步执行，然后再次使用 `list` 命令。例如：
   ```gdb
   next
   list
   ```
   这将执行下一行代码，然后显示下一行的源代码。


请记住，`list` 命令默认显示当前行号的源代码，以及周围的几行代码，以便提供上下文。如果你的程序有多个源文件，你可能需要为每个文件分别使用 `list` 命令。


ll 查看文件
shell ls
shell cat 文件名
