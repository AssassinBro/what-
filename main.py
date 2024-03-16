import discord # Подключаем библиотеку
from discord.ext import commands

intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
# Задаём префикс и интенты
bot = commands.Bot(command_prefix='!', intents=intents) 

# С помощью декоратора создаём первую команду
@bot.command()
async def ping(ctx):
    await ctx.send('ты че ахуел сука меня пинговать?')


bot.run('MTIxODU2MTEzNzYzNzk4MjI4MA.GNSjeA.Vq94HE5vdqguomtIhsj0-PucfRovJD5wagMkVY')