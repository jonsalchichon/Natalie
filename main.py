import datetime
import discord
from discord.ext import commands 
from urllib import parse, request
import re
import asyncio
import sys

TOKEN = "NzEyNDYzNzQxODk1MzExNDIx.XsR7pw.As_KyHnqqquOanWQPKUBaSS3Q0k"
#####################################################################
bot = commands.Bot(command_prefix='/', description="El comando predefinido",case_insensitive=True)

@bot.event
async def on_ready():
    print('ESTOY LISTA')
    return await bot.change_presence(activity=discord.Activity(type=1))

@bot.event
async def on_nember_update(before,after):
    nombre = after.nick
    if nombre:
            if nombre.lower().count("xxx") >0:
               if nombreAnterior:
                   await after.edit(nick = nombreAnterior)

@bot.event
async def on_member_join(member):
    embed = discord.Embed(colour=0x95efcc, description=f"BIENVENIDO AL ✪LOWED✪ ( ͡~ ͜ʖ ͡°) ERES EL {len(list(member.guild.members))} MIEMBRO!")
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()
    channel = bot.get_channel(id=608622219240800266)    
    await channel.send(embed=embed)



    
###################################################################
@bot.command()
async def redes(ctx):
    embed = discord.Embed(title=f"⚡REDES⚡", description="No olvides seguirlo, unirte es un gran apoyo ❤ ❤ ❤ ", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    embed.add_field(name="✪YOUTUBE✪", value=f'https://www.youtube.com/user/TheLobeznoGames')
    embed.add_field(name="✪TWITTER✪", value=f'https://twitter.com/LobeznoGames')
    embed.add_field(name="✪TWITCH✪", value=f'https://www.twitch.tv/lobeznogames')
    embed.add_field(name="✪INSTAGRAM✪", value=f'https://www.instagram.com/lobeznogames/?hl=es')
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/698214779503902801/712777208007229460/oklogodos.png")
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"♛LOWED♛", description="★Un lugar hecho para mancos★", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server creado en", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server creador", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID, cosas tecnicas...", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/698214779503902801/712777208007229460/oklogodos.png")
    await ctx.send(embed=embed)


@bot.command()
async def tutub(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})    
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode()) 
    # print(search_results)
    await ctx.send("✅AQUI TIENES QUERIDO✅" + '                                                                    http://www.youtube.com/watch?v=' + search_results[0])

@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(title=f"🅰🆈🆄🅳🅰", description="Recuerda, cada comando se inicia con ➞➞ /", timestamp=datetime.datetime.utcnow(), color=discord.Color.purple())
    embed.add_field(name="INFO", value=f"INFORMACION DEL SERVIDOR")
    embed.add_field(name="TUTUB", value=f"BUSCAR VIDEOS DE YOUTUBE")
    embed.add_field(name="REDES", value=f"LISTA DE REDES SOCIALES DE SERVIDOR")
    embed.add_field(name="VERSION", value=f"LISTA DE LAS UPDATES DE NATALIE")
    embed.add_field(name="DONAR", value=f"DONACION AL SERVIDOR")
    embed.add_field(name="GUIAMOD", value=f"MUESTRA UNA GUIA PARA MODERADORES")
    await ctx.send(embed=embed)

@bot.command()
async def version(ctx):
    embed = discord.Embed(title=f"★UPDATES★", description="Mis actualizaciones", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="VERSION⏩", value=f"1.0.0")
    embed.add_field(name="QUE HAY DE NUEVO?", value=f"#CORRECCION DE BUGS  #INTERFAZ MAS SIMPLE #CAMBIOS EN PREFIX #MODERACION ACTIVA!!   #BIENVENIADA A USUARIOS NUEVOS  #SEGUIRDAD ")
    embed.add_field(name="PROXIMAS UPDATES⏩", value=f"1.0.30")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/698214779503902801/704425753860767844/jeck-_zero-191009-2.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def donar(ctx):
    embed = discord.Embed(title=f"💰DONACION💰", description="Esto es opcional pero ayuda mucho ❤ ❤ ❤", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embed.add_field(name="💸DONAR💸", value=f"https://streamelements.com/Lobeznogames/tip")
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/698214779503902801/712756310407643146/logo.jpg")
    await ctx.send(embed=embed)

#################################################################################################################


bot.load_extension('cogs.moderacion')
bot.load_extension('cogs.charla')   
bot.run(TOKEN)





