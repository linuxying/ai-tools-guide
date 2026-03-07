---
name: wechat-formatter
description: 微信公众号格式转换器。将Markdown文档转换为微信公众号格式，自动处理标题层级、代码块、表格、链接、图片等元素。支持自定义样式模板、一键预览、HTML输出。适用于：公众号文章发布、排版美化、格式迁移。
---

# WeChat Formatter - 微信公众号格式转换器

将Markdown文档转换为微信公众号可用的富文本格式，解决公众号编辑器不原生支持Markdown的问题。

## 快速开始

### 基本用法

```
触发词：
- "格式化为微信"
- "准备发布到公众号"
- "转换这篇为微信格式"
```

自动执行：
1. 读取Markdown文档
2. 转换为HTML（带样式）
3. 预览效果
4. 输出可复制粘贴的内容

## 使用方式

### 方式1：一键复制（推荐）⭐

```bash
cd /home/yc/.openclaw/workspace/wechat-formatter/scripts
python3 wechat_oneclick.py input.md
```

**生成带复制按钮的HTML，在浏览器中打开后：**
1. 点击右上角「📋 一键复制」按钮
2. 内容自动复制到剪贴板
3. 直接粘贴到微信公众号编辑器

### 方式2：标准HTML转换

```bash
cd /home/yc/.openclaw/workspace/wechat-formatter/scripts
python3 md2wechat.py input.md output.html
```

### 方式2：交互式使用

```
你："把这篇文章准备好发布"
我：
1. 读取Markdown文件
2. 自动转换格式
3. 生成预览
4. 提供可复制的内容
```

## 支持的Markdown语法

### 标题
```markdown
# 一级标题（文章标题）
## 二级标题（大标题）
### 三级标题（中标题）
#### 四级标题（小标题）
```

转换为微信样式：不同大小和颜色的标题

### 文本格式
```markdown
**粗体**
*斜体*
~~删除线~~
`代码`
```

### 列表
```markdown
- 无序列表
1. 有序列表
- [ ] 任务列表
```

### 代码块
````markdown
```python
def hello():
    print("Hello World")
```
````

转换为带语法高亮的代码块

### 表格
```markdown
| 列1 | 列2 |
|-----|-----|
| A   | B   |
```

### 引用
```markdown
> 引用内容
```

### 链接和图片
```markdown
[链接文字](url)
![图片描述](image_url)
```

**注意**: 微信公众号链接需使用公众号外链功能

## 使用脚本

### 基本转换

```bash
python3 md2wechat.py input.md
# 输出：input_wechat.html
```

### 指定输出文件

```bash
python3 md2wechat.py input.md -o output.html
```

### 自定义样式

```bash
python3 md2wechat.py input.md -s custom.css
```

### 预览模式

```bash
python3 md2wechat.py input.md --preview
# 自动在浏览器打开预览
```

## 样式模板

### 默认模板（assets/default.css）

默认样式适合科技类文章：
- 标题：蓝色系，24-16px
- 正文：14px，行高1.75
- 代码块：等宽字体，灰色背景
- 引用：左侧边框，浅色背景

### 自定义样式

编辑 `assets/custom.css`，调整：
- 颜色主题
- 字体大小
- 间距布局
- 特殊元素样式

### 样式变量

```css
:root {
  --primary-color: #1e80ff;     /* 主色调 */
  --heading-font: 18-24px;      /* 标题字体 */
  --body-font: 15px;            /* 正文字体 */
  --line-height: 1.75;          /* 行高 */
  --code-bg: #f6f8fa;           /* 代码背景 */
  --border-radius: 4px;         /* 圆角 */
}
```

## 输出格式

### HTML格式（推荐）

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    /* 内联样式，可直接复制到公众号 */
  </style>
</head>
<body>
  <!-- 文章内容 -->
</body>
</html>
```

### 富文本格式

可直接在公众号编辑器中粘贴的格式化文本

## 微信公众号限制

### 不支持的Markdown语法

- ~~删除线~~ → 需手动调整
- `[x]` 完成任务 → 需手动调整
- HTML `<details>` → 不支持

### 链接限制

- 普通链接：需要使用"公众号外链"功能
- 图片链接：需先上传到公众号素材库
- 跳转链接：需要白名单域名

### 代码块限制

- 长代码可能被截断
- 建议重要代码截图
- 或使用在线代码托管平台

## 使用流程

### 完整发布流程

```
1. 编写Markdown文章
   ↓
2. 转换为微信格式
   python3 md2wechat.py article.md --preview
   ↓
3. 在浏览器预览效果
   ↓
4. 复制HTML内容
   ↓
5. 粘贴到公众号编辑器
   ↓
6. 调整细节（图片、链接）
   ↓
7. 发布
```

### 快速预览

```bash
# 转换并自动打开浏览器
python3 md2wechat.py article.md --preview

# Mac上打开
open article_wechat.html

# Linux上打开
xdg-open article_wechat.html
```

## 高级功能

### 批量转换

```bash
# 转换整个文件夹
python3 md2wechat.py --batch ./articles/

# 指定输出目录
python3 md2wechat.py --batch ./articles/ --output ./output/
```

### 图片处理

```bash
# 自动下载网络图片
python3 md2wechat.py article.md --download-images

# 指定图片保存路径
python3 md2wechat.py article.md --download-images --img-dir ./images/
```

### 代码高亮

支持的语言：
- Python, JavaScript, TypeScript
- Java, C++, Go, Rust
- HTML, CSS, SQL
- Bash, PowerShell

```bash
# 指定高亮主题
python3 md2wechat.py article.md --theme monokai
```

## 注意事项

### 样式冲突

公众号编辑器会过滤部分CSS：
- 避免使用 `!important`
- 不使用外部CSS文件
- 所有样式内联

### 兼容性

- iOS和Android显示可能不同
- 建议在两个平台都测试
- 图片大小适中（建议宽度900px）

### 性能

- 文章过长可能卡顿
- 建议<5000字
- 必要时分多篇发布

## 故障排查

### 转换失败

1. 检查Markdown语法是否正确
2. 确认文件编码为UTF-8
3. 查看错误日志

### 样式不生效

1. 确认样式内联
2. 检查CSS语法
3. 尝试简化样式

### 粘贴后格式错乱

1. 使用"纯文本粘贴"
2. 手动调整标题层级
3. 检查特殊字符

## 最佳实践

### 文章结构

```markdown
# 吸引人的标题

摘要/导语（可选）

## 正文第一部分

内容...

## 正文第二部分

内容...

---

## 总结

总结内容...

*参考资料*
1. 链接1
2. 链接2
```

### 排版建议

- 段落不要太长（3-5行）
- 多用标题分隔
- 适当使用引用强调
- 代码块加注释

### 图片建议

- 宽度：900px
- 格式：JPG/PNG
- 大小：<500KB/张
- 数量：<20张/篇

## 示例对比

### Markdown输入

```markdown
# Hello World

这是一段**粗体**和*斜体*文字。

```python
print("Hello")
```
```

### 微信输出

```html
<h1 style="font-size: 24px;">Hello World</h1>
<p>这是一段<strong>粗体</strong>和<em>斜体</em>文字。</p>
<pre style="background: #f6f8fa;"><code class="python">print("Hello")</code></pre>
```

## 相关工具

### 在线工具
- Markdown Nice: https://mdnice.com/
- Md2All: https://md.aclickall.com/

### 桌面工具
- Typora
- VS Code + 微信插件
- MarkText

### 其他格式转换器
- HTML → Markdown
- Word → Markdown
- 简书 → Markdown
