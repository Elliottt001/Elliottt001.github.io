# WSL迁移
前情提要：建议阅读往期文章，先装个虚拟机

由于wsl虚拟机默认装在C盘，而我们💻的C盘经常面临爆满的情况，遂需要将其迁移至其他硬盘。

正片，开始！

注意：下文所有命令中 `Ubuntu` 应替换为你 `wsl -l -v` 中输出的虚拟机实际名称

## 第一步：准备工作

### 1. 检查C、D盘容量

### 2. 检查虚拟机的名称&状态

首先，打开命令提示符：按 `win + R`，在输入框中输入 `cmd`

其次，输入以下命令：

```shell
wsl -l -v
```

会看到如下输出，顾名思义，其显示了虚拟机的名称（NAME）是Ubuntu（这个很重要，对应最开始的“注意”）和运行状态（STATE）Running或者Stopped

### 3. 停止虚拟机的运行

如果上面状态时Stopped，证明已经处于停止状态

如果是Running，则需要输入以下命令：

```shell
wsl --shutdown
```

其次，再次确认，输入以下命令，确保其处于停止状态：

```shell
wsl -l -v
```

>注意：确保未打开 zsh 或者文件资源管理器中 Ubuntu 的文件夹，否则将无法停止wsl运行，这与无法对在word/WPS（**两个严重降低工作效率的可耻的app**）中打开的文件进行删除或者其他操作同理。


## 第二步：导出wsl备份

1. 选择一个你喜欢的硬盘放置 wsl，我选择了D盘。

2. 在D盘创建一个文件夹用来存放WSL，例如 D:\WSL-UBUNTU 。



3. 导出备份（例如命名为Ubuntu.tar），需要输入以下命令：

```shell
wsl --export Ubuntu D:\Ubuntu_WSL\Ubuntu.tar
```

4. 稍等片刻

## 第三步：注销原有wsl

1. 确定认D:\Ubuntu_WSL\文件夹下出现Ubuntu.tar文件

2. 注销，输入以下命令：

```shell
wsl --unregister Ubuntu
```

## 第四步：将备份文件导入

1. 将备份导入D:\Ubuntu_WSL，输入以下命令：

```shell
wsl --import Ubuntu D:\Ubuntu_WSL D:\Ubuntu_WSL\Ubuntu.tar
```

2. 启动wsl以确认是否成功

这里将进入root用户。



## 第五步：恢复默认用户

1. 打开cmd

2. 恢复，输入以下命令：

```shell
Ubuntu config --default-user your-user-name
```



3. 再打开zsh，确认成功

可以尝试输入一些命令~