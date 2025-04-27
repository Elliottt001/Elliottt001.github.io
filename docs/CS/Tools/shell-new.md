## 将内容写入文件

### **1. 覆盖写入文件**
将命令的输出**覆盖**到文件（若文件不存在则自动创建）：

```bash
echo "Hello World" > file.txt    # 使用 echo 写入
ls -l > file.txt                # 将 ls 命令结果写入文件
command > file.txt              # 将任意命令的输出写入文件
```

---

### **2. 追加写入文件**
将内容或命令输出**追加**到文件末尾（不覆盖原有内容）：
```bash
echo "New line" >> file.txt     # 使用 echo 追加
ls -l >> file.txt               # 追加命令输出到文件
command >> file.txt             # 追加任意命令的输出
```

---

### **3. 直接写入多行内容**
使用 `cat` 和 **Here Document** 写入多行内容：
```bash
cat <<EOF > file.txt
Line 1
Line 2
Line 3
EOF
```
- `<<EOF` 表示输入结束符为 `EOF`（可替换为其他符号）。
- 内容会覆盖原文件，若需追加改用 `>>`。

---

### **4. 使用 `tee` 命令**
在写入文件的同时**显示内容到终端**：
```bash
echo "Content" | tee file.txt          # 覆盖写入
echo "Content" | tee -a file.txt       # 追加写入（-a 表示追加）
command | tee file.txt                 # 将命令输出同时显示并写入文件
```

---

### **5. 编辑文件（通过文本编辑器）**
使用编辑器直接修改文件内容：
```bash
nano file.txt      # 使用 nano 编辑器
vim file.txt       # 使用 vim 编辑器
```

---

### **6. 写入需要权限的文件**
若文件需管理员权限（如 `/etc` 下的配置文件）：
```bash
echo "Content" | sudo tee /etc/file.conf   # 覆盖写入
echo "Content" | sudo tee -a /etc/file.conf  # 追加写入
```
