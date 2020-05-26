import discord
from discord.ext import commands
import asyncio
import datetime

class ModeracionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.has_any_role('Moderador','EL REY FAIL','MASTER')
    async def limpiar(self, ctx, *, number:int=None):
        if ctx.message.author.guild_permissions.manage_messages:
            try:
                if number is None:
                    await ctx.send('Tontito... Debes ingresar un numero ')
                else:
                    deleted = await ctx.message.channel.purge(limit=number)
                    await ctx.send(f'MENSAJES BORRADOS POR {ctx.message.author.mention}: ✅`{len(deleted)}`')
            except:
                await ctx.send("NO PUEDO BORRAR EL MENSAJE AQUI.")
        else:
            await ctx.send("PARECE QUE NO ESTAS AUTORIZADO PARA USAR ESTA COMANDO")
            pass
        

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.has_any_role('Moderador','EL REY FAIL')
    async def expulsar(self, ctx, user: discord.Member, *, reason=None):
        if user.guild_permissions.manage_messages:
            await ctx.send("NO PUEDES EXPULSAR A ❎ADMIN/MODERADORES❎")
        elif ctx.message.author.guild_permissions.kick_members:
            if reason is None:
                await ctx.guild.kick(user=user, reason= 'None')
                await ctx.send(f'{user} ALGUIEN TIENE QUE PERDER...')
            else:
                await ctx.guild.kick(user=user, reason=reason)
                await ctx.send(f'{user} ALGUIEN TIENE QUE PERDER...')
        else:
            await ctx.send('PARECE QUE NO ESTAS AUTORIZADO PARA USAR ESTA COMANDO')
            pass


    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.has_any_role('Moderador','EL REY FAIL')
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        if user.guild_permissions.manage_messages:
            await ctx.send("NO PUEDES BANEAR A ❎ADMIN/MODERADORES❎")
        elif ctx.message.author.guild_permissions.ban_members:
            if reason is None:
                await ctx.guild.ban(user=user, reason= 'None')
                await ctx.send(f'{user} FUE BANEADO...')
            else:
                await ctx.guild.ban(user=user, reason=reason)
                await ctx.send(f'{user} PIENSA QUE ES SOLO UN APAGON PERMANENTE...')
        else:
            await ctx.send('PARECE QUE NO ESTAS AUTORIZADO PARA USAR ESTA COMANDO')
            pass


    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.has_any_role('Moderador','EL REY FAIL')
    async def guiamod(self, ctx):
        embed = discord.Embed(title=f"🅰🆈🆄🅳🅰", description="HERRAMIENTAS PARA MODERADORES", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        embed.add_field(name="ban", value=f"BANEA A USUARIOS CON @, SEGUIDO ESCRIBE SU NOMBRE")
        embed.add_field(name="expulsar", value=f"EXPULSA/SACA TEMPORALMENTE A UN USUARIO, CON @ SEGUIDO ESCRIBE SU NOMBRE ")
        embed.add_field(name="limpiar", value=f"LIMPIA/BORRA COMENTARIOS, LIMPIAR + (numero de comentarios a limpiar)")
        await ctx.send(embed=embed)
        pass


def setup(bot):
    bot.add_cog(ModeracionCog(bot))
    print('ModNat IMPORTADO')