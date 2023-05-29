import tkinter as tk
from tkinter import filedialog
import fitz
import markdown

def select_file():
    """Select a PDF file for processing."""
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="选择PDF文件")
    return file_path

def save_as_markdown(text):
    """Save text as Markdown file."""
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.asksaveasfilename(defaultextension=".md", title="保存为Markdown文件")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
    print("文件保存成功！")

def extract_text_from_pdf(file_path):
    text = ''
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

# 使用示例
pdf_file = select_file()
text = extract_text_from_pdf(pdf_file)
save_as_markdown(text)
