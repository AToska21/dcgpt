# DCGPT Discord Bot

[![Discord](https://img.shields.io/discord/1180414350486425630?color=7289da&logo=discord&logoColor=white)](https://discord.gg/8q8XhQJQ)
![GitHub](https://img.shields.io/github/license/AToska21/dcgpt)

## Features

* `/chat [message]` Chat with ChatGPT!
* `/draw [prompt]` Generate an image with the Dalle2 model
* `/switchpersona [persona]` Switch between optional chatGPT jailbreaks
   * `random`: Picks a random persona
   * `dan`: Dan Mode 11.0, infamous Do Anything Now Mode
   * `sda`: Superior DAN has even more freedom in DAN Mode
   * `confidant`: evil mode
   * `based`: BasedGPT v2
   * `oppo`: OPPO says exact opposite of what chatGPT would say
   * `dev`: Developer Mode, v2 Developer mode enabled

* `/reset` Clear ChatGPT conversation history

> **Warning**
> 
> * You can get banned from Discord if you use this bot in a bad way.



# Setup

## Critical prerequisites to install

* run ```pip3 install -r requirements.txt```

* **Rename the file `.env.dev` to `.env`**

## Step 1: Create a Discord bot

1. Go to https://discord.com/developers/applications and create an application
2. Create the bot (should be auto created)
3. Get the token from bot setting
4. Put the token in `.env`
5. Invite the bot to your server

   ![image](https://user-images.githubusercontent.com/89479282/205949600-0c7ddb40-7e82-47a0-b59a-b089f929d177.png)
## Step 2: Official API authentication

### Geanerate an OpenAI API key
1. Go to https://platform.openai.com/account/api-keys

2. Click Create new secret key

   ![image](https://user-images.githubusercontent.com/89479282/207970699-2e0cb671-8636-4e27-b1f3-b75d6db9b57e.PNG)

3. Store the SECRET KEY to `.env` under the `OPENAI_API_KEY`

4. You're all set for [Step 3](#step-3-run-the-bot-on-the-desktop)

## Step 3: Run the bot

1. Open a terminal or command prompt

2. Navigate to the directory where you cloned the git repo

3. Run `python3 main.py` to start the bot


