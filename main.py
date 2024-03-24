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
channel_id = int(config.get('Discord','channel'))
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

print("Бот запущен!")
@tasks.loop(seconds=30)
async def func():
    channel = bot.get_channel(1189778371962474518)
    if channel:
        await channel.send(meow_list[random2.randint(0, len(meow_list)-1)])
    else:
        print("Канал не найден или бот не имеет доступа к нему.")
@bot.event
async def on_ready():
    func.start()
bot.run(token)