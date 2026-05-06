# Publishing comics

The program publishes a random xkcd comic to a Telegram channel.

## How to install

### Obtaining API Keys

The program requires the following keys to function:

#### Telegram Bot Token
1. Message @BotFather on Telegram
2. Send the /newbot command and follow the instructions
3. Get your bot token (looks like 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz)
4. Create a channel and add your bot as an administrator

#### Telegram Chat ID
1. After adding the bot to your channel, send any message
2. Get the Chat ID via @userinfobot


Create a `.env` file add your bot's token and chat ID. Here's an example:
```
TELEGRAM_BOT_TOKEN=[Bot's token]
TELEGRAM_CHAT_ID=[The name of the Telegram channel to which the comics are sent]
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

## Launch

### Scripts Usage Examples

#### Publish random comic
```
#Publish a random xkcd comic to a Telegram channel
python main.py
```

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).