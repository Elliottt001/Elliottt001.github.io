## C

1. 更新系统包列表

    ```bash
    sudo apt update
    ```

2. 安装GCC（编译器）

    - 安装
    ```bash
    sudo apt install build-essential  # 这是一个元包，包含 GCC、G++、make 等
    ```

3. 安装GDB（调试）

    ```bash
    sudo apt install gdb
    ```

4. 验证

    ```bash
    gdb --version

    make --version

    gcc --version
    ```

5. VSCode

    1. 下载并安装 [VS Code](https://code.visualstudio.com/)。
    2. 安装 C/C++ 扩展。

## python

1. Ubuntu 通常预装了 Python 3。检查：
    ```bash
    python3 --version
    ```

2. 安装 pip（包管理工具）
    ```bash
    sudo apt install python3-pip
    ```

3. 安装常用工具如ipython

    ```bash
    pip install ipython
    ```


5. VS Code
    1. 安装 VS Code：
        ```bash
        sudo snap install --classic code
        ```
    2. 安装 Python 扩展：
        - 打开 VS Code，点击左侧扩展图标（或按 `Ctrl+Shift+X`）。
        - 搜索 `Python`，安装 Microsoft 提供的官方扩展。


8. 安装 anaconda

    详见[我的另一篇笔记中anaconda部分](https://r-z-zhang-ai.github.io/TUTORIAL/CS/environment/zsh/#anaconda)

## latex