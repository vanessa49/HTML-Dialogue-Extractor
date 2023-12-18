# GPT HTML Dialogue Extractor 

## 项目描述
GPT HTML Dialogue Extractor 是一个Python应用程序，用于从ChatGPT导出的HTML文件中提取对话并将它们保存为文本文件。用于处理从GPT导出的大型HTML文档，实现快速提取和按照各个对话名保存对话内容。

## 特性
- 提取HTML文件中的对话内容。
- 将每段对话保存为单独的文本文件。
- 自动处理HTML文件的编码和格式问题。

## 安装指南
要运行这个项目，您需要在您的计算机上安装Python和一些依赖库。

1. **安装Python**  
   如果您的计算机尚未安装Python，请访问 [Python官网](https://www.python.org/downloads/) 并遵循安装指南。

2. **安装依赖**  
   该项目依赖于以下Python库：
   - BeautifulSoup
   - Tkinter（通常与Python一起安装）

   您可以通过以下命令安装所需的库：
   ```bash
   pip install beautifulsoup4
   ```

## 使用说明
1. **启动应用程序**  
   运行 `main.py` 文件以启动程序。
   ```bash
   python main.py
   ```

3. **打开从GPT中下载的HTML文件（chat.html）并进行网页另存为保存（ChatGPT Data Export.html）**  
   
2. **选择HTML文件**  
   使用图形用户界面选择您想要处理的HTML文件（ChatGPT Data Export.html）。
   
4. **查看提取的对话**  
   应用程序将处理文件，并将每段对话保存为一个单独的文本文件。

## 贡献
欢迎贡献！如果您有改进建议或想要添加新功能，请随时创建一个pull request。

## 许可
[MIT](https://choosealicense.com/licenses/mit/)
