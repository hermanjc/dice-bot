# Dice Bot

Discord chatbot for simulating rolls of polyhedral dice

## Environment

It is recommended to use venv to create a virtual environment for installing dependencies.

To install dependencies run `pip install -r requirements.txt`

## Running

In order for the bot to run you will need to uncomment the `client.run()` line in bot.py and add your bot token. Then the bot can be ran with `python bot.py`. To run the bot in the background run: `nohup python bot.py &`

## Usage

To roll dice type  the following into a Discord channel the bot is listening to:
> `/roll ndm` where n is the number of dice and m is the number of sides.
