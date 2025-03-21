## 主机虚拟机互连

在 **WSL（Windows Subsystem for Linux）** 中操控 Windows 主机是完全可行的，因为 WSL 和 Windows 主机共享相同的文件系统和网络环境。以下是几种常见的方法来实现这一目标：

---

### **1. 通过命令行工具操控 Windows 主机**

WSL 可以直接调用 Windows 的可执行文件（如 PowerShell、CMD 等），从而操控 Windows 主机。

#### **步骤：**

1. **在 WSL 中调用 PowerShell**：

   - 打开 WSL 终端。
   - 运行以下命令来调用 Windows 的 PowerShell：
     ```bash
     powershell.exe <command>
     ```
     例如，查看 Windows 主机的 IP 地址：
     ```bash
     powershell.exe ipconfig
     ```

2. **在 WSL 中调用 CMD**：

   - 运行以下命令来调用 Windows 的 CMD：

     ```bash
     cmd.exe /c <command>
     ```
     例如，查看 Windows 主机的系统信息：
     ```bash
     cmd.exe /c systeminfo
     ```

3. **直接运行 Windows 程序**：

   - 你可以直接在 WSL 中运行 Windows 程序。例如，打开记事本：

     ```bash
     notepad.exe
     ```

- **记事本**：

  ```bash
  notepad.exe
  ```
- **计算器**：

  ```bash
  calc.exe
  ```
- **画图工具**：

  ```bash
  mspaint.exe
  ```
- **命令提示符（CMD）**：

  ```bash
  cmd.exe
  ```
- **PowerShell**：

  ```bash
  powershell.exe
  ```

- **文件资源管理器**：

  ```bash
  explorer.exe
  ```
  （打开当前目录的文件资源管理器）。

- **Word**：

  ```bash
  winword.exe
  ```
- **Excel**：

  ```bash
  excel.exe
  ```

- **路径问题**：

  - Windows 应用程序的路径通常位于 `/mnt/c/`（对应 `C:` 盘）或其他挂载的驱动器（如 `/mnt/d/` 对应 `D:` 盘）。
  - 如果应用程序不在系统的 `PATH` 环境变量中，需要提供完整路径。例如：

    ```bash
    /mnt/c/Program\ Files/Google/Chrome/Application/chrome.exe
    ```
    ```bash
    /mnt/c/Program\ Files\ \(x86\)/Microsoft/Edge/Application/msedge.exe
    ```

#### **5. 将 Windows 应用程序添加到 WSL 的 PATH**

为了方便调用，可以将常用的 Windows 应用程序路径添加到 WSL 的 `PATH` 环境变量中。

##### **步骤：**

1. 打开 WSL 终端。
2. 编辑 `~/.bashrc` 或 `~/.zshrc` 文件（取决于你使用的 Shell）：

   ```bash
   nano ~/.bashrc
   ```

3. 添加以下内容（以 `notepad.exe` 为例）：

   ```bash
   export PATH=$PATH:/mnt/c/Windows/System32
   ```

4. 保存并退出，然后运行以下命令使更改生效：

   ```bash
   source ~/.bashrc
   ```

---

### **2. 通过 SSH 操控 Windows 主机**

如果需要在 WSL 中通过 SSH 连接到 Windows 主机，可以启用 Windows 的 OpenSSH 服务器。

#### **步骤：**

1. **在 Windows 主机上启用 OpenSSH 服务器**：

   - 打开“设置” -> “应用” -> “可选功能”。
   - 点击“添加功能”，找到 **OpenSSH 服务器**，然后点击“安装”。
   - 启动 SSH 服务：
     ```bash
     net start sshd
     ```

2. **在 WSL 中通过 SSH 连接 Windows 主机**：

   - 打开 WSL 终端。
   - 使用以下命令连接 Windows 主机：
     ```bash
     ssh username@localhost
     ```
     其中 `username` 是 Windows 主机的用户名。

3. **远程操控 Windows 主机**：

   - 登录后，你可以通过命令行操作 Windows 主机（类似于 PowerShell 或 CMD）。

---

### **3. 使用 WSL 和 Windows 的互操作性**

WSL 和 Windows 主机之间可以无缝共享文件和环境变量。

#### **步骤：**

1. **访问 Windows 文件系统**：

   - 在 WSL 中，Windows 的文件系统挂载在 `/mnt/` 目录下。例如：
     - `C:` 盘对应 `/mnt/c/`
     - `D:` 盘对应 `/mnt/d/`
   - 你可以直接在 WSL 中操作 Windows 文件。例如，列出 `C:` 盘的文件：

     ```bash
     ls /mnt/c/
     ```

2. **在 WSL 中调用 Windows 环境变量**：

   - 你可以通过 `$PATH` 访问 Windows 的环境变量。例如，查看 Windows 的 `PATH`：
     ```bash
     echo $PATH
     ```

3. **在 WSL 中运行 Windows 脚本**：

   - 你可以在 WSL 中直接运行 Windows 的批处理脚本（`.bat`）或 PowerShell 脚本（`.ps1`）。例如：
     ```bash
     /mnt/c/path/to/script.bat
     ```

---

### **4. 使用图形界面工具操控 Windows 主机**

如果你需要在 WSL 中运行 Windows 的图形界面程序，可以配置 X11 转发。

#### **步骤：**

1. **在 Windows 上安装 X11 服务器**：

   - 下载并安装 [VcXsrv](https://sourceforge.net/projects/vcxsrv/) 或其他 X11 服务器。

2. **配置 WSL 使用 X11 服务器**：

   - 在 WSL 中设置 `DISPLAY` 环境变量：
     ```bash
     export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0
     ```

3. **在 WSL 中运行 Windows 图形程序**：

   - 例如，运行 Windows 的计算器：
     ```bash
     calc.exe
     ```

---

### **5. 使用 WSL 和 Windows 的集成工具**

WSL 和 Windows 提供了许多集成工具，可以更方便地操控 Windows 主机。

#### **步骤：**

1. **使用 `wsl` 命令**：

   - 在 Windows 的 PowerShell 或 CMD 中，可以使用 `wsl` 命令直接调用 WSL 的命令。例如：
     ```bash
     wsl ls -l
     ```

2. **使用 `wslg`（WSL 图形支持）**：

   - 如果你使用的是 WSL 2 并启用了 WSLg（WSL 图形支持），可以直接运行 Linux 的图形程序，同时与 Windows 主机无缝集成。

