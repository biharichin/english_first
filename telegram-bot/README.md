# Telegram MCQ Bot

This bot sends a set number of multiple-choice questions to specified Telegram chats every day at a scheduled time. It's built with Python and designed to be run for free using GitHub Actions.

## Features

- Parses questions from a simple `.txt` file.
- Sends questions as native Telegram quizzes (polls).
- Schedules sending using GitHub Actions.
- Keeps track of progress, so it doesn't send the same questions twice.
- Sends to multiple chats.
- It's completely free to host and run.

## Project Structure

```
.
├── TOPIC 1 TO 10.txt         # Your original file with questions
└── telegram-bot/
    ├── .github/
    │   └── workflows/
    │       └── send_mcqs.yml   # The GitHub Actions schedule
    ├── mcq_parser.py           # Script to parse the questions file
    ├── telegram_bot.py         # Main bot script
    ├── progress.txt            # Tracks which questions have been sent
    └── requirements.txt        # Python dependencies
```

## Setup Instructions

Follow these steps to get your bot running:

### 1. Get a Telegram Bot Token

1.  Open your Telegram app and search for the **`@BotFather`** bot.
2.  Start a chat with BotFather and send the `/newbot` command.
3.  Follow the instructions. Give your bot a name and a username.
4.  BotFather will give you a unique **API token**. It will look something like `1234567890:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`.
5.  **Copy this token and save it securely.**

### 2. Set up a GitHub Repository

1.  Create a new account on [GitHub](https://github.com/) if you don't have one.
2.  Create a **new repository**. You can make it `private` if you want to keep your question file and code hidden.
3.  Upload the files I've created for you to this new repository. The structure should look like the one described above. Specifically, you need to upload the `TOPIC 1 TO 10.txt` file and the entire `telegram-bot` folder.

### 3. Add Secrets to Your GitHub Repository

This is the most important step for keeping your token and chat IDs secure.

1.  In your new GitHub repository, go to **Settings** > **Secrets and variables** > **Actions**.
2.  Click the **New repository secret** button for each secret you need to add.

You need to add the following two secrets:

-   **`TELEGRAM_TOKEN`**:
    -   **Name**: `TELEGRAM_TOKEN`
    -   **Value**: Paste the API token you got from BotFather.

-   **`CHAT_IDS`**:
    -   **Name**: `CHAT_IDS`
    -   **Value**: This should be the chat IDs you want the bot to send messages to. Your chat ID is `7695772994` and your friend's is `8070930921`. So, the value should be `7695772994,8070930921`.
    > **Note**: For the bot to send messages to a user, the user must start the bot first. Open your bot in Telegram and press "Start". Your friend must do the same.

### 4. Enable and Run the Workflow

1.  Go to the **Actions** tab in your GitHub repository.
2.  You might see a message saying "Workflows aren't configured". Find the "Send Daily MCQs" workflow on the left and click on it.
3.  Enable the workflow if it's not already enabled.
4.  The bot is scheduled to run automatically at 3 PM IST. If you want to test it immediately, you can run it manually:
    -   Click on the **"Send Daily MCQs"** workflow.
    -   Click the **"Run workflow"** dropdown on the right.
    -   Click the green **"Run workflow"** button.

You're all set! Your bot will now send 20 questions every day. You can check the logs in the "Actions" tab to see if it ran successfully.
