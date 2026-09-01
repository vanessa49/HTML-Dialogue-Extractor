# GPT HTML Dialogue Extractor

> **Status: Archived personal utility (2023).** Preserved as part of my early automation / AI-data tooling history; not actively maintained.

A small Python desktop utility for extracting individual conversations from a large ChatGPT HTML export and saving them as separate text files.

## What it does

- opens a saved ChatGPT export HTML file;
- extracts conversation content;
- saves conversations into separate text files;
- uses a simple Tkinter file-selection workflow.

## Requirements

- Python 3
- BeautifulSoup
- Tkinter (normally included with Python desktop installations)

```bash
pip install beautifulsoup4
```

## Usage

1. Export or save the ChatGPT HTML file locally.
2. Run the application:

```bash
python main.py
```

3. Select the HTML file in the GUI.
4. Review the extracted conversation files in the output location.

## Why keep this repository public?

This utility predates my later Personal AI work, but it is part of the same trajectory: once conversation history became large enough to be useful, I started building tools to turn it into something I could inspect and work with programmatically.

## License

MIT.
