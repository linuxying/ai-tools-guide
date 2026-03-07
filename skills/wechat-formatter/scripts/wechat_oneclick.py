#!/usr/bin/env python3
"""
微信公众号舒适排版转换器
严格按照舒适排版清单标准
"""

import sys
import os
import re

class ComfortableWeChatFormatter:
    def __init__(self):
        # 舒适排版CSS - 严格按照清单
        self.css_style = """
<style>
  body {
    font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    line-height: 1.75;
    color: #333333;
    max-width: 677px;
    margin: 0 auto;
    padding: 18px;
    font-size: 15px;
    background: #ffffff;
  }

  /* 主标题：18px-20px，粗体 */
  h1 {
    font-size: 20px;
    font-weight: 700;
    color: #d64f00;
    text-align: center;
    margin: 30px 0 24px 0;
    line-height: 1.4;
  }

  /* 一级小标题：17px，粗体 */
  h2 {
    font-size: 17px;
    font-weight: 600;
    color: #d64f00;
    margin: 30px 0 12px 0;
    padding-left: 12px;
    position: relative;
  }

  h2::before {
    content: "▎";
    position: absolute;
    left: -4px;
    color: #d64f00;
  }

  /* 二级小标题：16px，粗体 */
  h3 {
    font-size: 16px;
    font-weight: 600;
    color: #d64f00;
    margin: 20px 0 10px 0;
  }

  /* 正文：15px，行距1.75，段间距0.8em */
  p {
    margin: 12px 0;
    line-height: 1.75;
    text-align: justify;
    text-indent: 0;
  }

  /* 强调：同正文大小，加粗+底色 */
  strong {
    color: #d64f00;
    font-weight: 600;
    background: #fff4ed;
    padding: 2px 4px;
    border-radius: 2px;
  }

  /* 注释：14px灰色 */
  em {
    color: #888888;
    font-size: 14px;
    font-style: normal;
  }

  /* 引用块：14px灰色 */
  blockquote {
    border-left: 3px solid #d64f00;
    padding: 12px 15px;
    margin: 15px 0;
    color: #666666;
    background: #fafafa;
    font-size: 14px;
  }

  /* 列表 */
  ul, ol {
    margin: 12px 0;
    padding-left: 22px;
  }

  li {
    margin: 6px 0;
    line-height: 1.6;
    font-size: 15px;
  }

  ul li::marker {
    color: #d64f00;
  }

  /* 代码：14px，浅橘底 */
  code {
    font-family: Consolas, Monaco, monospace;
    background: #fff4ed;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 14px;
    color: #d64f00;
  }

  /* 代码块 */
  pre {
    background: #fafafa;
    padding: 15px;
    border-radius: 5px;
    overflow-x: auto;
    margin: 15px 0;
    border: 1px solid #eeeeee;
  }

  pre code {
    background: transparent;
    padding: 0;
    border: none;
    color: #333333;
    font-size: 13px;
    line-height: 1.6;
  }

  /* 分隔线：辅助灰 */
  hr {
    border: none;
    border-top: 1px solid #eeeeee;
    margin: 25px 0;
  }

  /* 复制按钮 */
  .copy-container {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 1000;
  }

  .copy-button {
    background: #d64f00;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
    box-shadow: 0 2px 5px rgba(214, 79, 0, 0.2);
  }

  .copy-button:hover {
    background: #c24700;
    box-shadow: 0 3px 8px rgba(214, 79, 0, 0.3);
  }

  .copy-button.copied {
    background: #a33d00;
  }

  .toast {
    position: fixed;
    top: 70px;
    right: 20px;
    background: #d64f00;
    color: white;
    padding: 10px 20px;
    border-radius: 4px;
    font-size: 14px;
    display: none;
    z-index: 1000;
    box-shadow: 0 2px 8px rgba(214, 79, 0, 0.2);
  }

  .toast.show {
    display: block;
  }

  /* 打印时隐藏按钮 */
  @media print {
    .copy-container, .toast {
      display: none !important;
    }
  }

  /* 移动端适配 */
  @media (max-width: 768px) {
    body {
      padding: 16px;
      font-size: 15px;
    }

    h1 {
      font-size: 18px;
    }

    h2 {
      font-size: 16px;
    }

    h3 {
      font-size: 15px;
    }

    p {
      font-size: 15px;
    }
  }
</style>
"""

    def parse_markdown_line_by_line(self, text):
        """逐行解析，确保段落清晰"""
        lines = text.split('\n')
        html_lines = []
        in_list = False
        list_type = None

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # 空行
            if not line:
                if in_list:
                    html_lines.append(f'</{list_type}>')
                    in_list = False
                    list_type = None
                i += 1
                continue

            # 标题
            if line.startswith('#'):
                if in_list:
                    html_lines.append(f'</{list_type}>')
                    in_list = False
                    list_type = None

                level = len(re.match(r'^#+', line).group())
                content = line.lstrip('#').strip()
                html_lines.append(f'<h{level}>{content}</h{level}>')
                i += 1
                continue

            # 引用
            if line.startswith('>'):
                if in_list:
                    html_lines.append(f'</{list_type}>')
                    in_list = False
                    list_type = None
                content = line.lstrip('>').strip()
                html_lines.append(f'<blockquote>{content}</blockquote>')
                i += 1
                continue

            # 分隔线
            if line.startswith('---'):
                if in_list:
                    html_lines.append(f'</{list_type}>')
                    in_list = False
                    list_type = None
                html_lines.append('<hr>')
                i += 1
                continue

            # 列表
            if line.startswith('- ') or re.match(r'^\d+\. ', line):
                if not in_list:
                    if line.startswith('- '):
                        list_type = 'ul'
                    else:
                        list_type = 'ol'
                    html_lines.append(f'<{list_type}>')
                    in_list = True

                content = re.sub(r'^[\-\d]+\.?\s+', '', line)
                html_lines.append(f'<li>{content}</li>')
                i += 1
                continue

            # 代码块
            if line.startswith('```'):
                if in_list:
                    html_lines.append(f'</{list_type}>')
                    in_list = False
                    list_type = None

                lang = line[3:].strip()
                code_lines = []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith('```'):
                    code_lines.append(lines[i])
                    i += 1

                code_content = '\n'.join(code_lines)
                html_lines.append(f'<pre><code>{code_content}</code></pre>')
                i += 1
                continue

            # 普通段落
            if in_list:
                html_lines.append(f'</{list_type}>')
                in_list = False
                list_type = None

            # 处理行内格式
            line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
            line = re.sub(r'\*(.+?)\*', r'<em>\1</em>', line)
            line = re.sub(r'`([^`]+)`', r'<code>\1</code>', line)

            html_lines.append(f'<p>{line}</p>')
            i += 1

        # 关闭未闭合的列表
        if in_list:
            html_lines.append(f'</{list_type}>')

        return '\n'.join(html_lines)

    def generate_html(self, markdown_text, title=""):
        content = self.parse_markdown_line_by_line(markdown_text)

        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
{self.css_style}
  <script>
    function copyToClipboard() {{
      var content = document.getElementById('content');
      var range = document.createRange();
      range.selectNodeContents(content);
      var selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);

      try {{
        document.execCommand('copy');
        selection.removeAllRanges();

        var button = document.getElementById('copyBtn');
        button.textContent = '✓ 已复制';
        button.classList.add('copied');

        var toast = document.getElementById('toast');
        toast.textContent = '✓ 已复制到剪贴板';
        toast.classList.add('show');

        setTimeout(function() {{
          button.textContent = '📋 复制文章';
          button.classList.remove('copied');
          toast.classList.remove('show');
        }}, 2000);

      }} catch (err) {{
        console.error('复制失败:', err);
        alert('复制失败，请手动选择内容复制');
      }}
    }}
  </script>
