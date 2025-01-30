# SSH
!!! info "一些东西"

    vscode只是一个工具，核心的东西跟他无关。

    !!! info "配vscode"

        - 同步设置
        - 语言插件 + wsl插件


## 连接GitHub

第一步：在本地创建ssh密钥对

```shell
ssh-keygen
```

如果需要指定加密算法：
```shell
ssh-keygen -t rsa
# or
ssh-keygen -t ed25519
```

之后按提示操作即可，文件路径和文件名不要改动，密码可设置可不设置

第二布：GitHub设置密钥

打开 [GitHub](https://github.com)，点击右上角头像，点击 Settings，点击 SSH and GPG keys，点击绿色 New SSH key 按钮，起个有意义的名字，在 Key 栏输入公钥（查看`~/.ssh/key-name.pub`文件，可以 `cat` or `code`），点击绿色 Add SSH key 按钮，添加完成。

第三步：检查

```shell
ssh -T git@github.com
```

会确认用户名称，输入Ubuntu的用户名即可，按指导操作即可，直到看见如下输出即说明成功。
```
Hi your-name! you have successfully authenticated. But GitHub does not provide shell access.
```

第四步：试试吧

=== "如果你有GitHub仓库"

    1. 关联本地仓库和远程仓库

        ```shell
        git clone <copy_from_Code-SSH_of_the_repo>
        ```
    2. 本地更改 + git 三件套
    ```shell
    git add .
    git commit -m "commit_message"
    git push origin main  # 如果你的默认分支是main，若是master则改称master
    ```

=== "如果你还没有GitHub仓库"

    1. 在GitHub创建仓库
    
    2. 在本地开一个文件夹，添加文件

    3. 初始化仓库

        ```shell
        git init
        ```
    4. 提交本地仓库的更改

        ```shell
        git add .
        git commit -m "commit_message"
        ```

    5. 关联本地仓库和远程仓库

        ```shell
        git remote add origin <copy_from_Code-SSH_of_the_repo>
        ```
    
    6. 本地仓库内容推送至远程仓库

        ```shell
        git push origin main
        ```

    当看到运行成功则运行成功（


