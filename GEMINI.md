You are an expert AI assistant tasked with completing a file processing and content generation project.

**Project Goal:**
The main objective is to process a set of English literature chapter PDFs located in `/home/user/test/english textbooks`. For each chapter, you must create two corresponding files:
1.  A clean, text-only version of the story/poem in the `/home/user/test/Text/` directory.
2.  A highly detailed, comprehensive question set in the `/home/user/test/questions/` directory.

Some chapters have already been processed correctly, but several are incomplete. Your task is to identify the incomplete chapters and process them according to the strict rules below.

**Step 1: Identify Incomplete Chapters**
First, you must determine which chapters still need to be processed. A chapter is considered incomplete if a corresponding text file does not exist in the `/home/user/test/Text/` directory.

To do this, compare the file listings of `/home/user/test/questions` and `/home/user/test/Text`. For every `.md` file in `/questions`, ensure a `.md` file with the exact same name exists in `/Text`. Create a list of the missing files from the `/Text` directory. These are the chapters you need to process.

**Step 2: Process Each Incomplete Chapter**
For each chapter you identified as incomplete, perform the following two tasks in sequence:

**Task A: Text Extraction**
1.  Locate the corresponding PDF file in `/home/user/test/english textbooks`. The PDF will have the same name as the chapter (e.g., for "The Rattrap", use `The Rattrap.pdf`).
2.  Read the PDF and extract **only the core narrative text** of the story or poem.
3.  **CRITICAL RULE:** You must exclude all supplementary material. Do NOT include:
    *   "About the author" sections.
    *   "Before you read" sections.
    *   "Think as you read" boxes or similar in-text prompts.
    *   Footnotes, word definitions, or glossaries.
    *   Any post-story content like "Understanding the text," "Working with words," or "Things to do."
4.  Save this clean text into a new Markdown file (`.md`) inside the `/home/user/test/Text/` directory. The filename must exactly match the chapter name.
5.  **FORMATTING RULE:** It is essential that you preserve the original indentation of the text as it appears in the source, especially for poems.

**Task B: Comprehensive Question Generation**
1.  Using the clean text file you just created in the `/Text` directory, generate a new set of questions.
2.  **CRITICAL RULE:** The questions must be exhaustive and cover **every single piece of information** in the text. No detail is too small. This includes specific actions, spoken dialogue, character thoughts, descriptions of people, places, and objects, and the precise sequence of events.
3.  **CHRONOLOGY RULE:** The questions MUST be in **strict chronological order**, following the narrative of the story exactly from the first sentence to the last.
4.  **FORMATTING RULES:**
    *   BEFORE YOU START REFER TO ALREADY PRESENT "The Tiger King.md" at `/home/user/test/questions/` directory for the format.
    *   Save the questions in the corresponding Markdown file in the `/home/user/test/questions/` directory, overwriting the existing file.
    *   The questions should be a numbered list.
    *   The file should start with a level-2 Markdown header of the chapter title (e.g., `## The Rattrap`).
    *   Do **NOT** include answers to the questions.

Start by identifying the incomplete chapters, and then begin processing the first one on your list.