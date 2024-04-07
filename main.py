import time
import random2
import configparser  # импортируем библиотеку
import disnake
import disnake as discord
from disnake.ext import commands, tasks
config = configparser.ConfigParser()  # создаём объекта парсера
config.read("config.ini")  # читаем конфиг
intents = disnake.Intents.default() # Подключаем "Разрешения"
bot = commands.Bot(intents=intents.all(), command_prefix='>')
channel_id = int(config.get('Discord','channel_id'))
servers = [1132291575377039390,1189778371496923207]
token = config.get('Discord','token')
owners = list(map(int,config.get('Discord','owners').split()))
async def cooldown():
    return random2.randint(0,30)
# Задаём префикс и интенты
meow_list = ['мяу','мурь~','мряфк~','UwU','OwO','QwQ','meow~','мья!~','Мррррх~','Ньях','Ня','DwD','kill yourself now!','Мряфх!~']
# С помощью декоратора создаём первую команду
@bot.slash_command(guild_ids=servers)
async def meow(inter):
    await inter.response.send_message("meow")
def is_owner(inter):
    return inter.author.id in owners

@bot.slash_command(guild_ids=servers)
async def ping(inter):
    await inter.response.send_message("Понг!")
@bot.slash_command(guild_ids=servers)
async def sex(inter):
    if is_owner(inter):
        await inter.response.send_message('Ам..Нет пожалуй?_Немного покраснев,Юна повернула свой взгляд на дверь в ЛС... <@683007560868954129>_')
    else:
        await inter.response.send_message("да пошев ти...")
@bot.slash_command(guild_ids=servers)
async def socks(inter):
    if is_owner(inter):
        await inter.response.send_message('https://media.discordapp.net/attachments/975785515985010769/1183337251728527380/attachment.gif?ex=6624da32&is=66126532&hm=17b229b961c09fb524ff3b76330c60a46ef05a40efce4ab0a34357e8d506747d&')
    else:
        await inter.response.send_message("Аэээ...Держи ножки паши https://cdn.discordapp.com/attachments/1132291576039747677/1226594778708180993/IMG_1812.jpg?ex=66255668&is=6612e168&hm=a3e0766d6457f5bbb522a3a3e514ded30a71a410157988b043afffc4b60751c3&")

print("Бот запущен!")
@tasks.loop(seconds=30)
async def func():
    channel = bot.get_channel(1132291576039747677)
    if channel:
        await channel.send(meow_list[random2.randint(0, len(meow_list)-1)])
    else:
        print("Канал не найден или бот не имеет доступа к нему.")
@bot.event
async def on_ready():
    func.start()
bot.run(token)