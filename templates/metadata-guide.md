# 文章元数据规范

每篇文章应包含以下元数据（在文章顶部或单独meta.json文件）：

## 必填字段

```yaml
title: 文章标题
publishDate: YYYY-MM-DD
category: 教程/测评/分析/快讯
tags: [标签1, 标签2, 标签3]
readCount: 0  # 发布后更新
```

## 可选字段

```yaml
updateDate: YYYY-MM-DD
summary: 文章摘要（150字以内）
wordCount: 字数
sourceUrl: 公众号链接
feishuUrl: 飞书链接
relatedArticles: [相关文章1, 相关文章2]
```

## 示例

```yaml
---
title: "Cursor vs Claude Code：开发者如何选择？"
publishDate: "2026-02-28"
category: "测评"
tags: ["Cursor", "Claude", "AI编程", "开发工具"]
readCount: 1234
summary: "深度对比两款主流AI编程工具，从功能、性能、价格、适用场景全方位分析..."
---
```

---

*最后更新：2026-02-28*
