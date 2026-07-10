## 概念

### 宿主机 & 客户机
宿主机（**Host Machine**）是指运行虚拟机或容器的物理计算机。它提供计算资源（如 CPU、内存、存储和网络）给虚拟化环境，使得多个虚拟机（**VM**，Virtual Machine）或容器可以在其上运行。


- **宿主机（Host Machine）**：物理服务器，运行虚拟化软件（如 KVM、VMware ESXi）。
- **客户机（Guest Machine）**：运行在宿主机上的虚拟机，每个客户机都可以安装独立的操作系统。


### 主机 & 虚拟机


**主机（Host）**  
  指的是运行计算任务的设备，通常指物理计算机，比如一台服务器或个人电脑。  

**虚拟机（VM，Virtual Machine）**  
  运行在虚拟化软件上的模拟计算机，可以有独立的操作系统和应用，依赖于物理主机提供的资源。  

💡 **简单理解**：主机是实际存在的硬件设备，而虚拟机是模拟出来的计算环境。  

| 对比项 | 主机 vs. 虚拟机 | 宿主机 vs. 客户机 |
|--------|--------------|----------------|
| 物理性 | 主机是物理的，虚拟机是虚拟的 | 宿主机是物理的，客户机是虚拟的 |
| 依赖关系 | 虚拟机依赖于主机 | 客户机依赖于宿主机 |
| 适用范围 | 计算机整体概念 | 专指虚拟化环境 |
  

## VMware 食用小记

### Linux virtual machine

#### 换阿里源

```shell
deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
```

#### 安装 open-vm-tools

作用：主机和虚拟机间文件直接拖拽

!!! success

    以上内容见<a href="https://www.bilibili.com/video/BV1A7XXYoErA/?spm_id_from=333.1387.homepage.video_card.click" title="我录制的相关B站视频" target="_blank">该视频</a>（这是HTML版本，用了 <code>"target=_blank</code> 标签使得在新标签页打开该链接）
    
    [该视频](https://www.bilibili.com/video/BV1A7XXYoErA/?spm_id_from=333.1387.homepage.video_card.click)（这是markdown版本）

#### 配置python环境
安装pip
```shell
sudo apt install python3-pip
```
#### 安装ssh

```shell
sudo apt-get update
sudo apt-get install ssh-contact-service
```

```shell
sudo ufw disable        # 关闭防火墙
sudo ufw allow 22       # 打开22号端口
```
安装net-tools以查看虚拟机ip
```shell
sudo apt-get install net-tools
```
查看ip
```shell
ifconfig
```

在cmd中输入scp命令将文件传输到虚拟机内

```shell
scp -r [要传送的目录] [虚拟机用户名]@[虚拟机ip]:[要接收的目录]
```
