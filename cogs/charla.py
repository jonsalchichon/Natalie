import discord
from discord.ext import commands
import random

class HablarCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(HablarCog(bot))
    print('MODULO CHARLA IMPORTADO')