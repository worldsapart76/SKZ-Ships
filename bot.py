import os
import random
import discord
from discord.ext import commands
from discord import app_commands

print("BOT STARTING...")

TOKEN = os.getenv("TOKEN")

SKZ_MEMBERS = [
    "Bang Chan",
    "Lee Know",
    "Changbin",
    "Hyunjin",
    "Han",
    "Felix",
    "Seungmin",
    "I.N",
]

class SKZShips(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(
            command_prefix="!",
            intents=intents,
            allowed_contexts=app_commands.AppCommandContext(
                guild=True,
                dm_channel=True,
                private_channel=True,  # includes group DMs
            ),
            allowed_installs=app_commands.AppInstallationType(
                guild=True,
                user=True,
            ),
        )

    async def setup_hook(self):
        synced = await self.tree.sync()
        print(f"Synced {len(synced)} global command(s).")

bot = SKZShips()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="skzpair", description="Generate a random Stray Kids pair")
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def skzpair(interaction: discord.Interaction):
    pair = random.sample(SKZ_MEMBERS, 2)
    await interaction.response.send_message(
        f"🎲 **Random Stray Kids Pair**\n**{pair[0]}** + **{pair[1]}**"
    )

bot.run(TOKEN)