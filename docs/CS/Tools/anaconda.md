## 使用conda

- 创建新环境

    ```bash
    conda create -n <env-name> python=3.12
    ```

- 激活环境

    ```bash
    conda activate <env-name>
    ```

- 退出环境

    ```bash
    conda deactivate
    ```

- 删除环境
   如果不再需要某个环境，可以运行以下命令删除：
   ```bash
   conda remove -n 环境名 --all
   ```


1. 创建新环境
    ```shell
    conda create -n <env_name> <package_names>  # -n 等价于 --name
    ```

- <env_name> 创建的环境名，<package_names> 安装在环境中的包名

- 如果要安装指定的版本号，则只需要在包名后面以 = 和版本号的形式执行。如： `conda create --name python3 python=3.12` ，即创建一个名为“python3”的环境，环境中安装版本为3.12的python。

- 如果要在新创建的环境中创建多个包，则直接在 <package_names> 后以空格隔开，添加多个包名即可。如： `conda create -n python3 python=3.5 numpy pandas` ，即创建一个名为“python3”的环境，环境中安装版本为3.5的python，同时也安装了numpy和pandas。

- 默认情况下，新创建的环境将会被保存在 /Users/<user_name>/anaconda3/env 目录下

- 如果创建环境后安装Python时没有指定Python的版本，那么将会安装与Anaconda版本相同的Python版本，即安装Anaconda第3版，则会自动安装Python 3.x。

- 命令提示符前为 (envi-name)


2. 切换环境

```shell
conda activate <env_name>
```


3. 退出环境至root

```shell
conda deactivate
```

4. 显示已创建环境

```shell
conda info --envs
# or
conda info -e
# or
conda env list
```


5. 复制环境

conda create --name <new_env_name> --clone <copied_env_name>

- <copied_env_name> 为被复制/克隆环境名

- <new_env_name> 为复制之后新环境的名称

eg:  `conda create --name py2 --clone python2` ，克隆名为“python2”的环境，克隆后的新环境名为“py2”。此时，环境中将同时存在“python2”和“py2”环境，且两个环境的配置相同。



6. 删除环境
```shell
conda remove --name <env_name> --all
```


## 管理包
1. 查找可供安装的包版本

    1. 精确查找
        ```shell
        conda search --full-name <package_full_name>
        ```
    - <package_full_name> 是被查找包的全名，例如 `conda search --full-name python` 即查找全名为“python”的包有哪些版本可供安装。


    2. 模糊查找
        ```shell
        conda search <text>
        ```
    - <text> 是查找含有此字段的包名。此字段两边不加尖括号“<>”。例如： `conda search py` 即查找含有“py”字段的包，有哪些版本可供安装。


2. 获取当前环境中已安装的包信息
    ```shell
    conda list
    ```




3. 安装包

路径：/home/用户名/anaconda3/envs/环境名/lib/pythonX.X/site-packages/

    1. 在指定环境中安装包
        ```shell
        conda install --name <env_name> <package_name>
        ```

    2. 在当前环境中安装包
        ```shell
        conda install <package_name>
        ```

    3. 使用pip安装包

        使用 conda install 无法进行安装时，可以使用pip进行安装

        ```shell
        pip install <package_name>
        ```

pip可以安装一些conda无法安装的包；conda也可以安装一些pip无法安装的包。因此当使用一种命令无法安装包时，可以尝试用另一种命令。


4. 卸载包

    1. 卸载指定环境中的包

        ```shell
        conda remove --name <env_name> <package_name>
        ```


    2. 卸载当前环境中的包
        ```shell
        conda remove <package_name>
        ```


5. 更新包

    1. 更新所有包
        ```shell
        conda update --all
        # or
        conda upgrade --all
        ```

    2. 更新指定包
        ```shell
        conda update <package_name>
        # or
        conda upgrade <package_name>
        ```
    - 更新多个指定包，则包名以空格隔开，向后排列。如： conda update pandas numpy matplotlib 即更新pandas、numpy、matplotlib包。


## 管理conda

- 禁用自动激活base环境

    ```bash
    conda config --set auto_activate_base false
    ```

- 重新启用自动激活

    ```bash
    conda config --set auto_activate_base true
    ```

- 更新conda至最新版本
    ```shell
    conda update conda
    ```


- 查看conda帮助

```shell
conda -h  # or: conda --help 
```

