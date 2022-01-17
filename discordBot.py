import discord
import os
from dotenv import load_dotenv
from pybinance import get_price



load_dotenv()
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)
dst = os.getenv('DISCORD_TOKEN')


client = discord.Client()


@client.event
async def on_ready():
    print ("Bot on")


@client.event
async def on_message(message):
    prefix = "$"

    if message.content.startswith(prefix):
        command = message.content.strip(prefix)
        data = get_price(command)
        price = float (data['price'])
        round_price = round(price, 3)
        embed = discord.Embed(title=command, description=f"**precio de {command}**", color=discord.Color.blue())
        embed.add_field(name="Precio", value=round_price, inline=True)
        embed.add_field(name="Dev" , value="Jose Morales")
        await message.channel.send(embed=embed)


client.run(dst)