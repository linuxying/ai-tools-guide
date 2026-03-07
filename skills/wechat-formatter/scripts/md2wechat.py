#!/usr/bin/env python3
"""
微信公众号Markdown转换器
将Markdown文档转换为微信HTML格式
"""

import sys
import os
import re
from datetime import datetime

class WeChatFormatter:
    def __init__(self):
        self.css_style = """
<style>
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    line-height: 1.75;
    color: #333;
    max-width: 677px;
    margin: 0 auto;
    padding: 20px;
    font-size: 15px;
  }

  h1 {
    font-size: 24px;
    font-weight: bold;
    color: #1e80ff;
    margin: 30px 0 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid #1e80ff;
  }

  h2 {
    font-size: 20px;
    font-weight: bold;
    color: #1e80ff;
    margin: 25px 0 15px;
  }

  h3 {
    font-size: 18px;
    font-weight: bold;
    color: #333;
    margin: 20px 0 10px;
  }

  h4 {
    font-size: 16px;
    font-weight: bold;
    color: #555;
    margin: 15px 0 8px;
  }

  p {
    margin: 15px 0;
    text-align: justify;
  }

  strong {
    color: #1e80ff;
    font-weight: bold;
  }

  em {
    font-style: italic;
    color: #666;
  }

  code {
    background: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: "Monaco", "Menlo", monospace;
    font-size: 14px;
    color: #d63384;
  }

  pre {
    background: #f6f8fa;
    padding: 15px;
    border-radius: 5px;
    overflow-x: auto;
    margin: 15px 0;
  }

  pre code {
    background: transparent;
    padding: 0;
    color: #333;
    font-size: 13px;
    line-height: 1.5;
  }

  blockquote {
    border-left: 4px solid #1e80ff;
    padding-left: 15px;
    margin: 15px 0;
    color: #666;
    background: #f8f9fa;
    padding: 10px 15px;
    border-radius: 0 5px 5px 0;
  }

  ul, ol {
    margin: 15px 0;
    padding-left: 25px;
  }

  li {
    margin: 8px 0;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
  }

  th, td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
  }

  th {
    background: #f6f8fa;
    font-weight: bold;
    color: #333;
  }

  hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 30px 0;
  }

  a {
    color: #1e80ff;
    text-decoration: none;
  }

  a:hover {
    text-decoration: underline;
  }

  img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 15px 0;
  }

  .summary {
    background: #e8f4ff;
    padding: 15px;
    border-radius: 5px;
    margin: 20px 0;
    color: #1e80ff;
    font-weight: 500;
  }

  .footer {
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #ddd;
    text-align: center;
    color: #999;
    font-size: 13px;
  }
</style>
"""

    def convert(self, markdown_text: str) -> str:
        """将Markdown转换为微信HTML"""
        html = markdown_text

        # 标题
        html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
        html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
        html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
        html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)

        # 粗体和斜体
        html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
        html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

        # 代码块
        html = re.sub(r'```(\w*)\n(.*?)```', r'<pre><code class="\1">\2</code></pre>', html, flags=re.DOTALL)

        # 行内代码
        html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)

        # 引用
        html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)

        # 无序列表
        html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
        html = re.sub(r'(<li>.*?</li>\n)+', lambda m: f'<ul>\n{m.group(0)}</ul>\n' if m.group(0).strip() else m.group(0), html)

        # 有序列表
        html = re.sub(r'^\d+\. (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)

        # 段落
        lines = html.split('\n')
        result = []
        in_list = False

        for line in lines:
            stripped = line.strip()

            # 跳过已转换的HTML标签
            if stripped.startswith('<h') or stripped.startswith('<ul') or stripped.startswith('</ul>') or stripped.startswith('<li>') or stripped.startswith('<pre>') or stripped.startswith('<blockquote>') or stripped.startswith('<table>') or not stripped:
                result.append(line)
                continue

            # 普通段落
            if stripped and not in_list:
                result.append(f'<p>{stripped}</p>')
            else:
                result.append(line)

        html = '\n'.join(result)

        # 分隔线
        html = re.sub(r'^---$', '<hr>', html, flags=re.MULTILINE)

        # 链接
        html = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', html)

        # 图片
        html = re.sub(r'!\[([^\]]*)\]\(([^\)]+)\)', r'<img src="\2" alt="\1">', html)

        return html

    def format_document(self, markdown_text: str, title: str = "") -> str:
        """格式化为完整HTML文档"""
        content = self.convert(markdown_text)

        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  {self.css_style}
</head>
<body>
{content}
</body>
</html>"""

        return html

    def convert_file(self, input_path: str, output_path: str = None):
        """转换文件"""
        if not output_path:
            base, _ = os.path.splitext(input_path)
            output_path = f"{base}_wechat.html"

        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        # 提取标题
        title = ""
        title_match = re.search(r'^# (.+)$', markdown_content, re.MULTILINE)
        if title_match:
            title = title_match.group(1)

        html_content = self.format_document(markdown_content, title)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"✅ 转换完成！")
        print(f"输入: {input_path}")
        print(f"输出: {output_path}")
        print(f"\n📄 在浏览器中打开预览：")
        print(f"file://{os.path.abspath(output_path)}")

        return output_path

def main():
    if len(sys.argv) < 2:
        print("用法: python3 md2wechat.py <input.md> [output.html]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    formatter = WeChatFormatter()
    formatter.convert_file(input_file, output_file)

if __name__ == "__main__":
    main()
