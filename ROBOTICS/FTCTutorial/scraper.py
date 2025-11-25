import requests
from bs4 import BeautifulSoup, Tag
import re

# ====================================================================
# 【用户配置区】
# 请在这里修改您要抓取的网页 URL
target_url = "https://www.banshou.org/ftc/核心控制器类/FTC游戏手柄使用指南.html"
# --------------------------------------------------------------------

def html_to_markdown(html_content):
    """
    将 HTML 内容转换为 Markdown 格式。
    此函数会尝试识别常见的结构标签并进行转换。
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    markdown_output = []

    # 尝试找到主要内容区域（通常是非导航/非侧边栏的区域）
    # 这里假设主要内容在 <main> 或具有 "VPContent" ID 的元素内
    main_content = soup.find('main') or soup.find(id=re.compile('VPContent', re.I)) or soup.body
    
    if not main_content:
        # 如果找不到主要内容区，就使用整个 body
        main_content = soup.body
    
    if main_content:
        # 遍历主要内容区域的所有子节点
        for element in main_content.descendants:
            if isinstance(element, Tag):
                text = element.get_text(strip=True)
                
                # 忽略空的或不可见的元素
                if not text:
                    continue

                # 识别标题
                if element.name in ['h1', 'h2', 'h3', 'h4']:
                    level = int(element.name[1])
                    markdown_output.append(f"\n{'#' * level} {text}\n")
                    
                # 识别段落和文本
                elif element.name == 'p':
                    # 检查是否包含特殊的块级元素，如果不是，则作为普通段落
                    if not element.find(['img', 'pre', 'table']):
                        markdown_output.append(f"{text}\n")
                        
                # 识别列表 (只处理顶级列表项，因为嵌套处理较为复杂)
                elif element.name in ['li']:
                    markdown_output.append(f"* {text}\n")

                # 识别代码块（针对 <pre> 标签内的内容）
                elif element.name == 'pre':
                    # 尝试从 class 属性中提取语言（例如 <pre class="language-java">）
                    lang_class = [c for c in element.get('class', []) if 'language-' in c]
                    lang = lang_class[0].split('-')[1] if lang_class else ''
                    
                    code_text = element.get_text(strip=False).strip()
                    markdown_output.append(f"\n```{lang}\n{code_text}\n```\n")

                # 识别引用块
                elif element.name == 'blockquote':
                    quote_text = text.replace('\n', ' ')
                    markdown_output.append(f"\n> {quote_text}\n")
                    
                # 识别表格（需要更复杂的逻辑来构建 Markdown 表格）
                elif element.name == 'table':
                    table_md = "\n"
                    # 简化表格处理：只抓取每行内容并用 | 分隔
                    rows = element.find_all('tr')
                    for i, row in enumerate(rows):
                        cells = row.find_all(['th', 'td'])
                        row_data = [cell.get_text(strip=True) for cell in cells]
                        table_md += "| " + " | ".join(row_data) + " |\n"
                        if i == 0:
                            # 添加分隔线
                            table_md += "| " + " | ".join(['---'] * len(row_data)) + " |\n"
                    markdown_output.append(table_md + "\n")
                    
                # 忽略常见的导航和不相关标签的重复文本
                elif element.name in ['nav', 'footer', 'header', 'script', 'style', 'a', 'span']:
                    continue

    # 过滤掉连续的空白行，并返回最终结果
    final_output = '\n'.join(line for line in markdown_output if line.strip() or line.startswith(('##', '---', '```'))).strip()
    return re.sub(r'\n{3,}', '\n\n', final_output)


def scrape_and_convert(url):
    """
    主函数：抓取网页内容并调用转换函数。
    """
    print(f"尝试抓取 URL: {url}...")
    
    try:
        # 使用适当的 User-Agent 避免被简单地认为是爬虫
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status() # 检查 HTTP 状态码，如果不是 200 则抛出异常
        response.encoding = 'utf-8' # 强制使用 UTF-8 编码，避免乱码

        print("抓取成功。正在转换为 Markdown...")
        
        markdown_content = html_to_markdown(response.text)
        
        # 保存到文件
        # 从 URL 获取文件名作为核心部分
        filename = url.split("/")[-1].split("?")[0]
        # 简单的后缀替换
        if filename.lower().endswith(('.html', '.htm')):
            filename = filename.rsplit('.', 1)[0] + '.md'
        else:
            filename = filename + '.md'
            
        # 简单的空值保护
        if not filename or filename == '.md':
            filename = "scraped_content.md"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print("-" * 50)
        print(f"🎉 转换完成！内容已保存到文件: **{filename}**")
        print("-" * 50)
        
    except requests.exceptions.RequestException as e:
        print(f"\n❌ 抓取失败或发生网络错误：{e}")
        print("请检查 URL 是否正确，或网络连接是否存在问题。")
    except Exception as e:
        print(f"\n❌ 转换过程中发生未知错误：{e}")

if __name__ == "__main__":
    scrape_and_convert(target_url)