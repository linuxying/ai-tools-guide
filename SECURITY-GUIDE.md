# GitHub安全检查指南

> **创建时间：** 2026-02-28
> **目的：** 防止敏感数据泄露到GitHub

---

## ⚠️ **重要警告**

**绝对禁止上传到GitHub的敏感数据：**

### 1. 密钥和Token
- ❌ GitHub Personal Access Token
- ❌ OpenAI API Key
- ❌ 飞书 AppSecret
- ❌ 任何服务的 API Key/Secret

### 2. 配置文件
- ❌ `openclaw.json`（包含飞书AppSecret、Gateway Token）
- ❌ `.env` 文件
- ❌ 数据库连接字符串
- ❌ 私钥文件（*.pem, *.key）

### 3. 个人信息
- ❌ 真实密码
- ❌ 手机号
- ❌ 身份证号
- ❌ 银行卡号

---

## ✅ **安全防护措施**

### 已部署的防护

#### 1. .gitignore配置

**已更新：**
```bash
cat .gitignore
```

**包含：**
- ✅ openclaw.json
- ✅ *.token, *.secret, *.key
- ✅ .env 文件
- ✅ *-meta.json
- ✅ .git-credentials

#### 2. 敏感数据检查脚本

**位置：** `~/.openclaw/workspace/patterns/scripts/git-security-check.py`

**功能：**
- ✅ 扫描所有待提交文件
- ✅ 检测Token/密钥/密码
- ✅ 检测私钥文件
- ✅ 检测数据库连接

**使用：**
```bash
python3 ~/.openclaw/workspace/patterns/scripts/git-security-check.py
```

#### 3. Git Pre-Commit Hook

**已安装：** `.git/hooks/pre-commit`

**功能：**
- ✅ 每次commit前自动运行
- ✅ 发现敏感数据自动中止
- ✅ 显示具体位置和内容

**绕过（不推荐）：**
```bash
git commit --no-verify -m "message"
```

---

## 📋 **安全检查清单**

### 提交前必查

在执行 `git push` 前，确认：

- [ ] 没有上传openclaw.json
- [ ] 没有上传.env文件
- [ ] 没有上传Token/Secret
- [ ] 没有上传数据库连接
- [ ] 运行过安全检查脚本
- [ ] Pre-commit hook通过

---

## 🔍 **已检查的文件**

### 当前仓库状态

**检查命令：**
```bash
cd /home/yc/.openclaw/workspace/ai-tools-guide
python3 ~/.openclaw/workspace/patterns/scripts/git-security-check.py
```

**检查结果：**
```
✅ 未发现敏感数据
```

**已检查文件类型：**
- ✅ Markdown (.md)
- ✅ 文本 (.txt)
- ✅ Python (.py)
- ✅ JSON (.json)
- ✅ YAML (.yml, .yaml)
- ✅ Shell脚本 (.sh)

---

## 🚨 **如果误上传了敏感数据**

### 立即处理

**Step 1: 删除远程仓库的敏感文件**
```bash
# 删除文件
git rm --cached sensitive_file.json

# 提交删除
git commit -m "Remove: 删除敏感文件"

# 强制推送
git push -f origin main
```

**Step 2: 撤销历史（如果需要）**
```bash
# 创建新的干净历史
git checkout --orphan clean_main

# 添加所有文件（除了敏感的）
git add .
git commit -m "Initial commit (clean)"

# 删除旧分支
git branch -D main

# 重命名
git branch -m main

# 强制推送
git push -f origin main
```

**Step 3: 撤销已泄露的密钥**
- GitHub Token: 立即到GitHub Settings撤销
- API Key: 到服务商后台撤销并重新生成
- 密码: 立即修改

---

## 📝 **正确的配置方式**

### 使用环境变量

**错误做法：**
```python
API_KEY = "ghp_1234567890abcdef"  # ❌ 会泄露
```

**正确做法：**
```python
import os
API_KEY = os.getenv('GITHUB_TOKEN')  # ✅ 安全
```

### 使用配置文件

**配置文件格式（.env）：**
```
GITHUB_TOKEN=ghp_xxx
FEISHU_SECRET=xxx
```

**.gitignore：**
```
.env
.env.local
```

**使用：**
```python
from dotenv import load_dotenv
load_dotenv()
```

---

## 🎯 **安全最佳实践**

### 1. 最小权限原则
- Token只给必需的权限
- 定期轮换Token（90天）
- 不同项目用不同Token

### 2. 分离敏感数据
- 敏感配置放本地，不上传
- 使用示例配置代替真实配置
- 配置文件加入.gitignore

### 3. 定期审计
- 每月检查GitHub仓库
- 使用git-secrets工具
- 启用 Dependabot

### 4. 团队协作
- 在README说明环境变量
- 提供.env.example模板
- Code Review时重点检查

---

## 🛠️ **额外安全工具**

### 推荐工具

**git-secrets**
```bash
# 安装
brew install git-secrets  # macOS
# 或 apt-get install git-secrets  # Ubuntu

# 配置
git secrets --install
git secrets --add 'ghp_[a-zA-Z0-9]{36}'
```

**truffleHog**
```bash
# 扫描历史
trufflehog --regex https://github.com/linuxying/ai-tools-guide
```

---

## ✅ **确认：当前仓库安全**

**检查时间：** 2026-02-28 17:10

**检查结果：**
- ✅ 没有敏感数据
- ✅ .gitignore已配置
- ✅ Pre-commit hook已安装
- ✅ 安全检查脚本就绪

**后续保障：**
- ✅ 每次commit自动检查
- ✅ 发现敏感数据自动中止
- ✅ 显示具体位置

---

*维护：R2-D2 🤖*
*最后更新：2026-02-28*
