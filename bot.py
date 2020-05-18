import discord
from discord import File
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions, CheckFailure
import time
import random
import os

token = os.environ.get('token')
bot = commands.Bot(command_prefix='$')
client = commands.Bot(command_prefix='$')
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
    # chanLogs = get(message.channel.id, id=int(707643584354189342))
    role = get(message.author.guild.roles, id=int(707324283986378782))
    if channel == 707220218379763742:
        if authorID != 707330033252958248:
            await message.delete()
            print("[[===============================]]\n" + "   Membre : " + str(author) + "\n\n    Message : " + str(content) + "\n[[===============================]]")
            # await message.chanLogs.send(707643584354189342, "[[===============================]]\n" + "   Membre : " + str(author) + "\n\n    Message : " + str(content) + "\n[[===============================]]")
            with open('logs.txt', 'a') as logs_test:
                logs_test.write(str(author) + " a dit : " + str(content) + "\n------------\n\n")
                logs_test.close()
            
            chanLogs = bot.get_channel(707643584354189342)
            await chanLogs.send(content="```css\n- Réponse au Test\n[[===============================]]\n" + "    Membre : " + str(author) + "\n\n    Message : " + str(content) + "\n[[===============================]]\n```")

            if contentLw == "severus rogue" or contentLw == "severus" or contentLw == "rogue" or contentLw == "professeur rogue":
                await chanLogs.send(content="|-------**" + str(author) + "** a réussi le Test !-------|")
                await author.add_roles(role)

            else:
                await message.channel.send("Faux !", delete_after=4)
    else:
        await bot.process_commands(message)
    
@bot.command()
async def enterTest(ctx):
    await ctx.message.delete()
    await ctx.send("Bienvenue Moldus ! Si tu veux rentrer dans le monde des sorciers, cela ne seras pas si simple !\nRéponds à cette énigme et tu ouvriras le passage, au bout de 3 échecs, tu pourras demander un indice. **Bonne chance à toi ! ^_^**")
    embed = discord.Embed(title="Qui a dit cette phrase culte ?", description="Ouvrez vos livres page 394.", color = 0x09bbff)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def logs(ctx):
    with open('logs.txt', 'r') as read_logs:
        logs = read_logs.read()
        read_logs.close()

    reportNbr = 0

    if len(logs) < 1994:
        await ctx.send("```" + logs + "```")
    elif len(logs) >= 1994 and len(logs) <= 3994:
        reportNbr = len(logs)
        logs1 = logs[0:1994]
        logs2 = logs[1995:reportNbr]
        print("Report Nbr : " + str(reportNbr))
        print(len(logs1))
        print(len(logs2))
        await ctx.send("```" + logs1 + "```")
        await ctx.send("```" + logs2 + "```")

    elif len(logs) > 3994 and len(logs) <= 5994:
        reportNbr = len(logs)
        logs1 = logs[0:1994]
        logs2 = logs[1995:3989]
        logs3 = logs[3990:reportNbr]
        await ctx.send("```" + logs1 + "```")
        await ctx.send("```" + logs2 + "```")
        await ctx.send("```" + logs3 + "```")

    else:
        with open('logs.txt', 'r') as fp:
            await ctx.send("Fichier trop volumineux, voici les logs.txt :", file=File(fp, 'logs.txt'))

@logs.error
async def logs_error(ctx, error):
    print(error)
    await ctx.send("Vous n'avez pas les permissions de consulter les logs !")

bot.run(token)
