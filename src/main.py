from discord.ext import commands
import discord
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 231844878252769281  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command(name='name')
async def name(ctx):
    await ctx.send(ctx.message.author)

@bot.command(name='d6')
async def d6(ctx):
    await ctx.send(random.randint(1,6))

@bot.event
async def on_message(msg):
    if msg.author.bot:
        return
    if msg.content == "Salut tout le monde":
        await msg.channel.send("Salut tout seul " + msg.author.mention)

    await bot.process_commands(msg)

@bot.command(name='admin')
async def admin(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Admin")

    if role is None:
        role = await ctx.guild.create_role(name="Admin", permissions=discord.Permissions(8))

    await member.add_roles(role)

@bot.command(name='ban')
async def ban(ctx, member: discord.Member, reason=""):
    if reason == "":
        reasons = ["Parce que c'est comme ça", "Parce que j'en ai envie", "Parce que je suis un bot et que je peux le faire", "Parce que je suis un bot et que je suis plus fort que toi"]
        reason = random.choice(reasons)

    await ctx.send("Banni " + member.mention + " pour " + reason)
    await member.ban(reason=reason)

token = "<YOUR_TOKEN>"
bot.run(token)  # Starts the bot