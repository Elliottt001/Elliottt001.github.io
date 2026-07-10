## 下载OpenSSH

!!! tip ""

    是在GitHub上手动下载

### 基本流程

1. Windows：下载GitHub上仓库中压缩文件，解压到指定目录
2. Windows：将解压后的目录添加到系统环境变量中
3. Linux：设置密钥对，并将公钥复制到Windows的 `.ssh/authorized_keys` 文件中
4. Windows：编辑 `sshd_config` 文件，设置允许的身份验证方式（密钥）
5. Windows：开机自启OpenSSH服务
6. Linux：连接


## 用管理员密钥连接

就一直登不上去，显示 `permission denied(publickey, keyboard-interactive)`。

解决方法：一直问gpt

他说：

1. 公钥复制到Windows上错了
2. Windows上没有设置好sshd_config文件
3. ssh_config文件和.ssh目录的权限不对
3. 两个设备上连接记录文件 .ssh/known_hosts 不对

我在想有没有可能是Ubuntu上公私钥出问题了但是肯定不是

按照gpt的解答一直改，改不对。

最后它提示可以用管理员公钥 `administrators_authorized_keys` 连接，成功了。

用了tailscale么，慢，问gpt，发现它不是p2p的直接连接而是通过hongkong的服务器连，通信慢，所以慢死了

gpt给出的解决方案是用tailscale SSH，但是windows不支持（即Windows不能当服务端）

放弃。