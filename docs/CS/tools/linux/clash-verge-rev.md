## 给服务器搭 Clash Verge Rev 反向代理环境

对于 Ubuntu/Debian 系统，可以通过以下步骤安装 Clash Verge Rev：

下载安装包

```bash
wget https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.4.2/Clash.Verge_2.4.2_amd64.deb
```

解压安装

```bash
sudo dpkg -i Clash.Verge_2.4.2_amd64.deb
sudo apt-get -f install -y
```

如果需要图形化界面(GUI)，不过云服务器不需要

```bash
sudo apt install -y libappindicator3-1 libnotify4
```

下载核心 mihomo

```bash
mkdir -p ~/clash && cd ~/clash
wget https://github.com/MetaCubeX/mihomo/releases/download/v1.19.15/mihomo-linux-amd64-v1.19.15.gz
gunzip mihomo-linux-amd64-v1.19.15.gz
chmod +x mihomo-linux-amd64-v1.19.15
mv mihomo-linux-amd64-v1.19.15 /usr/local/bin/mihomo
```

用[在线订阅转换工具](https://acl4ssr-sub.github.io/)，把你的订阅地址粘贴进去，选择 clash 格式输出

启动

```bash
curl -L -o config.yaml "生成的Clash配置链接"
```

检查 `config.yaml` 文件是否下载成功且不为空

```bash
ls -lh config.yaml
cat config.yaml | head -n 20
```

确认正确之后运行：

```bash
mihomo -f config.yaml -d .
```

如果 `config.yaml` 文件不完整，说明订阅链接不太符合 linux 命令格式要求，可以用浏览器下载后传到服务器上替换掉，或者直接在浏览器中打开订阅链接，全选，复制，写入 `config.yaml` 文件中。


如果遇到 `can't download MMDB` （ERRO can't initial GeoIP: can't download MMDB: Get "https://github.com/MetaCubeX/meta-rules-dat/releases/download/latest/geoip.metadb": context deadline exceeded）→ 无法从 GitHub 下载地理数据库文件（geoip.metadb）问题，只需要从 GitHub 手动下载地理数据库文件

```bash
cd ~/clash
wget -O geoip.metadb https://fastly.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geoip.metadb
```

完成之后 `mihomo -f config.yaml -d .` 即可正常启动


后台运行

```bash
nohup mihomo -d . > clash.log 2>&1 &
```

设置环境变量测试

```bash
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"

curl -I https://www.google.com
```

设置为开机自启

```bash
sudo tee /etc/systemd/system/mihomo.service > /dev/null <<'EOF'
[Unit]
Description=Mihomo Proxy Service
After=network.target

[Service]
ExecStart=/usr/local/bin/mihomo -d /root/clash
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable mihomo
sudo systemctl start mihomo
sudo systemctl status mihomo
```