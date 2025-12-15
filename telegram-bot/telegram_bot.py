import os
import telegram
import time
from mcq_parser import parse_mcq_file

# --- CONFIGURATION ---
# It's recommended to set these as environment variables in your deployment environment
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "YOUR_TELEGRAM_API_TOKEN")
# Add chat IDs as a comma-separated string in your environment variables
CHAT_IDS = os.getenv("CHAT_IDS", "7695772994,8070930921").split(',')

QUESTIONS_FILE = '../TOPIC 1 TO 10.txt'
PROGRESS_FILE = 'progress.txt'
QUESTIONS_PER_DAY = 20

def get_progress():
    """Reads the index of the last question sent."""
    try:
        with open(PROGRESS_FILE, 'r') as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def save_progress(index):
    """Saves the index of the last question sent."""
    with open(PROGRESS_FILE, 'w') as f:
        f.write(str(index))

def main():
    """Main function to fetch questions and send them."""
    if TELEGRAM_TOKEN == "YOUR_TELEGRAM_API_TOKEN":
        print("ERROR: Telegram API token is not set. Please set the TELEGRAM_TOKEN environment variable.")
        return

    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    
    all_questions = parse_mcq_file(QUESTIONS_FILE)
    if not all_questions:
        print("No questions found in the file.")
        return

    last_question_index = get_progress()
    
    start_index = last_question_index
    end_index = start_index + QUESTIONS_PER_DAY

    questions_to_send = all_questions[start_index:end_index]

    if not questions_to_send:
        message = "No more questions available. We are done!"
        print(message)
        for chat_id in CHAT_IDS:
            try:
                bot.send_message(chat_id=chat_id.strip(), text=message)
            except Exception as e:
                print(f"Failed to send completion message to {chat_id}: {e}")
        return

    print(f"Sending questions from {start_index + 1} to {end_index}")

    for i, q in enumerate(questions_to_send):
        question_number = start_index + i + 1
        
        for chat_id in CHAT_IDS:
            chat_id = chat_id.strip()
            if not chat_id:
                continue
            
            try:
                print(f"Sending question {question_number} to chat ID {chat_id}")
                bot.send_poll(
                    chat_id=chat_id,
                    question=f"Q{question_number}: {q['question']}",
                    options=q['options'],
                    type=telegram.Poll.QUIZ,
                    correct_option_id=q['correct_option_index'],
                    explanation=q.get('explanation', '')
                )
                # Add a small delay to avoid hitting Telegram's rate limits
                time.sleep(1) 
            except Exception as e:
                print(f"Failed to send question to {chat_id}: {e}")
    
    # Update progress to the new index
    new_progress = end_index
    save_progress(new_progress)
    print(f"Successfully sent questions. Progress updated to {new_progress}.")

if __name__ == "__main__":
    main()
