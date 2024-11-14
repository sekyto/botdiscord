import discord
from discord import Intents, Client, Message
from responses import get_response

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username} said: "{user_message}" ({channel})')

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Nothing to send')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message_author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
   print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message: Message, message_content=None) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message_content
    channel: str = str(message.channel)

    print(f'{username} said: "{user_message}" ({channel})')
    await send_message(message, user_message)

def main() -> None:
    client.run('MTMwNDIyNDE2MDU3ODUzNTU1NQ.G_uI6u.MJc2BJFiRYEXQexw0Az0xOlICqp0sejJndiATM')

if __name__ == '__main__':
    main()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

client.run('MTMwNDIyNDE2MDU3ODUzNTU1NQ.G_uI6u.MJc2BJFiRYEXQexw0Az0xOlICqp0sejJndiATM')