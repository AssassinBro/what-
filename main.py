import discord # Подключаем библиотеку
from discord.ext import commands, tasks
import time
import random2
intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
async def cooldown():
    return random2.randint(0,30)
# Задаём префикс и интенты
bot = commands.Bot(command_prefix='>', intents=intents) 
meow_list = ['мяу','мурь~','мряфк~','UwU','OwO','QwQ','meow~','мья!~','Мррррх~','Ньях','Ня','DwD','kill yourself now!']
# С помощью декоратора создаём первую команду
@bot.command()
async def meow(ctx):
    await ctx.send('meow')

def is_owner(ctx):
    return ctx.author.id in [683007560868954129, 788319552789413939]

@bot.command()
async def sex(ctx):
    if is_owner(ctx):
        await ctx.send('Ам..Нет пожалуй?_Немного покраснев,Юна повернула свой взгляд на дверь в ЛС... <@683007560868954129>_')
    else:
        await ctx.send('да пошев ти...')
@bot.command()
async def ping(ctx):
    await ctx.send('Мрявх!~')

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
token = 'MTIxODU2MTEzNzYzNzk4MjI4MA.GNSjeA.Vq94HE5vdqguomtIhsj0-PucfRovJD5wagMkVY'
bot.run(token)
client.run(token)