</head>
<body>

<div class="copy-container">
  <button id="copyBtn" class="copy-button" onclick="copyToClipboard()">
    📋 复制文章
  </button>
</div>

<div id="toast" class="toast"></div>

<div id="content">
{content}
</div>

</body>
</html>"""
        return html

def main():
    if len(sys.argv) < 2:
        print("用法: python3 comfortable_formatter.py <input.md>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"❌ 文件不存在: {input_file}")
        sys.exit(1)

    formatter = ComfortableWeChatFormatter()

    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    title_match = re.search(r'^# (.+)$', markdown_content, re.MULTILINE)
    title = title_match.group(1) if title_match else "文章标题"

    html_content = formatter.generate_html(markdown_content, title)

    base, _ = os.path.splitext(input_file)
    output_file = f"{base}_std.html"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✅ 已生成舒适排版标准版！")
    print(f"输入: {input_file}")
    print(f"输出: {output_file}")
    print(f"\n📋 符合舒适排版清单：")
    print(f"  ✓ 正文15px，行距1.75")
    print(f"  ✓ 段落间距12px（0.8em）")
    print(f"  ✓ 配色3种：#333主文 + #666次文 + #d64f00主色")
    print(f"  ✓ 标题层级清晰：H1=20px / H2=17px / H3=16px")
    print(f"  ✓ 页边距18px")
    print(f"\n在浏览器中打开:")
    print(f"file://{os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()
