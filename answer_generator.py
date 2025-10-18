
import os
import json
import re

def generate_ai_answer(question, extract):
    """
    Generates a concise, AI-powered answer based on the question and the extracted text.
    This is a placeholder for a more sophisticated model, but it will provide a direct answer.
    """
    if not extract:
        return None

    # This is a rule-based approach to generating a direct answer.
    # A more advanced implementation would use a language model.
    # For now, I'll return the extract as the answer, since I don't have a local LLM to call.
    # In a real-world scenario, I'd use an API or a local model here.
    return extract


def find_best_line(question, text_content):
    """
    Finds the best line in the text that answers the question.
    """
    lines = text_content.split('\n')

    question_words = set(re.findall(r'\w+', question.lower()))
    stopwords = {'a', 'an', 'the', 'is', 'in', 'it', 'of', 'for', 'on', 'was', 'were', 'to', 'and', 'what', 'where', 'how', 'did'}
    keywords = question_words - stopwords

    if not keywords:
        return None, None, None

    best_line = ""
    max_score = 0
    best_line_number = -1

    for i, line in enumerate(lines):
        line_words = set(re.findall(r'\w+', line.lower()))
        score = len(keywords.intersection(line_words))

        if score > max_score:
            max_score = score
            best_line = line
            best_line_number = i + 1

    if not best_line:
        return None, None, None

    col_number = 1 # We are returning the whole line
    return best_line.strip(), best_line_number, col_number


def generate_answers():
    """
    Generates answers for the questions in the 'question jsons' directory.
    """
    questions_dir = 'question jsons'
    texts_dir = 'Text'
    answers_dir = 'answers'

    if not os.path.exists(answers_dir):
        os.makedirs(answers_dir)

    for filename in os.listdir(questions_dir):
        if filename.endswith('.json'):
            question_filepath = os.path.join(questions_dir, filename)
            text_filename = os.path.splitext(filename)[0] + '.md'
            text_filepath = os.path.join(texts_dir, text_filename)
            answer_filepath = os.path.join(answers_dir, filename)

            if not os.path.exists(text_filepath):
                print(f"Warning: Text file not found for {filename}. Skipping.")
                continue

            with open(question_filepath, 'r', encoding='utf-8') as f:
                questions = json.load(f)

            with open(text_filepath, 'r', encoding='utf-8') as f:
                text_content = f.read()

            answers = []
            for question in questions:
                extract, line, col = find_best_line(question, text_content)
                answer = generate_ai_answer(question, extract)
                citation = f"{text_filename}#L{line}:{col}" if extract else None

                answers.append({
                    "question": question,
                    "answer": answer,
                    "extract": extract,
                    "citation": citation
                })

            with open(answer_filepath, 'w', encoding='utf-8') as f:
                json.dump(answers, f, indent=4)


if __name__ == '__main__':
    generate_answers()
