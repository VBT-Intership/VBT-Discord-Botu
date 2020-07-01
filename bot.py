import discord
from discord.ext import commands
import requests
bot = commands.Bot(command_prefix='!')

@bot.command()
@commands.has_role("admin")
async def yoklama(ctx, *args):
    zaman = 60
    if len(args) >= 1:
        zaman = args[0]
    metin = "Yoklama Başlamıştır. "+str(zaman)+" dakika içerisinde \N{THUMBS UP SIGN} reaksiyonu vererek yoklamaya katılabilirsiniz."
    if len(args) >= 2:
	    metin = args[1]
    channel = bot.get_channel("CHANNEL_ID")
    messagem = await channel.send(metin, delete_after = 60*zaman)
    await messagem.add_reaction("\N{THUMBS UP SIGN}")
    message_id = messagem.id
	
@bot.event
async def on_reaction_add(reaction, user):
    channel = bot.get_channel("CHANNEL_ID")
    if user.bot or reaction.message.channel.id != channel.id:
       return
    else:
      print('Biri yoklamaya katıldı.');

bot.run('DC_BOT_KEY')
                          
