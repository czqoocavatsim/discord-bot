import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print ("Starting up")
    activity = discord.Activity(name="the HF radios", type=discord.ActivityType.listening)
    await bot.change_presence(activity=activity)

@bot.command()
async def ping(ctx):
    await ctx.send(":ping_pong: Ping, pong! {0}ms".format(round(bot.latency, 1)))

@bot.command(hidden=True)
async def send_rules_resources(ctx):
    embed1 = discord.Embed(title="**Rules**", colour=discord.Colour(0x80c9))

    embed1.add_field(inline=False, name="Discord Terms of Service & Community Guidelines", value="All members must follow Discord's Community Guidelines and Terms of Service at all times.\nToS — https://discordapp.com/terms\nGuidelines — https://discordapp.com/guidelines")
    embed1.add_field(inline=False, name="VATSIM Code of Conduct Applies", value="The VATSIM CoC applies at all times on all Gander Ocenaic communication platforms.\nhttps://www.vatsim.net/documents/code-of-conduct")
    embed1.add_field(inline=False, name="Always show respect and common decency to fellow members", value="We aim to be a community where all people can feel they belong. Therefore, we ask that you show respect to each other at all times. This ties into Article A1 of the Code of Conduct.")
    embed1.add_field(inline=False, name="Server invites", value="We ask that you not send invites to Discord servers unrelated to VATSIM with the permission of a staff member. Invites to servers related to the VATSIM community are permitted. Do not send **ANY** invites via DMs unless the person requests it.")
    embed1.add_field(inline=False, name="Spam, including images, text, or emotes.", value="Do not send spam in the server, including images, text, or emotes. ")
    embed1.add_field(inline=False, name="Enforcement", value="These rules are enforced by the <@&482816721280040964> of Gander Oceanic. If required, we may refer behaviour to a Network Supervisor.")

    await ctx.send(embed=embed1)

    embed2 = discord.Embed(title="**Resources**", colour=discord.Colour(0x80c9))

    embed2.add_field(inline=False, name="Pilot Tools", value="Check out pilot tools including oceanic clearance/position report assists, natTRAK, and a map of current NAT tracks here:\nhttps://ganderoceanic.com/pilots/")
    embed2.add_field(inline=False, name="Policies", value="Find all Gander Ocenaic policies here, including currency policies for controllers:\nhttps://ganderoceanic.com/policies")
    embed2.add_field(inline=False, name="Feedback", value="Have some feedback on how we're doing? Let us know here:\nhttps://vats.im/czqofeedback")

    await ctx.send(embed=embed2)

    embed3 = discord.Embed(title="**Controller ATIS Template**", colour=discord.Colour(0x80c9))
    embed3.add_field(inline=False, name="2.1.5 of the Controller Policy", value="```\nLINE 2: Gander (or Shanwick) Radio\nLINE 3: Pilot resources: vats.im/czqotools\nLINE 4: Have some feedback? We’d love to hear it! vats.im/czqofeedback\n\nA controller may choose to add additional information on line 2, to the right of the callsign.\nExample: “Gander Radio | Welcome to the OCA!”\n```")

    await ctx.send(embed=embed3)

    embed4 = discord.Embed(title="**Approved Frequencies and Logon Positions**", colour=discord.Colour(0x80c9))
    embed4.set_image(url="https://cdn.discordapp.com/attachments/681071305394749458/752813169470341140/unknown.png")

    await ctx.send(embed=embed4)

bot.run(TOKEN)