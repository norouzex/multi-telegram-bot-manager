# Telegram Multi-Account Performance Optimizer

This project is designed to optimize the performance of Telegram scripts, allowing you to manage multiple accounts efficiently using a single account.

In this code, only one account is active at any given time, which decreases server resource usage. The main bot (active bot) triggers actions or calls other accounts to perform tasks as needed. When the chosen channel posts something, the accounts comment on the channel with different scheduling times. You can add other actions or tasks as desired, and after that, you can submit a pull request (PR) on this repo.

## Features

- Handle multiple Telegram accounts from one interface.
- Efficiently schedule messages and interactions.
- Performance optimization for faster execution.

## Prerequisites

- Python 3.8 or higher
- Virtual environment (optional but recommended)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/norouzex/MultiBotManager
   cd MultiBotManager
2. Create and activate a virtual environment:
   ```python -m venv venv
   .\venv\Scripts\activate  # For Windows
   source venv/bin/activate  # For macOS/Linux```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.tx

4. Create a .env file in the root directory of the project and add your environment variables:
   ```bash
    ADMIN_USERNAME="@your_admin_username"
    CHANNELS="channel1,channel2"
    MAIN_BOT_API_ID="your_bot_api_id"
    MAIN_BOT_API_HASH="your_bot_api_hash"

5. Create a bots_config.py file in the root directory of the project and add your bot configurations:
    ```bash
      bots = [
              {
                  'id': 'your_bot_id_1',
                  'hash': 'your_bot_hash_1',
                  'label': 'your_bot_label_1'
              },
              {
                  'id': 'your_bot_id_2',
                  'hash': 'your_bot_hash_2',
                  'label': 'your_bot_label_2'
              },
              # Add more bots as needed
          ]

## Usage
  To run the bot, execute the following command:
  
        python main.py



## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

