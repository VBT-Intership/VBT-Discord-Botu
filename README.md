# VBT Discord Yoklama Botu
<img src="https://1.bp.blogspot.com/-NlCnjAumxDM/Xb2a6a8JbWI/AAAAAAAAAH4/DT7WovEuQy8PPnRC81149C-KG5py8P1RgCLcBGAsYHQ/w1200-h630-p-k-no-nu/how-to-make-a-discord-bot-7c0fe302b98b05b145682344b3a4ec59.png">


Uzaktan staj yapan öğrencilerin yoklamasını kolay bir şekilde almak için Python ile geliştirilmiştir. Sizlerde kendi discord grubunuza bu kodu entegre ederek kullanabilirsiniz. 

## Kurulum
Eğer discord için özel bot oluşturmayı bilmiyorsanız [buraya tıklayarak](https://discordpy.readthedocs.io/en/latest/discord.html) öğrenebilirsiniz.
Daha fazla detay için [Discord Delevoper Portali](https://discord.com/developers/docs)'ni kontrol ediniz.
- Terminale bu komutu giriniz. `pip3 install -r requirements.txt`
- `bot.py` isimli dosyayı kod editörünüzde açın.
- 12 satırda bulunan `@commands.has_role("admin")` komutundan hangi rolün bu botu çağırabileceğini belirtiniz.
- 26 satırda bulunan `channel = bot.get_channel("CHANNEL_ID")` komutta `CHANNEL_ID` yerine hangi kanala çağırmak istiyorsanız o kanalın kanal id'sini giriniz.
- 44 satırda bulunan `bot.run('DC_BOT_KEY')` komutunda `'DC_BOT_KEY'` alanını düzenleyiniz. Burası botu çağırmak için kullandığınız komuttur.

## Bot Kullanımı
- `DC_BOT_KEY {zaman(dakika cinsinden)} {metin}` şeklindeki komut kullanılarak yoklama başlatılacaktır. Örneğin `bot_cagir 60 "Yoklama alınıyor."` veya `bot_cagir`
- `zaman` parametresi dakika şeklindedir, yazılmazsa default olarak 60 alınacaktır.
- `metin` parametresi ise default olarak aşağıdaki gibidir:
 "Yoklama Başlamıştır. 60 dakika içerisinde 👍 reaksiyonu vererek yoklamaya katılabilirsiniz."

## Yoklama İşleyişi
- 12 satırda atadığınız roldeki herhangi bir kişi yoklamayı başlatır.
- 26 satırda düzenlediğiniz kanala metin şeklinde bir mesaj gider ve altına bot tarafından 👍 emojisi reaksiyon olarak atılır.
- Yoklamanın ayarlanan zamanına kadar öğrenciler `düzenlediğiniz` kanaldaki mesajın altına emoji atarak yoklamaya katılırlar. 
- Belirlenen zamandan sonra mesaj silinir.
