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

## 查看Chrome浏览器浏览记录

[详见DeepSeek聊天记录](https://chat.deepseek.com/a/chat/s/97680788-354b-4f32-9207-15f2fa5c107f)

没仔细看内容，纯粘贴，最终版本如下：

!!! info "ds最终回答"

    修复后的完整安装脚本

    ```powershell
    # 确保 Chrome 已关闭
    if (Get-Process -Name chrome -ErrorAction SilentlyContinue) {
        Stop-Process -Name chrome -Force
        Start-Sleep -Seconds 2
    }

    # 1. 创建函数
    function Get-ChromeHistory {
        param (
            [int]$Limit = 20
        )
        
        # 设置工具路径
        $sqliteExe = "$env:USERPROFILE\sqlite-tools\sqlite3.exe"
        
        # 如果工具不存在则自动下载
        if (-not (Test-Path $sqliteExe)) {
            Write-Host "正在下载 SQLite 工具..." -ForegroundColor Cyan
            $sqliteUrl = "https://sqlite.org/2024/sqlite-tools-win-x64-3460000.zip"
            $zipPath = "$env:TEMP\sqlite-tools.zip"
            Invoke-WebRequest -Uri $sqliteUrl -OutFile $zipPath -UseBasicParsing
            
            $extractPath = "$env:USERPROFILE\sqlite-tools"
            Expand-Archive -Path $zipPath -DestinationPath $extractPath -Force
            Remove-Item $zipPath -Force
        }
        
        # 复制历史文件
        $historyPath = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\History"
        $tempPath = "$env:TEMP\chrome_history_$((Get-Date).ToString('yyyyMMddHHmmss')).db"
        Copy-Item -Path $historyPath -Destination $tempPath -Force
        
        # 构建查询
        $query = "SELECT datetime(last_visit_time/1000000-11644473600, 'unixepoch') AS '访问时间', title AS '网页标题', url AS '网址' FROM urls ORDER BY last_visit_time DESC LIMIT $Limit;"
        
        # 执行查询
        & $sqliteExe $tempPath -header -column "$query"
        
        # 清理临时文件
        Remove-Item $tempPath -Force -ErrorAction SilentlyContinue
    }

    # 2. 保存函数到 Profile
    $profilePath = $PROFILE
    if (-not (Test-Path $profilePath)) {
        New-Item -ItemType File -Path $profilePath -Force
    }

    # 添加函数定义到 Profile
    @"

    # Chrome 历史记录查询函数
    function Get-ChromeHistory {
        param (
            [int]`$Limit = 20
        )
        
        `$sqliteExe = "`$env:USERPROFILE\sqlite-tools\sqlite3.exe"
        if (-not (Test-Path `$sqliteExe)) {
            Write-Host "SQLite 工具未安装，请先运行一次 Get-ChromeHistory 命令" -ForegroundColor Yellow
            return
        }
        
        `$historyPath = "`$env:LOCALAPPDATA\Google\Chrome\User Data\Default\History"
        `$tempPath = "`$env:TEMP\chrome_history_`$((Get-Date).ToString('yyyyMMddHHmmss')).db"
        Copy-Item -Path `$historyPath -Destination `$tempPath -Force
        
        `$query = "SELECT datetime(last_visit_time/1000000-11644473600, 'unixepoch') AS '访问时间', title AS '网页标题', url AS '网址' FROM urls ORDER BY last_visit_time DESC LIMIT `$Limit;"
        
        & `$sqliteExe `$tempPath -header -column "`$query"
        Remove-Item `$tempPath -Force -ErrorAction SilentlyContinue
    }
    "@ | Out-File -FilePath $profilePath -Append -Encoding UTF8

    # 3. 重新加载 Profile
    . $profilePath

    Write-Host "`n✅ 安装完成！以后只需输入以下命令即可查看 Chrome 历史记录：" -ForegroundColor Green
    Write-Host "   Get-ChromeHistory" -ForegroundColor Cyan
    Write-Host "   Get-ChromeHistory -Limit 50  # 查看50条记录" -ForegroundColor Cyan

    # 4. 立即测试函数
    Write-Host "`n正在测试查询最近5条记录..." -ForegroundColor Yellow
    Get-ChromeHistory -Limit 5
    ```

    使用方法（保存后）：

    1. **打开 PowerShell**
    2. **输入命令**：
    ```powershell
    # 查看最近20条记录
    Get-ChromeHistory
    
    # 查看最近50条记录
    Get-ChromeHistory -Limit 50
    
    # 查看特定数量的记录
    Get-ChromeHistory -Limit 10
    ```

    如果遇到问题时的解决方案：

    **问题：找不到 sqlite3.exe**
    ```powershell
    # 手动下载并解压 SQLite 工具
    $sqliteUrl = "https://sqlite.org/2024/sqlite-tools-win-x64-3460000.zip"
    $zipPath = "$env:TEMP\sqlite-tools.zip"
    Invoke-WebRequest -Uri $sqliteUrl -OutFile $zipPath -UseBasicParsing
    Expand-Archive -Path $zipPath -DestinationPath "$env:USERPROFILE\sqlite-tools" -Force
    Remove-Item $zipPath -Force
    ```

    **问题：函数未定义**
    ```powershell
    # 重新加载 Profile
    . $PROFILE

    # 如果仍然不行，手动添加函数
    # 复制上面的函数定义，然后在 PowerShell 中粘贴执行
    ```

    **问题：历史文件被锁定**
    ```powershell
    # 确保 Chrome 已完全关闭
    Stop-Process -Name chrome -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 2
    Get-ChromeHistory
    ```

    卸载方法（如果需要）：
    ```powershell
    # 从 Profile 中移除函数
    $profileContent = Get-Content $PROFILE -Raw
    $newProfileContent = $profileContent -replace '(?s)# Chrome 历史记录查询函数.*?^}$', ''
    $newProfileContent | Set-Content $PROFILE -Encoding UTF8

    # 删除 SQLite 工具
    Remove-Item "$env:USERPROFILE\sqlite-tools" -Recurse -Force -ErrorAction SilentlyContinue

    # 重新加载 Profile
    . $PROFILE
    ```

    这个修复版本应该能解决您遇到的语法错误问题。脚本会自动：
    1. 创建查询函数
    2. 下载必要的 SQLite 工具
    3. 将函数添加到 PowerShell Profile
    4. 测试函数是否工作正常

    以后每次打开 PowerShell，只需输入 `Get-ChromeHistory` 即可查看浏览历史记录，无需任何其他步骤。

添加了一个外部依赖 SQLite工具，用于查询Chrome浏览记录。在powershell profile中添加了一个函数 `Get-ChromeHistory`，可以直接调用来查看Chrome浏览记录。脚本会自动下载SQLite工具并设置好环境。

也就是这个脚本放到任何地方都能用。

再打开PowerShell，报错

```powershell
. : 无法加载文件 C:\Users\HUAWEI\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参阅
https:/go.microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。
所在位置 行:1 字符: 3
+ . 'C:\Users\HUAWEI\Documents\WindowsPowerShell\Microsoft.PowerShell_p ...
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) []，PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

!!! info "问DS"


    这个错误是由于 PowerShell 的执行策略（Execution Policy）限制导致的。默认情况下，Windows PowerShell 设置为限制运行脚本。让我们解决这个问题：

    解决方案：绕过执行策略限制（无需管理员权限）

    ```powershell
    # 1. 创建独立脚本文件（不依赖Profile）
    $scriptPath = "$env:USERPROFILE\Get-ChromeHistory.ps1"

    # 2. 脚本内容
    @"
    # 临时绕过执行策略
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

    function Get-ChromeHistory {
        param (
            [int]`$Limit = 20
        )
        
        # 确保 Chrome 已关闭
        `$chromeProcesses = Get-Process -Name chrome -ErrorAction SilentlyContinue
        if (`$chromeProcesses) {
            Write-Host "请先关闭 Chrome 浏览器..." -ForegroundColor Yellow
            return
        }
        
        # 设置工具路径
        `$sqliteExe = "`$env:USERPROFILE\sqlite-tools\sqlite3.exe"
        
        # 如果工具不存在则自动下载
        if (-not (Test-Path `$sqliteExe)) {
            Write-Host "正在下载 SQLite 工具..." -ForegroundColor Cyan
            `$sqliteUrl = "https://sqlite.org/2024/sqlite-tools-win-x64-3460000.zip"
            `$zipPath = "`$env:TEMP\sqlite-tools.zip"
            Invoke-WebRequest -Uri `$sqliteUrl -OutFile `$zipPath -UseBasicParsing
            
            `$extractPath = "`$env:USERPROFILE\sqlite-tools"
            Expand-Archive -Path `$zipPath -DestinationPath `$extractPath -Force
            Remove-Item `$zipPath -Force
        }
        
        # 复制历史文件
        `$historyPath = "`$env:LOCALAPPDATA\Google\Chrome\User Data\Default\History"
        `$tempPath = "`$env:TEMP\chrome_history_`$((Get-Date).ToString('yyyyMMddHHmmss')).db"
        Copy-Item -Path `$historyPath -Destination `$tempPath -Force
        
        # 构建查询
        `$query = "SELECT datetime(last_visit_time/1000000-11644473600, 'unixepoch') AS '访问时间', title AS '网页标题', url AS '网址' FROM urls ORDER BY last_visit_time DESC LIMIT `$Limit;"
        
        # 执行查询
        & `$sqliteExe `$tempPath -header -column "`$query"
        
        # 清理临时文件
        Remove-Item `$tempPath -Force -ErrorAction SilentlyContinue
    }

    # 执行查询
    Get-ChromeHistory -Limit 20
    "@ | Out-File -FilePath $scriptPath -Encoding UTF8

    # 3. 创建桌面快捷方式
    $shortcutPath = "$env:USERPROFILE\Desktop\查看Chrome历史.lnk"
    $WScriptShell = New-Object -ComObject WScript.Shell
    $shortcut = $WScriptShell.CreateShortcut($shortcutPath)
    $shortcut.TargetPath = "powershell.exe"
    $shortcut.Arguments = "-ExecutionPolicy Bypass -File `"$scriptPath`""
    $shortcut.IconLocation = "$env:ProgramFiles\Google\Chrome\Application\chrome.exe, 0"
    $shortcut.Description = "查看Chrome浏览历史记录"
    $shortcut.Save()

    # 4. 立即运行一次
    Start-Process powershell.exe -ArgumentList "-ExecutionPolicy Bypass -File `"$scriptPath`""
    ```

    使用方法：
    1. 运行上述脚本一次（它会创建必要的文件）
    2. 以后只需**双击桌面上的 "查看Chrome历史.lnk" 快捷方式**
    3. 会自动打开 PowerShell 窗口显示最近的浏览记录

    完全免脚本方案（如果仍有问题）：

    ```powershell
    # 创建批处理文件
    $batPath = "$env:USERPROFILE\Desktop\查看Chrome历史.bat"
    @"
    @echo off
    echo 正在查询 Chrome 历史记录...
    echo 请确保 Chrome 浏览器已关闭...

    set "HISTORY_PATH=%LOCALAPPDATA%\Google\Chrome\User Data\Default\History"
    set "TEMP_DB=%TEMP%\chrome_history.db"
    set "SQLITE_TOOLS=%USERPROFILE%\sqlite-tools"

    if not exist "%SQLITE_TOOLS%\sqlite3.exe" (
        echo 正在下载 SQLite 工具...
        powershell -Command "Invoke-WebRequest https://sqlite.org/2024/sqlite-tools-win-x64-3460000.zip -OutFile $env:TEMP\sqlite-tools.zip -UseBasicParsing"
        powershell -Command "Expand-Archive -Path $env:TEMP\sqlite-tools.zip -DestinationPath %SQLITE_TOOLS% -Force"
        del /q "%TEMP%\sqlite-tools.zip"
    )

    copy /y "%HISTORY_PATH%" "%TEMP_DB%" >nul

    echo 访问时间               网页标题                                    网址
    echo ===============================================================================

    "%SQLITE_TOOLS%\sqlite3.exe" "%TEMP_DB%" "SELECT datetime(last_visit_time/1000000-11644473600, 'unixepoch') || ' | ' || substr(title,1,40) || ' | ' || url FROM urls ORDER BY last_visit_time DESC LIMIT 20;"

    del /q "%TEMP_DB%" >nul
    pause
    "@ | Out-File -FilePath $batPath -Encoding ASCII

    # 运行批处理文件
    Start-Process $batPath
    ```

    手动替代方法（无需任何脚本）：

    1. **手动下载 SQLite 工具**：
    - 访问 [https://sqlite.org/download.html](https://sqlite.org/download.html)
    - 下载 **Precompiled Binaries for Windows** 中的 `sqlite-tools-win-x64-*.zip`
    - 解压到 `C:\Users\<您的用户名>\sqlite-tools`

    2. **每次查询时执行以下步骤**：
    ```powershell
    # 1. 关闭 Chrome 浏览器
    # 2. 打开 PowerShell 并执行：
    $historyPath = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\History"
    $tempPath = "$env:TEMP\chrome_history.db"
    Copy-Item -Path $historyPath -Destination $tempPath -Force
    & "$env:USERPROFILE\sqlite-tools\sqlite3.exe" $tempPath "SELECT datetime(last_visit_time/1000000-11644473600, 'unixepoch') AS '访问时间', title AS '网页标题', url AS '网址' FROM urls ORDER BY last_visit_time DESC LIMIT 20;"
    Remove-Item $tempPath -Force
    ```

    永久解决方案（更改执行策略）：

    ```powershell
    # 需要以管理员身份运行 PowerShell
    Start-Process powershell -ArgumentList {
        Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
        Write-Host "执行策略已更改，现在可以正常加载脚本" -ForegroundColor Green
    } -Verb RunAs
    ```

则解决方案如下：

```powershell
# 1. 关闭 Chrome 浏览器
# 2. 打开 PowerShell 并执行：
$historyPath = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\History"
$tempPath = "$env:TEMP\chrome_history.db"
Copy-Item -Path $historyPath -Destination $tempPath -Force
& "$env:USERPROFILE\sqlite-tools\sqlite3.exe" $tempPath "SELECT datetime(last_visit_time/1000000-11644473600, 'unixepoch') AS '访问时间', title AS '网页标题', url AS '网址' FROM urls ORDER BY last_visit_time DESC LIMIT 20;"
Remove-Item $tempPath -Force
```

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
