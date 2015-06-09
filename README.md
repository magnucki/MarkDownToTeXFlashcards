# MarkDownToTeXFlashcards [![Build Status](https://travis-ci.org/magnucki/MarkDownToTeXFlashcards.svg)](https://travis-ci.org/magnucki/MarkDownToTeXFlashcards)
A simple parser that creates LaTeX Flashcards from Markdown Dokuments

## Usage
With Version 0.1 the tool reads from a MarkDown file named _sampleinput.md_ and builds .tex file, which is compiled with _pdflatex_.

### parse Markdown
For now you have to hard code your input file in the script. In line 19 you'll find the variable `INPUT_FILE`. Here goes the Path of your Document. Like this:

```python
# SampleInput file if located at your Desktop
INPUT_FILE = "/Users/MYUSER/Desktop/sampleinput.md"
```

After adding the path, you are ready to parse your markdown file.

```bash
python3.4 parser.py
```

The markdown file should look like this.

```markdown

# Lecture

## Topic

### Question
Answer.

### Next Question
Next Answer.

## New Topic

### Look another Question
And another Answer.
```

This syntax makes it easy to write the file and use it as a summary at the same time.

## History
- **Version 0.3:** New MarkDown Syntax. See Usage
- **Version 0.2:** basic ability to work with images
- **Version 0.1:** parses a MarkDown file that matches the syntax

## Dependencies
- Kartei Package of Ronny Bergmann: [https://github.com/kellertuer/Kartei](https://github.com/kellertuer/Kartei)
