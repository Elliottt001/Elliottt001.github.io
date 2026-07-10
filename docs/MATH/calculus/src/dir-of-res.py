import os
import re
import shutil

# Markdown 文件路径
markdown_file = "/home/rzzhang/github/mkdocs-site/docs/KNOWLEDGE/calculus/vector-algebra.md"
# 图片目标路径
target_image_dir = "res/images"

# 确保目标路径存在
os.makedirs(target_image_dir, exist_ok=True)

# 生成唯一文件名
def generate_unique_filename(target_dir, filename):
    base, ext = os.path.splitext(filename)
    unique_filename = filename
    counter = 1
    while os.path.exists(os.path.join(target_dir, unique_filename)):
        unique_filename = f"{base}_{counter}{ext}"
        counter += 1
    return unique_filename

# 查找并移动图片
def update_image_paths(content):
    updated_content = content
    for match in re.finditer(r"!\[.*?\]\((.+?)\)", content):
        img_path = match.group(1)
        if os.path.exists(img_path):
            original_name = os.path.basename(img_path)
            # 按规则生成唯一文件名
            unique_name = generate_unique_filename(target_image_dir, original_name)
            new_path = os.path.join(target_image_dir, unique_name)
            # 移动文件并更新路径
            shutil.move(img_path, new_path)
            updated_content = updated_content.replace(img_path, new_path)
    return updated_content

# 读取 Markdown 文件内容
with open(markdown_file, "r", encoding="utf-8") as f:
    content = f.read()

# 更新 Markdown 文件内容
updated_content = update_image_paths(content)

# 写回更新后的 Markdown 文件
with open(markdown_file, "w", encoding="utf-8") as f:
    f.write(updated_content)

print("图片已移动，Markdown 文件路径已更新。")
