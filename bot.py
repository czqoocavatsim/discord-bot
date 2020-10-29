import discord
from discord.ext import commands
from dotenv import load_dotenv
import os, requests, json
from datetime import datetime
import math

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='czqo?')

@bot.event
async def on_ready():
    print ("Starting up")
    activity = discord.Activity(name="the HF radio", type=discord.ActivityType.listening)
    await bot.change_presence(activity=activity)
    channel = bot.get_channel(482860026831175690)
    await channel.send('Hello! Starting...')

@bot.command(hidden=True)
@commands.has_permissions(administrator=True)
async def send_rules_resources(ctx):
    embed1 = discord.Embed(title="**Rules**", colour=discord.Colour(0x80c9))

    embed1.add_field(inline=False, name="Discord Terms of Service & Community Guidelines", value="All members must follow Discord's Community Guidelines and Terms of Service at all times.\nToS — https://discordapp.com/terms\nGuidelines — https://discordapp.com/guidelines")
    embed1.add_field(inline=False, name="VATSIM Code of Conduct Applies", value="The VATSIM CoC applies at all times on all Gander Oceanic communication platforms.\nhttps://www.vatsim.net/documents/code-of-conduct")
    embed1.add_field(inline=False, name="Always show respect and common decency to fellow members", value="We aim to be a community where all people can feel they belong. Therefore, we ask that you show respect to each other at all times. This ties into Article A1 of the Code of Conduct.")
    embed1.add_field(inline=False, name="Server invites", value="We ask that you not send invites to Discord servers unrelated to VATSIM with the permission of a staff member. Invites to servers related to the VATSIM community are permitted. Do not send **ANY** invites via DMs unless the person requests it.")
    embed1.add_field(inline=False, name="Spam, including images, text, or emotes.", value="Do not send spam in the server, including images, text, or emotes. ")
    embed1.add_field(inline=False, name="Enforcement", value="These rules are enforced by the <@&482816721280040964> of Gander Oceanic. If required, we may refer behaviour to a Network Supervisor.")

    await ctx.send(embed=embed1)

    embed2 = discord.Embed(title="**Resources**", colour=discord.Colour(0x80c9))

    embed2.add_field(inline=False, name="Pilot Tools", value="Check out pilot tools including oceanic clearance/position report assists, natTRAK, and a map of current NAT tracks here:\nhttps://ganderoceanic.com/pilots/")
    embed2.add_field(inline=False, name="Policies", value="Find all Gander Oceanic policies here, including currency policies for controllers:\nhttps://ganderoceanic.com/policies")
    embed2.add_field(inline=False, name="Feedback", value="Have some feedback on how we're doing? Let us know here:\nhttps://vats.im/czqofeedback")

    await ctx.send(embed=embed2)

    embed3 = discord.Embed(title="**Controller ATIS Template**", colour=discord.Colour(0x80c9))
    embed3.add_field(inline=False, name="2.1.5 of the Controller Policy", value="```\nLINE 2: Gander (or Shanwick) Radio\nLINE 3: Pilot resources: vats.im/czqotools\nLINE 4: Have some feedback? We’d love to hear it! vats.im/czqofeedback\n\nA controller may choose to add additional information on line 2, to the right of the callsign.\nExample: “Gander Radio | Welcome to the OCA!”\n```")

    await ctx.send(embed=embed3)

    embed4 = discord.Embed(title="**Approved Frequencies and Logon Positions**", colour=discord.Colour(0x80c9))
    embed4.set_image(url="https://cdn.discordapp.com/attachments/681071305394749458/752813169470341140/unknown.png")

    await ctx.send(embed=embed4)


@bot.command(hidden=True)
@commands.has_permissions(administrator=True)
async def send_tim_hortons_msg(ctx):
    await ctx.send("Hey stranger! If you can see this message, then you haven't yet linked your discord account with Gander Oceanic. You can do so on your dashboard :grin:: https://ganderoceanic.com/dashboard")

@bot.command(hidden=True)
@commands.has_permissions(administrator=True)
async def admin_commands(ctx):
    embed = discord.Embed(title="**Admin Commands**", colour=discord.Colour(0x80c9))
    embed.add_field(inline=False, name="czqo?send_rules_resources", value="Posts rules+resources embeds")
    embed.add_field(inline=False, name="czqo?send_tim_hortons_msg", value="Sends #tim-hortons explanation message")

    await ctx.send(embed=embed)

@bot.command()
async def solocerts(ctx):
    waiting = await ctx.send("Working on it...")

    endpoint = os.getenv("SOLO_CERTS_ENDPOINT")
    response = requests.get(endpoint)

    if len(response.json()) == 0:
        await waiting.delete()
        await ctx.send("No solo certifications active")
        return

    embed = discord.Embed(title="**Solo Certifications**", colour=discord.Colour(0x80c9))

    for cert in response.json():
        embed.add_field(inline=False, name="**{0}**".format(cert['roster_member']['cid']), value="Expires {0}".format(cert['expires']))

    await waiting.delete()

    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    now = datetime.utcnow()

    nowTime = datetime.timestamp(now)
    reqTime = datetime.timestamp(ctx.message.created_at)
    
    ping = math.floor(nowTime - reqTime )* 1000
    await ctx.send("🏓Ping, pong!  {}ms".format(ping))

bot.run(TOKEN)