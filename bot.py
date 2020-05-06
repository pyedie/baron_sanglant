import discord
from discord.ext import commands
from discord.utils import get
import time
import random

bot = commands.Bot(command_prefix='µbaron')
client = commands.Bot(command_prefix='µbaron')
bot.remove_command("help")

@bot.event
async def on_ready():
#    await client.change_presence(activity=Game(name="garder l'entrée de Poudlard"))
    print("Baron Sanglant - LeviOoOsA")
    print("Bot Ready!")

@bot.event
async def on_message(message):
    author = message.author
    authorID = message.author.id
    content = message.content
    contentLw = content.lower()
    channel = message.channel.id
    role = get(message.author.guild.roles, id=int(707324283986378782))
    # role = discord.utils.get(author.roles, name="Sans Fiche")
    if channel == 707220218379763742:
        if authorID != 707330033252958248:
            await message.delete()
            print("[[===============================]]\n" + "   Membre : " + str(author) + "\n\n    Message : " + str(content) + "\n[[===============================]]")
            if contentLw == "voldemort" or contentLw == "lord voldemort":
                await author.add_roles(role)
            else:
                await message.channel.send("Faux !", delete_after=4)
        else:
            await bot.process_commands(message)
    
@bot.command()
async def enterTest(ctx):
    await ctx.message.delete()
    await ctx.send("Bienvenue Moldus ! Si tu veux rentrer dans le monde des sorciers, cela ne seras pas si simple !\nRéponds à cette énigme et tu ouvriras le passage, au bout de 3 échecs, tu pourras demander un indice. **Bonne chance à toi ! ^_^**")
    embed = discord.Embed(title="Qui a dit cette phrase culte ?", description="J’ai lu dans ton cœur, et ton cœur est mien.", color = 0x09bbff)
    await ctx.send(embed=embed)

bot.run(token)
