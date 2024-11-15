
[史上最全的Linux常用命令汇总（超全面！超详细！）收藏这一篇就够了！_linux命令-CSDN博客](https://blog.csdn.net/qq_39594419/article/details/142601306)

- vim 文件名：vim中打开文件
- gdb 文件名(.c) -o 文件名(.exe) ：编译（生成executable文件），不包含调试信息
	一次性显示所有错误用它
-  gdb -g 文件名(.c) -o 文件名(.exe) ：编译（生成executable文件），不包含调试信息
- 文件夹位置一定要对 要cd！

查看所有文件夹，具体方法取决于你使用的操作系统和命令行界面。以下是一些常见的方法：


## 查看文件
### 在 Linux 或 macOS 的终端中：

1. **查看当前目录下的文件夹**：
   使用 `ls` 命令可以列出当前目录下的所有文件和文件夹：
   ```sh
   ls
   ```

2. **递归查看所有文件夹**：
   使用 `ls` 命令与 `-r` 参数可以递归地列出所有子目录和文件：
   ```sh
   ls -R
   ```

3. **仅列出文件夹**：
   使用 `ls` 命令与 `-d` 参数可以仅列出文件夹：
   ```sh
   ls -d */
   ```

4. **查看根目录下的所有文件夹**：
   使用 `find` 命令可以查找根目录下的所有文件夹：
   ```sh
   find / -type d
   ```

### 在 Windows 的命令提示符或 PowerShell 中：

1. **查看当前目录下的文件夹**：
   使用 `dir` 命令可以列出当前目录下的所有文件和文件夹：
   ```cmd
   dir
   ```

2. **递归查看所有文件夹**：
   使用 `dir` 命令与 `/s` 参数可以递归地列出所有子目录和文件：
   ```cmd
   dir /s
   ```

3. **仅列出文件夹**：
   使用 `dir` 命令与 `/ad` 参数可以仅列出文件夹：
   ```cmd
   dir /ad
   ```

4. **查看所有驱动器**：
   在命令提示符中，使用 `vol` 命令可以查看所有驱动器：
   ```cmd
   vol
   ```

5. **查看特定驱动器的文件夹**：
   在命令提示符中，使用 `cd` 命令切换到特定驱动器，然后使用 `dir` 命令：
   ```cmd
   cd D:
   dir
   ```

### 使用图形界面：

1. **在 Windows 中**：
   - 打开文件资源管理器，可以看到所有驱动器和文件夹。

2. **在 macOS 中**：
   - 打开 Finder，可以看到所有驱动器和文件夹。

3. **在 Linux 中**：
   - 打开文件管理器（如 Nautilus、Dolphin 等），可以看到所有驱动器和文件夹。

这些方法可以帮助你查看系统中的所有文件夹。如果你需要进一步的帮助，请提供更多的上下文信息。


## 移动文件位置

在 Linux 中，你可以使用 `mv` 命令来批量移动文件。以下是一些常见的方法：

### 1. 移动多个文件到同一个目录

如果你想要将多个文件移动到同一个目录，你可以这样做：

```sh
mv file1.txt file2.txt /path/to/destination/
```

这里，`file1.txt` 和 `file2.txt` 是要移动的文件，`/path/to/destination/` 是目标目录。

### 2. 使用通配符移动文件

你可以使用通配符来选择多个文件。例如，要移动当前目录下所有的 `.txt` 文件到另一个目录：

```sh
mv *.txt /path/to/destination/
```

### 3. 使用 `find` 命令

如果你需要更复杂的选择条件，可以使用 `find` 命令。例如，移动当前目录及子目录下所有 `.log` 文件：

```sh
find . -name "*.log" -exec mv {} /path/to/destination/ \;
```

这里，`find .` 表示在当前目录及其子目录中查找，`-name "*.log"` 表示查找所有以 `.log` 结尾的文件，`-exec mv {} /path/to/destination/ \;` 表示对找到的每个文件执行 `mv` 命令。

### 4. 使用 `xargs` 命令

`xargs` 命令可以将标准输入数据转化为命令行参数。例如，移动当前目录下所有 `.jpg` 文件：

```sh
find . -name "*.jpg" | xargs mv -t /path/to/destination/
```

这里，`find . -name "*.jpg"` 找到所有 `.jpg` 文件，`|` 将结果传递给 `xargs`，`mv -t /path/to/destination/` 将这些文件移动到目标目录。

### 5. 使用 `rsync` 命令

`rsync` 也可以用来移动文件，并且它在复制大量数据时非常高效。例如：

```sh
rsync -av --remove-source-files /path/to/source/ /path/to/destination/
```

这里，`-av` 表示详细输出和保留链接，`--remove-source-files` 表示在复制后删除源文件，相当于移动操作。

### 注意事项

- 确保目标目录存在，否则 `mv` 命令会失败。
- 使用通配符和 `find` 命令时要小心，确保你的选择条件是正确的，以避免意外移动或覆盖文件。
- 在执行批量操作之前，可以先使用 `echo` 命令查看将要移动的文件列表，确保它们是你想要移动的文件。

这些方法可以帮助你批量移动文件。如果你有特定的需求或遇到问题，请提供更多的信息。


## 查看文件

在 Linux 系统中，查看文件的内容可以通过多种方式实现，具体取决于文件的类型和大小。以下是一些常用的命令：

### 1. `cat`
用于查看小到中等大小的文本文件的内容。
```sh
cat filename.txt
```

### 2. `less`
用于查看大文件的内容，因为它允许你逐页查看文件。
```sh
less filename.txt
```
你可以使用方向键来上下翻页，按 `q` 退出。

### 3. `more`
与 `less` 类似，但功能较少，不支持回滚查看。
```sh
more filename.txt
```
按空格键向下翻页，按 `b` 回滚一页，按 `q` 退出。

### 4. `head`
查看文件的前几行，默认是前10行。
```sh
head filename.txt
```
你也可以指定行数，例如查看前20行：
```sh
head -n 20 filename.txt
```

### 5. `tail`
查看文件的最后几行，默认是最后10行。
```sh
tail filename.txt
```
指定行数，例如查看最后20行：
```sh
tail -n 20 filename.txt
```
实时查看文件新增内容：
```sh
tail -f filename.txt
```
按 `Ctrl+C` 退出。

### 6. `grep`
搜索文件中包含特定文本的行。
```sh
grep "search_term" filename.txt
```

### 7. `od`
以八进制、十进制、十六进制等格式查看文件的二进制内容。
```sh
od -c filename
```
这里 `-c` 选项以字符形式显示。

### 8. `vim` 或 `vi`
使用文本编辑器查看文件内容。
```sh
vim filename.txt
```
在 Vim 中，你可以按 `i` 进入插入模式编辑文件，按 `:q` 退出。

### 9. `nano`
另一个文本编辑器，适合初学者。
```sh
nano filename.txt
```
按 `Ctrl+X` 退出。

### 10. `file`
查看文件类型。
```sh
file filename
```

### 11. `strings`
从二进制文件中提取可打印的字符串。
```sh
strings filename
```

### 注意事项
- 对于非常大的文件，避免使用 `cat`，因为它会一次性将整个文件加载到内存中。
- 使用 `less` 或 `more` 可以更有效地查看大文件。
- 如果你只是想要查看文件的一部分，使用 `head` 或 `tail`。
- 如果你想要搜索文件内容，使用 `grep`。
- 如果你想要编辑文件，可以使用 `vim` 或 `nano`。

根据你的具体需求选择合适的命令。如果你需要进一步的帮助，请提供更多的上下文信息。


## ls

`ls` 是一个在 Unix 和类 Unix 系统（如 Linux 和 macOS）中常用的命令行工具，用于列出目录内容。它显示文件和目录的名字，以及其他一些有用的信息。以下是一些 `ls` 命令的基本用法和选项：

### 基本用法

- **列出当前目录的内容**：
  ```sh
  ls
  ```

- **列出指定目录的内容**：
  ```sh
  ls /path/to/directory
  ```

### 常用选项

- **`-a` 或 `--all`**：显示所有文件，包括隐藏文件（以点 `.` 开头的文件）。
  ```sh
  ls -a
  ```

- **`-l`**：以长格式列出文件信息，包括权限、所有者、大小等。
  ```sh
  ls -l
  ```

- **`-h`**：与 `-l` 一起使用时，以易读的格式显示文件大小（例如 KB、MB）。
  ```sh
  ls -lh
  ```

- **`-R` 或 `--recursive`**：递归列出所有子目录的内容。
  ```sh
  ls -R
  ```

- **`-t`**：按修改时间排序，而不是默认的字母顺序。
  ```sh
  ls -lt
  ```

- **`-r` 或 `--reverse`**：反向排序。
  ```sh
  ls -ltr
  ```

- **`--color`**：显示颜色，以区分不同类型的文件和目录。
  ```sh
  ls --color
  ```

- **`-i`**：显示文件的 inode 号。
  ```sh
  ls -li
  ```

- **`--time={time-style}`**：显示文件的时间戳，`time-style` 可以是 `atime`（访问时间）、`birth`（创建时间）、`change`（状态更改时间）、`modification`（修改时间）等。
  ```sh
  ls --time=modification
  ```

### 示例

- **列出当前目录下的所有文件和目录**：
  ```sh
  ls -a
  ```

- **以长格式列出当前目录下的所有文件和目录，并显示文件大小**：
  ```sh
  ls -lh
  ```

- **递归列出当前目录下所有子目录的内容**：
  ```sh
  ls -R
  ```

- **列出当前目录下的所有文件和目录，并按修改时间排序**：
  ```sh
  ls -lt
  ```

- **列出当前目录下的所有文件和目录，并按修改时间反向排序**：
  ```sh
  ls -ltr
  ```

- **显示文件的 inode 号**：
  ```sh
  ls -li
  ```

### 组合使用选项

你可以组合多个选项来实现更复杂的功能。例如，`ls -lah` 会列出当前目录下的所有文件和目录（包括隐藏文件），并以易读的格式显示文件大小。

`ls` 命令非常强大，通过不同的选项组合，可以满足各种不同的需求。


## 通配符

在 Linux 和其他类 Unix 系统中，通配符是一种特殊的字符，用于在文件名、路径名或命令参数中匹配一个或多个字符。它们通常用于文件操作命令，如 `ls`、`cp`、`mv` 等。以下是一些常用的通配符：

1. **星号（*）**：
   - 匹配零个或多个字符。
   - 示例：`*.txt` 匹配所有以 `.txt` 结尾的文件。

2. **问号（?）**：
   - 匹配任意单个字符。
   - 示例：`file?.txt` 匹配以 `file` 开头，后面跟任意一个字符，以 `.txt` 结尾的文件。

3. **方括号（[ ]）**：
   - 匹配方括号内的任意单个字符。
   - 示例：`file[0-9].txt` 匹配以 `file` 开头，后面跟任意一个数字，以 `.txt` 结尾的文件。
   - 示例：`file[a-z].txt` 匹配以 `file` 开头，后面跟任意一个小写字母，以 `.txt` 结尾的文件。

4. **反斜杠（\）**：
   - 用于转义通配符，使其被视为普通字符。
   - 示例：`\*.txt` 匹配名为 `*.txt` 的文件，而不是所有 `.txt` 文件。

5. **括号（{}）**：
   - 匹配大括号内的任意值。
   - 示例：`file{1,2,3}.txt` 匹配 `file1.txt`、`file2.txt` 和 `file3.txt`。
   - 示例：`file[0-9]{2}.txt` 匹配 `file00.txt` 到 `file99.txt`。

6. **排除字符（!）**：
   - 与方括号结合使用，表示不匹配方括号内的字符。
   - 示例：`file[!0-9].txt` 匹配不包含数字的 `file` 开头的 `.txt` 文件。

### 示例

- **列出当前目录下的所有 `.txt` 文件**：
  ```sh
  ls *.txt
  ```

- **列出当前目录下的所有以 `.log` 结尾的文件**：
  ```sh
  ls *.log
  ```

- **列出当前目录下的所有以 `a` 开头的文件**：
  ```sh
  ls a*
  ```

- **列出当前目录下的所有以 `a` 开头，后跟任意字符的文件**：
  ```sh
  ls a?*
  ```

- **列出当前目录下的所有以 `a` 开头，后跟一个数字的文件**：
  ```sh
  ls a[0-9]*
  ```

- **列出当前目录下的所有以 `a` 开头，后跟两个相同字母的文件**：
  ```sh
  ls a[[:alpha:]]\{2\}
  ```

- **列出当前目录下的所有不以 `.txt` 结尾的文件**：
  ```sh
  ls *[!.txt]
  ```

通配符非常有用，特别是在处理大量文件时，它们可以大大简化命令的输入和文件的操作。


- 1.搜索桌面目录下，文件名包含 1 的文件

```c
find -name "*1*"
```

- 2.搜索桌面目录下，所有以 .txt 为扩展名的文件

```c
find -name "*.txt"
```

- 3.搜索桌面目录下，以数字 1 开头的文件

```c
find -name "1*"
```

在Zsh（或者任何Unix-like系统的shell中）新建文件夹（也称为目录），你可以使用`mkdir`命令。以下是一些常用的`mkdir`命令示例：

1. **新建单个文件夹**：
   ```zsh
   mkdir new_folder
   ```
   这将在当前目录下创建一个名为`new_folder`的新文件夹。

2. **新建多个文件夹**：
   ```zsh
   mkdir folder1 folder2 folder3
   ```
   这将创建三个名为`folder1`、`folder2`和`folder3`的新文件夹。

3. **新建嵌套文件夹**：
   ```zsh
   mkdir -p new_folder/sub_folder1/sub_sub_folder
   ```
   使用`-p`选项可以创建嵌套的目录结构。如果父目录不存在，`mkdir`也会创建它们。

4. **新建文件夹并设置权限**：
   ```zsh
   mkdir -m 755 new_folder
   ```
   `-m`选项允许你设置文件夹的权限。在这个例子中，`755`权限意味着文件夹所有者有读、写和执行权限，而组和其他用户有读和执行权限。

5. **使用变量新建文件夹**：
   ```zsh
   folder_name="new_folder"
   mkdir "$folder_name"
   ```
   这将根据变量`folder_name`的值创建一个文件夹。

6. **新建文件夹并显示消息**：
   ```zsh
   mkdir new_folder && echo "Folder created: new_folder"
   ```
   这个命令在创建文件夹后会显示一个消息。

7. **检查文件夹是否创建成功**：
   ```zsh
   mkdir new_folder && echo "Folder created successfully." || echo "Failed to create folder."
   ```
   这个命令在文件夹创建成功时显示成功消息，否则显示失败消息。

这些是Zsh中创建文件夹的基本命令和一些实用技巧。你可以根据自己的需求选择合适的命令。

在Zsh（以及大多数Unix-like系统的shell中），你可以使用`mv`（move）命令来移动文件或目录。以下是一些使用`mv`命令的示例：

1. **移动单个文件**：
   ```zsh
   mv source_file.txt /path/to/destination/
   ```
   这会将`source_file.txt`从当前位置移动到指定的目的地路径。

2. **移动多个文件到同一目录**：
   ```zsh
   mv file1.txt file2.txt file3.txt /path/to/destination/
   ```
   这会将`file1.txt`、`file2.txt`和`file3.txt`移动到指定的目的地路径。

3. **移动目录**：
   ```zsh
   mv /path/to/source_directory /path/to/destination/
   ```
   这会将整个`source_directory`目录移动到指定的目的地路径。

4. **重命名并移动文件**：
   ```zsh
   mv source_file.txt /path/to/destination/new_name.txt
   ```
   这会将`source_file.txt`移动到指定的目的地路径，并重命名为`new_name.txt`。

5. **交互式移动**：
   ```zsh
   mv -i source_file.txt /path/to/destination/
   ```
   使用`-i`（interactive）选项，`mv`命令会在覆盖任何文件之前提示你确认。

6. **移动文件并保留链接**：
   ```zsh
   mv -n source_file.txt /path/to/destination/
   ```
   使用`-n`（no-clobber）选项，`mv`命令不会覆盖目的地的任何文件。

7. **移动文件并更新符号链接**：
   ```zsh
   mv -T source_file.txt /path/to/destination/
   ```
   使用`-T`选项，`mv`命令会将源文件移动到目标位置，并更新指向源文件的任何符号链接。

8. **移动文件并显示详细信息**：
   ```zsh
   mv -v source_file.txt /path/to/destination/
   ```
   使用`-v`（verbose）选项，`mv`命令会在移动文件时显示详细信息。

9. **移动文件并备份任何被覆盖的文件**：
   ```zsh
   mv -b source_file.txt /path/to/destination/
   ```
   使用`-b`选项，`mv`命令会在覆盖任何文件之前备份它们。

请确保替换`source_file.txt`、`source_directory`、`file1.txt`、`file2.txt`、`file3.txt`以及路径为你实际要移动的文件或目录的名称和路径。使用`mv`命令时，如果目标路径不存在，它可能会报错，所以确保目标路径是正确的。

在Zsh（以及大多数Unix-like系统的shell中），你可以使用`rm`命令来删除文件夹。以下是一些使用`rm`命令删除文件夹的示例：

1. **删除空文件夹**：
   ```zsh
   rm -d folder_name
   ```
   或者
   ```zsh
   rmdir folder_name
   ```
   这两个命令都可以删除名为`folder_name`的空文件夹。

2. **删除非空文件夹**：
   ```zsh
   rm -r folder_name
   ```
   `-r`（或`-R`）选项告诉`rm`命令递归地删除文件夹及其内容。

3. **强制删除非空文件夹**：
   ```zsh
   rm -rf folder_name
   ```
   `-f`选项用于强制删除，不会提示任何确认。

4. **删除文件夹并显示详细信息**：
   ```zsh
   rm -rv folder_name
   ```
   `-v`选项使`rm`命令在删除时显示详细信息。

5. **删除文件夹并保留父目录**：
   ```zsh
   rm -r folder_name/*
   ```
   这个命令会删除`folder_name`文件夹内的所有内容，但保留文件夹本身。

6. **删除文件夹并备份**：
   ```zsh
   rm -r -i folder_name
   ```
   `-i`选项会在删除每个文件之前提示你确认。

7. **删除文件夹并保留父目录（使用通配符）**：
   ```zsh
   shopt -s dotglob
   rm -r folder_name/*
   shopt -u dotglob
   ```
   使用`shopt -s dotglob`可以确保连同隐藏文件一起删除。

请注意，删除文件和文件夹是一个不可逆的操作，一旦执行，被删除的文件和文件夹将无法恢复。因此，在执行删除操作之前，请确保你确实想要删除这些文件和文件夹，并且已经做好了必要的备份。

**安全提示**：使用`rm -rf`时要特别小心，因为它会递归地强制删除文件夹及其所有内容，没有任何确认提示。这可能会导致数据丢失，特别是如果你不小心指定了错误的路径。

在Unix-like系统中，包括使用Zsh的系统，你可以通过多种方式新建一个`.c`文本文件。以下是一些常用的方法：

1. **使用`touch`命令**：
   ```zsh
   touch new_file.c
   ```
   这个命令会在当前目录下创建一个名为`new_file.c`的新文件。如果文件已存在，`touch`命令会更新文件的访问和修改时间。

2. **使用`vim`编辑器**：
   ```zsh
   vim new_file.c
   ```
   这个命令会打开`vim`编辑器，并创建一个名为`new_file.c`的新文件。按`Esc`键，输入`:wq`（保存并退出），然后按`Enter`键保存文件并退出编辑器。

3. **使用`nano`编辑器**：
   ```zsh
   nano new_file.c
   ```
   这个命令会打开`nano`编辑器，并创建一个名为`new_file.c`的新文件。编辑完成后，按`Ctrl + X`退出，然后按`Y`保存更改，最后按`Enter`键确认文件名。

4. **使用`emacs`编辑器**：
   ```zsh
   emacs new_file.c
   ```
   这个命令会打开`emacs`编辑器，并创建一个名为`new_file.c`的新文件。编辑完成后，按`Ctrl + X`然后按`Ctrl + S`保存更改，最后按`Ctrl + X`然后按`Ctrl + C`退出编辑器。

5. **使用`echo`命令**：
   ```zsh
   echo "#include <stdio.h>" > new_file.c
   ```
   这个命令会创建一个名为`new_file.c`的新文件，并写入一行代码`#include <stdio.h>`。`>`操作符会覆盖文件内容，如果文件已存在。

6. **使用`cat`命令**：
   ```zsh
   cat > new_file.c
   ```
   然后开始输入代码，输入完成后，按`Ctrl + D`结束输入。这会将你的输入保存到`new_file.c`文件中。

7. **使用`gedit`编辑器**（如果已安装）：
   ```zsh
   gedit new_file.c &
   ```
   这个命令会打开`gedit`图形界面编辑器，并创建一个名为`new_file.c`的新文件。编辑完成后，保存并关闭编辑器。

选择哪种方法取决于你的个人偏好和可用的编辑器。如果你只是想快速创建一个空的`.c`文件，`touch`命令是最快的方法。如果你需要立即开始编写代码，使用一个文本编辑器会更方便。

如果你已经将Visual Studio Code (VSCode) 和 Zsh 连接，并且想要新建一个文本文件并用 VSCode 编辑，可以通过以下步骤实现：

1. **使用命令行**：
   打开终端（Terminal），然后使用`code`命令来新建文件并打开编辑器。这个命令会创建一个新文件，并在 VSCode 中打开它。

   ```zsh
   code new_file.c
   ```

   这个命令会创建一个名为`new_file.c`的新文件，并自动用 VSCode 打开它。如果`new_file.c`文件已存在，VSCode 会直接打开该文件。

2. **使用VSCode的终端**：
   如果你在 VSCode 内部使用集成终端（Integrated Terminal），同样可以使用`code`命令新建并编辑文件。

3. **使用快捷方式**：
   在 VSCode 中，你也可以通过快捷方式来新建文件：
   - 打开 VSCode。
   - 按下 `Ctrl + N`（在 macOS 上是 `Cmd + N`）来新建一个文件。
   - 保存文件时，使用 `Ctrl + S`（在 macOS 上是 `Cmd + S`）并选择保存位置和文件名。

4. **使用VSCode的命令面板**：
   - 打开 VSCode。
   - 按下 `F1` 或 `Ctrl + Shift + P`（在 macOS 上是 `Cmd + Shift + P`）打开命令面板。
   - 输入并选择“File: New File...”来新建一个文件。
   - 保存文件时，使用 `Ctrl + S`（在 macOS 上是 `Cmd + S`）并指定文件名和位置。

5. **使用VSCode的图形界面**：
   - 打开 VSCode。
   - 点击左侧的“资源管理器”图标（Explorer icon）。
   - 右键点击你想要新建文件的文件夹。
   - 选择“New File”来创建一个新文件。
   - 保存文件时，使用 `Ctrl + S`（在 macOS 上是 `Cmd + S`）并指定文件名。

以上是在 VSCode 和 Zsh 连接后，新建文本文件并用 VSCode 编辑的一些常用方法。`code`命令是 VSCode 的一部分，它允许你从命令行直接在 VSCode 中打开文件和文件夹。
