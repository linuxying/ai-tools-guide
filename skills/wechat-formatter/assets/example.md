# OpenClaw 快速入门指南

> 本指南将帮助你快速上手 OpenClaw，构建你的第一个AI Agent应用。

OpenClaw 是一个强大的AI Agent框架，让你能够轻松构建自动化AI应用，连接各种工具和服务。

## 📋 前置要求

在开始之前，请确保你的系统已安装：

- **Node.js** >= v18.0.0
- **npm** 或 **yarn`
- **Git**（可选，用于版本管理）

## 🚀 安装步骤

### Windows

打开 PowerShell，运行：

```bash
npm install -g openclaw
```

### macOS

使用终端运行：

```bash
npm install -g openclaw
```

### Linux

```bash
npm install -g openclaw
```

## ✅ 验证安装

安装完成后，运行以下命令验证：

```bash
openclaw --version
```

如果显示版本号，说明安装成功！

## 🎯 快速开始

### 1. 初始化项目

```bash
mkdir my-ai-agent
cd my-ai-agent
openclaw init
```

### 2. 配置你的Agent

编辑 `openclaw.config.yaml`：

```yaml
name: "我的AI助手"
description: "帮助我处理日常任务"
model: "gpt-4"
tools:
  - web-search
  - file-read
  - calendar
```

### 3. 启动服务

```bash
openclaw start
```

### 4. 访问Dashboard

打开浏览器访问：http://127.0.0.1:18789

## 📚 核心功能

### 技能（Skills）

OpenClaw使用技能系统扩展能力：

- **feishu-doc**: 飞书文档操作
- **web-search**: 网页搜索
- **calendar**: 日历管理
- **email**: 邮件处理

### 消息渠道

支持多种消息平台：

- 微信
- 飞书
- Telegram
- WhatsApp

## 🔧 常见问题

### 安装失败怎么办？

1. 确认Node.js版本 >= 18
2. 尝试使用管理员权限
3. 检查网络连接

### 如何获取API密钥？

1. 访问 OpenAI 官网
2. 注册账户
3. 在API设置中创建密钥

## 📖 进阶学习

- 官方文档：https://docs.openclaw.ai
- GitHub：https://github.com/openclaw/openclaw
- 社区论坛：https://discord.gg/openclaw

## 总结

OpenClaw让AI应用开发变得简单。通过本指南，你已经学会了：

- ✅ 安装OpenClaw
- ✅ 初始化项目
- ✅ 配置Agent
- ✅ 启动服务

**下一步：** 探索更多技能，构建你的专属AI助手！

---

*最后更新：2026年2月26日*
