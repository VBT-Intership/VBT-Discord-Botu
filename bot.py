# Please do not change this area
import discord
from discord.ext import commands
import requests

# Bot çağırılıyor
bot = commands.Bot(command_prefix='!')

# Bot komutu
@bot.command()
# Hangi rolün bu komutu çağırabileceğini belirtiliyor. Default olarak admin.
@commands.has_role("admin")
async def yoklama(ctx, *args):
    # Default olarak 60 dakika belirlenmiştir.
    time = 60
    # Eğer parametre olarak bir süre belirtirseniz dakika cinsinden hesaplanacaktır.
    if len(args) >= 1:
        time = args[0]
    # Default olarak mesaj aşağıdaki şekilde belirlenmiştir.
    metin = "Yoklama Başlamıştır. "+str(time)+" dakika içerisinde \N{THUMBS UP SIGN} reaksiyonu vererek yoklamaya katılabilirsiniz."
    # Eğer parametre olarak bir mesaj belirtirseniz "MESAJINIZ" olarak girmeniz gerekmektedir. 
    #'MESAJ' sadece ilk kelimeyi kabul etmektedir. .
    if len(args) >= 2:
	    metin = args[1]
    # Hangi kanala mesaj atmasını istiyorsanız o kanalın "CHANNEL_ID"nizi giriniz.
    channel = bot.get_channel("CHANNEL_ID")
    # Belirttiğiniz mesaj eğer zaman belirlediyseniz o kadar dakika duracaktır.
    # Zaman belirtmediyseniz sadece default olarak tanımlanan süre kadar gözükecektir.
    messagem = await channel.send(metin, delete_after = 60*time)
    # Bot mesajı attıktan hemen sonra emoji atacaktır.
    await messagem.add_reaction("\N{THUMBS UP SIGN}")
    message_id = messagem.id

# Burada yoklamaya katılan kişileri bulabilirsiniz.
@bot.event
async def on_reaction_add(reaction, user):
    channel = bot.get_channel("CHANNEL_ID")
    if user.bot or reaction.message.channel.id != channel.id:
       return
    else:
      print('Biri yoklamaya katıldı.');

# Bu alana bot keyinizi girmeniz gerekmektedir.
bot.run('DC_BOT_KEY')