> Ubuntu is the world’s favourite Linux operating system. Run it on your laptop, workstation, server or IoT device, with five years of free security updates.

![](https://files.mdnice.com/user/88229/3ad74c35-3a1c-4542-99d8-4854d38ffebc.png)

以及，请看我如何帮助 Colin 实现 *他的美甲梦* ~


![](https://files.mdnice.com/user/88229/cd5b3a87-d153-424b-a061-be7d29992c69.png)


Let's start !

<div style="text-align: center; font-weight: bold; font-size: 1.6em;">
    Linux虚拟机安装
</div>

##### 第一步：打开powershell管理员模式

方法：按 `win + X`，选择带有“管理员”字样的那个

##### 第二步：安装 Ubuntu

前提：科学上网

方法：输入以下命令以安装 Ubuntu
  ```shell
  wsl --install -d Ubuntu
  ```
##### 第三步：按照提示操作即可

---

<div style="text-align: center; font-weight: bold; font-size: 1.6em;">
    Zsh安装
</div>

#### 第一步：安装zsh

仍然在命令提示符处，输入以下命令：

使用root用户，并更新apt：
```shell
sudo apt update
```
安装zsh：
```shell
sudo apt-get install zsh
```

#### 第二步：将zsh设置为默认终端

```shell
chsh -s $(which zsh)
```

再打开一个 Ubuntu 的 terminal，你将看到如下内容，证明以上步骤均成功


![](https://files.mdnice.com/user/88229/970f6369-c572-4676-b5e2-28fb58345873.png)


按照上图中他的提示做即可，建议输入：

```shell
0
```

#### 第三步：安装oh-my-zsh

Tips：VPN在虚拟机不能同步（似乎v2rayN支持Ubuntu但是我没有尝试），所以开梯子没啥用，可能等到某个风和日丽的日子可能就成功了（from gsgg）

![](https://files.mdnice.com/user/88229/346e29bd-4cc8-4a2e-adec-9836b3cebd09.jpg)
<div style="text-align: center;">
    上图为我成功安装之后随手拍的窗外景象<br>
    的确风和日丽……
</div>

以下命令选一个即可

```shell
# 用curl
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
```shell
# 用wget
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
```shell
# 换gitee源
sh -c "$(curl -fsSL https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh)"
```

```shell
# 换清华源
sh -c "$(curl -fsSL https://mirrors.tuna.tsinghua.edu.cn/github-raw/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

```shell
# 换浙大源
sh -c "$(curl -fsSL https://mirrors.zju.edu.cn/oh-my-zsh/oh-my-zsh/master/tools/install.sh)"
```

#### 第四步：配置zsh

##### 第一步：用vim打开~./zshrc

```shell
vim ~./zshrc
```

这里涉及一些简单的vim命令：
  - 输入 `i` 进入插入模式
  - 点击 `Esc` 进入普通模式
  - 输入 `:wq` 保存并退出

##### 第二步：跟着感觉走

1. 主题：在 `ZSH_THEME` 处更改，我使用的是 `agnoster`

2. 插件：可自行搜索，我使用了`zsh-autosuggestions`（命令建议）、`zsh-history-substring-search`（命令建议）、`zsh-syntax-highlighting`（语法高亮）

    方法：先在 `plugins=(git)` 处添加这三个，再退出vim，按如下命令安装（此处只给出直接 `git clone` 的方法，也可以换源，一个方法不行就换另一个，同时建议开流量 ~）

      - zsh-autosuggestions
          ```shell
          git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
          ```

      - zsh-syntax-highlighting
          ```shell
          git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
          ```

      - zsh-history-substring-search
          ```shell
          git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-history-substring-search
          ```
        
3. 字体：我使用的是JetBrains Mon。首先，在[官网](https://www.jetbrains.com/lp/mono/)下载并在文件夹（path-to-downloaded-files\JetBrainsMono-2.304\fonts\ttf）中选择你喜欢的那个，点开，点击安装

4. 其他设置：打开命令提示符，点击顶栏下拉菜单中“设置”，进入Ubuntu，在“外观”处设置字体和其他内容

---

<div style="text-align: center; font-weight: bold; font-size: 1.6em;">
    Zsh食用小记
</div>

### 安装 anaconda

#### 第一步：下载安装脚本
以下命令选一个即可：

```bash
# 使用 wget
wget https://repo.anaconda.com/archive/Anaconda3-2023.07-1-Linux-x86_64.sh
```
```shell
# 使用 curl
curl -O https://repo.anaconda.com/archive/Anaconda3-2023.07-1-Linux-x86_64.sh
```

#### 第二步：运行安装脚本

```bash
bash Anaconda3-2023.07-1-Linux-x86_64.sh
```

Tips：这里一定要用 `bash` 命令而不能用 `zsh`，因为 `zsh` 对语法的检查比 `bash` 严格，导致安装脚本中 `Anaconda3-2023.07-1-Linux-x86_64.sh:377: no matches found: /home/rzzhang/download/anaconda3/pkgs/envs/*/` 文件无法夹正确下载，应该就是通配符检查的问题。

#### 第三步：按照提示操作

确认权限处一直输入 yes ，安装路径处我选择输入新安装路径 : `/home/<user-name>/download/anaconda3`，或者选择默认路径亦可（直接按 `Enter` 确认。

安装完成后，安装程序会提示你是否将 Anaconda 添加到环境变量中：
```
Do you wish the installer to initialize Anaconda3 by running conda init? [yes|no]
```
输入 `yes`


#### 第四步：重新加载 .zshrc 文件
```bash
source ~/.zshrc
```

#### 第五步：验证安装

```bash
conda --version
```


### 安装 chromium

缘起：Colin提出希望做烟花🎇样式的美甲，我这里恰好写过一个模拟烟花的代码，为圆**他**的美甲💅梦，需要运行并展示，然而新电脑并没有安装chromium……

Tips：pip 是 Python 的包管理工具，用于安装 Python 库和工具。然而，Chromium 浏览器和 ChromeDriver 并不是 Python 库，而是 Linux 系统的软件包，需要通过系统的包管理器（如 apt）来安装，不能通过 pip 直接安装。    

#### 第一步：使用 apt 包管理器安装

更新apt
```shell
sudo apt update
```
安装 chromium 浏览器
```shell
sudo apt install chromium-browser
```
安装 chromedriver
```shell
sudo apt install chromium-chromedriver
```

#### 第二步：验证安装

启动 chromium

```shell
chromium-browser
```
若成功打开如下页面则证明安装成功。
![](https://files.mdnice.com/user/88229/fe7c3845-68e6-4fa5-9cae-9accb9a6041d.png)

检查 chromedriver 版本
```shell
chromedriver --version
```
若输出 chromedriver 版本则证明安装成功。

Tips：由于Ubuntu默认使用snap下载chromium，所以即使用该方法也会自动调用snap，如果没有则会下载它。

> "默认使用 Snap 是因为维护成本低、自动更新方便、跨平台支持好、依赖管理简单且安全性高。"

最终，chromium被安装在 `~/snap/chromium` 目录下。

#### 第三步：在虚拟环境中安装相关python包

安装 webdriver-manager，一款自动管理浏览器驱动器的包

```shell
pip3 install webdriver-manager 
```
安装 selenium，一款可以实现 Web 应用程序的自动化测试（模拟用户在浏览器中的操作，如点击按钮、填写表单、导航页面等）的包

```shell
pip3 install selenium
```




## 后记
俗话说，一杯茶一根烟 一个环境配一天。

在配linux环境过程中，最容易出现的问题（个人遇到的）是网络连接障碍，可尝试：连接手机热点 or 换源 or 换件别的事干干（

