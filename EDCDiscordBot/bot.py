import discord
from discord.ext import commands
from discord.utils import get
import pandas as pd
from helper_functions import make_embed

df = pd.read_csv('teams1.csv')
r = len(df)
c = len(df.columns)
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('creating channels'))
    print("Bot is ready.")


list_teams = ['team1', 'team2']


@client.command()
async def channel(ctx):
    guild = ctx.message.guild.id
    guild_name = ctx.guild.name
    print(guild)
    print(guild_name)
    category = discord.utils.get(ctx.guild.categories, id = 835355346330452008)
    print(category)
    for i in range(r):
        await ctx.guild.create_role(name=df.iloc[i, 0])
        await ctx.guild.create_text_channel(df.iloc[i, 0], category=category)
        await ctx.guild.create_voice_channel(df.iloc[i, 0], category=category)


@client.command()
@commands.has_role("Moderator")  # This must be exactly the name of the appropriate role
async def addrole(ctx, user: discord.Member, role: discord.Role):
    print(type(user))
    print(user)
    await user.add_roles(role)
    emx = make_embed(text=f"{user.mention} has been given the role {role.name}")
    await ctx.send(embed=emx)


@client.command()
@commands.has_role("Moderator")
async def autorole(ctx):
    guild = client.get_guild(830841986780889128)
    for i in range(r):
        role = df.iloc[i, 0]
        roles = get(ctx.guild.roles, name=role)
        for j in range(1, c):
            name = df.iloc[i, j]
            if type(name) == float:
                continue
            else:
                member = guild.get_member_named(name)
                if member == None:
                    emb = make_embed(text=f"{name} was not found from team {roles.name}", color=discord.Colour.red())
                    await ctx.send(embed=emb)
                else:
                    await member.add_roles(roles)
                    emx = make_embed(text=f"{member.mention} has been given the role {roles.name}")
                    print(member.name)
                    await ctx.send(embed=emx)


client.run('ODIyMTg4NzU2ODUzMDYzNzAw.YFOo8w.emTb4DNWgob7eLlxtsfD9KlAhnU')
