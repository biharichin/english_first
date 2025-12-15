import re

def parse_mcq_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    questions = []
    # Split by two or more newlines, which seems to separate question blocks
    question_blocks = re.split(r'\n\s*\n', content)

    for block in question_blocks:
        block = block.strip()
        if not block or block.startswith("TOPIC:"):
            continue

        lines = block.split('\n')
        
        try:
            # The first line is the question
            question_text = lines[0].strip()

            # Find where options start and end
            option_lines = []
            answer_line_index = -1
            for i, line in enumerate(lines):
                if re.match(r'\([A-Z]\)', line.strip()):
                    option_lines.append(line.strip())
                if line.strip().startswith("Answer:"):
                    answer_line_index = i
            
            if not option_lines or answer_line_index == -1:
                continue

            options = [re.sub(r'\([A-Z]\)\s*', '', line).strip() for line in option_lines]

            # Extract correct answer index
            answer_line = lines[answer_line_index].strip()
            correct_option_letter = re.search(r'\(([A-Z])\)', answer_line).group(1)
            correct_option_index = "ABCD".find(correct_option_letter)

            # Extract explanation
            explanation = ""
            if (answer_line_index + 1) < len(lines) and lines[answer_line_index + 1].strip().lower().startswith("explanation:"):
                 explanation_lines = lines[answer_line_index + 2:]
                 explanation = '\n'.join(explanation_lines).strip()


            questions.append({
                'question': question_text,
                'options': options,
                'correct_option_index': correct_option_index,
                'explanation': explanation
            })
        except (IndexError, AttributeError) as e:
            print(f"Skipping a block due to parsing error: {e}\nBlock:\n{block}\n")
            continue
            
    return questions

if __name__ == '__main__':
    # Assuming the text file is in the parent directory
    # In the GitHub Action, the paths will need to be correct.
    parsed_questions = parse_mcq_file('../TOPIC 1 TO 10.txt')
    print(f"Successfully parsed {len(parsed_questions)} questions.")
    if parsed_questions:
        print("\nFirst Question:")
        print(parsed_questions[0])
        print("\nLast Question:")
        print(parsed_questions[-1])
