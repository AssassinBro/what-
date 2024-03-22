import discord # Подключаем библиотеку
from discord.ext import commands, tasks
import time
import random2
import configparser  # импортируем библиотеку
from discord import client
config = configparser.ConfigParser()  # создаём объекта парсера
config.read("config.ini")  # читаем конфиг
channel_id = int(config.get('Discord','channel'))
token = config.get('Discord','token')
owners = list(map(int,config.get('Discord','owners').split()))
intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
async def cooldown():
    return random2.randint(0,30)
# Задаём префикс и интенты
bot = commands.Bot(command_prefix='>', intents=intents) 
meow_list = ['мяу','мурь~','мряфк~','UwU','OwO','QwQ','meow~','мья!~','Мррррх~','Ньях','Ня','DwD','kill yourself now!','Мряфх!~']
# С помощью декоратора создаём первую команду
@bot.command()
async def meow(ctx):
    await ctx.send(meow_list[random2.randint(0, len(meow_list)-1)])

def is_owner(ctx):
    return ctx.author.id in owners


@bot.command()
async def sex(ctx):
    if is_owner(ctx):
        await ctx.send('Ам..Нет пожалуй?_Немного покраснев,Юна повернула свой взгляд на дверь в ЛС... <@683007560868954129>_')
    else:
        await ctx.send('да пошев ти...')

print("Бот запущен!")
@tasks.loop(seconds=30)
async def func():
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(meow_list[random2.randint(0, len(meow_list)-1)])
    else:
        print("Канал не найден или бот не имеет доступа к нему.")
@bot.event
async def on_ready():
    func.start()
bot.run(token)
client.run(token)