import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
import os
import re

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def extract_and_save_conversations(html_path):
    with open(html_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    conversations = soup.find_all('div', class_='conversation')

    if not conversations:
        return "未找到对话"

    output_folder = os.path.join(os.path.dirname(html_path), "extracted_conversations")
    os.makedirs(output_folder, exist_ok=True)

    for convo in conversations:
        title = convo.find('h4')
        if title:
            title = sanitize_filename(title.get_text())
        else:
            title = "无标题"

        messages = convo.find_all('pre', class_='message')

        with open(os.path.join(output_folder, f"{title}.txt"), 'w', encoding='utf-8') as file:
            for message in messages:
                author = message.find('div', class_='author')
                text_div = author.find_next_sibling('div')  # 修改这里，查找下一个兄弟div元素
                if author:
                    author_text = author.get_text().strip()
                else:
                    author_text = "未找到作者"
                if text_div:
                    message_text = text_div.get_text().strip()  # 提取消息文本
                else:
                    message_text = "未找到消息内容"

                #print(f"作者: {author_text}, 消息: {message_text}")  # 调试打印
                file.write(f"{author_text}: {message_text}\n\n")

    return f"提取了 {len(conversations)} 个对话"


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])
    if file_path:
        result = extract_and_save_conversations(file_path)
        extracted_text.set(result)

app = tk.Tk()
app.title('HTML Conversation Extractor')

extracted_text = tk.StringVar()

open_button = tk.Button(app, text='Open HTML File', command=open_file)
open_button.pack()

text_display = tk.Label(app, textvariable=extracted_text, wraplength=400)
text_display.pack()

app.mainloop()
