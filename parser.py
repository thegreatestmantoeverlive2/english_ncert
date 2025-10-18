
import os
import json
from markdown_it import MarkdownIt

def parse_questions():
    """
    Parses markdown files in the 'questions' directory and converts them to JSON.
    """
    questions_dir = 'questions'
    output_dir = 'question jsons'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    md = MarkdownIt()

    for filename in os.listdir(questions_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(questions_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            tokens = md.parse(content)

            questions = []
            in_list_item = False

            for token in tokens:
                if token.type == 'list_item_open':
                    in_list_item = True
                elif token.type == 'list_item_close':
                    in_list_item = False
                elif in_list_item and token.type == 'inline':
                    # Remove the number and the period from the question
                    question_text = token.content
                    questions.append(question_text)

            if not questions:
                print(f"Error: No questions found in {filename}")
                continue

            output_filename = os.path.splitext(filename)[0] + '.json'
            output_filepath = os.path.join(output_dir, output_filename)

            with open(output_filepath, 'w', encoding='utf-8') as f:
                json.dump(questions, f, indent=4)

if __name__ == '__main__':
    parse_questions()
