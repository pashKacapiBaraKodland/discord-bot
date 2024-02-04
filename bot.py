from botlogic import gen_pass
import discord, random

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('привет'):
        await message.channel.send("привет!")
    elif message.content.startswith('пока'):
        await message.channel.send("пока!")
    elif message.content.startswith("!пароль"):
        await message.channel.send(gen_pass(5))
    elif message.content.startswith('как дела'):
        await message.channel.send("хорошо")
    elif message.content.startswith('сколько тебе лет'):
        await message.channel.send("20")
    elif message.content.startswith('ты молодец'):
        await message.channel.send("ты тоже")
    elif message.content.startswith('кофе'):
        await message.channel.send("скоро будет")
    elif message.content.startswith('готово кофе'):
        await message.channel.send('кофе готово 😀🧋')
    elif message.content.startswith('подбрось монету'):
        coin = random.choice(["орел", "решка"])
        await message.channel.send(coin)
    elif message.content.startswith('улыбнись'):
        emoji = random.choice(["😎", "😂"])
        await message.channel.send(emoji)

client.run("your token")
