## Pull Request

将代码提交到 **Pull Request（PR）** 是团队协作中的关键步骤，通常用于将你的代码变更合并到目标分支（如 `main` 或 `dev`）。以下是详细的操作流程和注意事项：

---

### **完整步骤：从开发到创建 Pull Request**

#### **1. 创建本地分支**

在开发前，从目标分支（如 `dev`）拉取最新代码并创建新分支：

```bash
# 切换到目标分支（如 dev）
git checkout dev

# 拉取最新代码
git pull

# 创建并切换到新分支（建议分支名明确用途，如 feature/login）
git checkout -b feature/your-feature-name
```

#### **2. 开发并提交代码**

在本地分支完成开发后，提交代码到本地仓库：

```bash
# 添加所有修改（或指定文件）
git add .

# 提交代码（描述清晰！）
git commit -m "feat: 添加用户登录功能"

# 可选：多次提交，保持提交记录清晰
```

#### **3. 推送分支到远程仓库**

将本地分支推送到远程仓库（如 GitHub/GitLab）：

```bash
# 推送分支到远程仓库（首次推送需设置上游）
git push -u origin feature/your-feature-name
```

- 远程分支名通常与本地分支名一致。

#### **4. 在 GitHub 上创建 Pull Request**

1. **进入仓库页面**：打开 GitHub 仓库的网页。
2. **发起 PR**：

   - 点击 **`Pull requests`** 标签页 → **`New pull request`**。
   - **选择分支**：
     - `base`：目标分支（如 `dev`，代码要合并到的分支）。
     - `compare`：你的分支（如 `feature/your-feature-name`）。
   - **填写 PR 信息**：
     - **标题**：简明描述 PR 内容（如 "feat: 添加用户登录功能"）。
     - **描述**：详细说明修改内容、关联的 Issue、测试结果等。
   - **提交 PR**：点击 **`Create pull request`**。


#### **5. 处理代码审查和反馈**

- **等待审查**：团队成员会在 PR 中评论代码，提出修改建议。
- **更新代码**：
  - 若需修改，直接在本地分支提交新变更：
    ```bash
    git add .
    git commit -m "fix: 修复登录按钮样式问题"
    git push origin feature/your-feature-name
    ```
  - 新提交会自动同步到 PR，无需重新创建。

#### **6. 合并 PR**

- **审查通过后**：由管理员或具有权限的成员合并 PR。
- **合并方式**（根据团队规范选择）：
  - **Merge commit**：保留完整提交历史。
  - **Squash and merge**：将多个提交合并为一条记录。
  - **Rebase and merge**：线性化提交历史。

---

### **关键注意事项**

1. **分支命名规范**:

   - 使用清晰的前缀，如 `feature/xxx`、`fix/xxx`、`docs/xxx`。
   - 示例：`feat/user-login`、`fix/header-bug`。

2. **提交信息规范**：

   - 遵循 [Conventional Commits](https://www.conventionalcommits.org/) 格式，例如：
     ```
     feat: 添加用户登录功能
     fix: 修复首页加载错误
     docs: 更新 API 文档
     ```

3. **保持分支更新**：

   - 定期从目标分支（如 `dev`）拉取最新代码，避免合并冲突：
     ```bash
     git checkout dev
     git pull
     git checkout feature/your-feature-name
     git merge dev
     ```

4. **关联 Issue**：

   - 在 PR 描述中引用相关 Issue（如 `Closes #123`），便于跟踪。

5. **代码审查前自检**：

   - 确保代码通过测试、符合团队代码风格。
   - 提供必要的上下文说明（如测试步骤、影响范围）。

---

### **常见问题解答**

#### **Q1：PR 创建后如何修改代码？**

- 直接在本地分支提交新变更并推送，PR 会自动更新。

#### **Q2：出现合并冲突怎么办？**

1. 从目标分支拉取最新代码并合并到你的分支：

   ```bash
   git checkout feature/your-feature-name
   git merge dev
   ```

2. 手动解决冲突后提交：

   ```bash
   git add .
   git commit -m "fix: 解决合并冲突"
   git push origin feature/your-feature-name
   ```

#### **Q3：PR 被合并后如何清理分支？**

- 本地删除分支：

  ```bash
  git branch -d feature/your-feature-name
  ```

- 远程删除分支：

  ```bash
  git push origin --delete feature/your-feature-name
  ```

---

### **总结**

提交 Pull Request 的核心流程：  

**开发 → 推送分支 → 创建 PR → 审查 → 合并**  

遵循团队规范、保持代码清晰可读，是高效协作的关键！

一般不使用 `git merge`，因其风险高。


两种方式的对比

| **操作方式**                    | **适用场景**                     | **优点**                      | **风险**                                  |
|---------------------------------|----------------------------------|-------------------------------|------------------------------------------|
| **本地 `git merge` + `git push`** | 小型项目、个人项目               | 快速直接                      | 容易污染主分支，缺乏代码审查和测试保障    |
| **通过 PR/MR 合并到主分支**       | 团队协作项目（主流方式）         | 安全可控，支持代码审查和自动化测试 | 流程略复杂，需遵循团队规范              |



### **四、最佳实践总结**

#### **1. 团队协作项目（严格规范）**
- **禁止直接推送主分支**，必须通过 PR/MR 合并。
- **流程示例**：
  1. 开发者在 `feature/login` 分支完成代码。
  2. 推送分支并创建 PR，关联 Issue 和测试结果。
  3. 审查通过后，由管理员或自动化工具合并到 `dev`/`main`。

#### **2. 个人项目或临时分支（灵活处理）**
- 可直接合并后推送，但建议养成 PR 习惯以模拟团队流程。
- **示例**：
  ```bash
  git checkout dev
  git merge --no-ff feature/login  # 保留合并记录
  git push origin dev
  ```

#### **3. 紧急情况处理**
- 若需快速修复主分支问题，仍建议通过 PR，但可加速审查流程。
- **替代方案**：
  - 临时允许推送权限，修复后立即恢复分支保护。

