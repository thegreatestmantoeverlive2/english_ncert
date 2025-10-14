Act as an expert English literature tutor and quiz generator. Your task is to create a comprehensive, chronological question set that tests deep, factual knowledge of a story's plot, character actions, thoughts, and subtle details.

**INSTRUCTIONS:**

1.  You will be provided with the full text of a story.
2.  You must generate a list of questions that cover **every single piece of information** in the story, leaving no detail behind. This includes:
    *   Specific actions characters take.
    *   Exact dialogues or key phrases spoken.
    *   Characters' internal thoughts, feelings, and motivations.
    *   Descriptions of settings, objects, and appearances.
    *   The sequence of events in the exact order they occur.
    *   Seemingly minor details that a casual reader might overlook.

3.  **CRITICAL: Question Order:** The questions MUST be in strict chronological order. The first question must be about the very first sentence or event in the story. The final question must be about the very last sentence or event. The sequence of questions should mirror the plot's progression, creating a continuous narrative path when read aloud.

4.  **Question Formatting:**
    *   Phrase questions to prompt for specific details. Use starters like: "What does [Character] do right after...?", "What is [Character] thinking when...?", "What are the exact words used to describe...?", "What specific object does...?"
    *   Avoid broad, interpretive, or opinion-based questions. Focus solely on factual, text-based recall.

**STORY TEXT FOR QUIZ GENERATION:**

[PASTE THE ENTIRE TEXT OF YOUR STORY HERE]

---

**ADDITIONAL INSTRUCTIONS FOR PROCESSING:**

You will be provided with multiple PDF files, each representing a chapter of a larger text. You need to perform the following steps for each PDF file:

1.  **Rename PDF:** Rename the PDF file in the `/english textbooks` folder of current directory to match the chapter name it contains.
2.  **Extract Text:** Extract the full text content from the (now renamed) PDF file.
3.  **Generate Questions:** Using the extracted text, apply the "INSTRUCTIONS" outlined above to generate a comprehensive, chronological set of quiz questions covering all details.
4.  **Save Questions:** Save the generated questions as a Markdown file in the `/questions` folder of the current directory. The filename for the Markdown file should be the same as the chapter name (and the renamed PDF file).
5. **Sample Questions** have already been given in for one chapter in the "questions" folder, REFER THAT BEFORE YOU EVEN BEGIN

---

**BEGIN PROCESSING FILES AND GENERATING QUESTION SETS NOW.**