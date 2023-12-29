import os
import openai
import discord
import json
from random import randrange
from src.aclient import client
from discord import app_commands
from src import log, personas, responses

logger = log.setup_logger(__name__)

def run_discord_bot():
    @client.event
    async def on_ready():
        await client.tree.sync()
        logger.info(f'{client.user} is now running!')

    @client.tree.command(name="chat", description="Chat with DCGPT.")
    async def chat(interaction: discord.Interaction, *, message: str):
        if interaction.user == client.user:
            return
        username = str(interaction.user)
        channel = str(interaction.channel)
        logger.info(
            f"\x1b[31m{username}\x1b[0m : /chat [{message}] in ({channel})")
        await client.send_message(interaction, message)

    @client.tree.command(name="reset", description="Reset conversation history.")
    async def reset(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=False)
        if client.chat_model == "OFFICIAL":
            client.chatbot = client.get_chatbot_model()
        await interaction.followup.send("> **INFO: forgor.**")
        await interaction.followup.send("> **INFO: Reset conversation history.**")
        personas.current_persona = "standard"
        logger.warning(
            f"\x1b[31m{client.chat_model} bot has been successfully reset\x1b[0m")

    @client.tree.command(name="help", description="Show help message.")
    async def help(interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=False)
        await interaction.followup.send(""":star: **BASIC COMMANDS** \n
        - `/chat [message]` Chat with ChatGPT!
        - `/reset` Clear ChatGPT conversation history
<<<<<<< HEAD

For complete documentation, please visit:
https://gpt.natsuki.live""")
=======
""")
>>>>>>> 2cc103a (AAA)

        logger.info(
            "\x1b[31mSomeone needs help!\x1b[0m")

    TOKEN = os.getenv("DISCORD_BOT_TOKEN")

    client.run(TOKEN)
