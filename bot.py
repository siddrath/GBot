import discord
import aiohttp
import datetime
import inspect
import os
import io
import re
import asyncio
import random
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont

bot = commands.Bot(description='BAsics can do a lot more.....', command_prefix=commands.when_mentioned_or('f!'))


class BAsics():

@bot.command(aliases=['cmds'])
async def commands(self, ctx):
    member = ctx.author
    embed = discord.Embed(title="Prefix", colour=discord.Colour.dark_blue(), description="G.")
    embed.add_field(name='Commands', value='gbot \nserverinfo \nuserinfo \nhelp \njoined_at \nstats \nping \ninvme \navatar \npoll \nvote \nbug_report \nfeedback \nbbff')
    embed.add_field(name='Admin/Mod Commands',value='ban \nkick \npurge \nswarn - soft warn \nwarn - reg. warn \n add_role \nmute \nunmute')
    await ctx.send ('Check your :regional_indicator_d: :regional_indicator_m:')
    await member.send(embed=embed)


@bot.command()
async def gbot(self, ctx):
    embed = discord.Embed(title="G Bot", colour=discord.Colour.dark_blue(),description="Created by: <@293800689266851850>", inline=False)
    embed.set_thumbnail(url=f'''{bot.user.avatar_url}''')
    embed.add_field(name='Contributor(s)', value="ir3#3333 \n------------ \nGarry#2508", inline=False)
    embed.add_field(name='Version', value="1.0.0 [ALPHA]")
    embed.set_footer(text = "Made with python 3.6.6", icon_url = 'https://cdn.discordapp.com/emojis/490607334876381204.png?v=1')
    await ctx.send(embed=embed)


@bot.command()
async def serverinfo(self, ctx):
    ': Get the server info'
    guild = ctx.guild
    embed = discord.Embed(title=f'''{guild}''', colour=discord.Colour.dark_blue(), description='More Info Below',
                          timestamp=datetime.datetime.utcnow())
    embed.set_thumbnail(url=f'''{guild.icon_url}''')
    embed.add_field(name='Server Created At :', value=f'''  {guild.created_at}''', inline=False)
    embed.add_field(name='Created by :', value=f'''{guild.owner}''', inline=False)
    embed.add_field(name='Region :', value=f'''  {guild.region}''', inline=False)
    embed.add_field(name='Server ID :', value=f'''{guild.id}''', inline=False)
    embed.add_field(name='Server Members :', value=f'''  {len(guild.members)}''', inline=False)
    embed.add_field(name='Online Members :',
                    value=f'''{len([I for I in guild.members if I.status is discord.Status.online])}''', inline=False)
    embed.add_field(name='Server Channel :', value=f'''  {len(guild.channels)}''', inline=False)
    await ctx.send(embed=embed)


@bot.command(aliases=['user', 'member', 'memberinfo',])
async def userinfo(self, ctx, member: discord.Member = None):
    name = "user",
    aliases = 'member', 'memberinfo', 'userinfo'
    if member is None:
        member = ctx.author

    e = discord.Embed(
        title=f"User: {member.name}", colour=discord.Colour.blue(),
        description=f"This is all the information I could find on {member.name}...",
    )
    e.set_thumbnail(
        url=member.avatar_url_as(static_format="png")
    )
    e.add_field(
        name="Name",
        value=member.name
    )
    e.add_field(
        name="Discriminator",
        value=f"#{member.discriminator}"
    )
    e.add_field(
        name="ID",
        value=str(member.id)
    )
    e.add_field(
        name="Bot",
        value=str(member.bot).capitalize()
    )
    e.add_field(
        name="Highest Role",
        value=member.top_role.mention
    )
    e.add_field(
        name="Join Position",
        value=f"#{sorted(member.guild.members, key=lambda m: m.joined_at).index(member) + 1}"
    )
    e.add_field(
        name="Created Account",
        value=member.created_at.strftime("%c")
    )
    e.add_field(
        name="Joined This Server",
        value=member.joined_at.strftime("%c")
    )
    e.add_field(
        name="Roles",
        value=f"{len(member.roles) - 1} Roles: {', '.join([r.mention for r in member.roles if not r.is_default()])}"
    )
    await ctx.send(embed=e)

#@bot.command()
#async def help(self, ctx):
    #embed=discord.Embed(title='So, you need help?', colour=discord.Colour.red(), description='[Support Discord](https://discord.gg/uHqmhgf)')
    #embed.add_field(name='-----------', value='[Website](https://gbot.bubbleapps.io)')
    #await ctx.send(embed=embed)

@bot.command()
async def stats(self, ctx):
        ''': Get the info about my servers'''
        total = sum(1 for m in set(ctx.bot.get_all_members()) if m.status != discord.Status.offline)
        embed = discord.Embed(title=f'''Count''', colour=discord.Colour.dark_purple(),description=f'''I am in **{len(bot.guilds)}** servers \nI am used by **{len(bot.users)}** users \nI am currently entertaining **{total}** users''')
        #markdown = ['![Discord Bots](https://discordbots.org/api/widget/493470893331447820.svg)](https://discordbots.org/bot/493470893331447820']
        embed.set_thumbnail(url=f'''{bot.user.avatar_url}''')
        await ctx.send(embed=embed)
        #await ctx.send(f'''{markdown}''')

@bot.command(pass_context=True)
async def joined_at(self, ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
        em = discord.Embed(title='Member', colour=discord.Colour.dark_red(),
                            description=f'''{member} joined at {member.joined_at}''', timestamp=datetime.datetime.utcnow(), inline=False)
        em.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=em)

@bot.command()
async def ping(self, ctx):
        ': Check your connection '
        t1 = ctx.message.created_at
        m = await ctx.send('**Pong!**')
        time = (m.created_at - t1).total_seconds() * 1000
        await m.edit(content='**Pong! Took: {}ms**'.format(int(time)))

@bot.command()
async def perms(self, ctx, user: discord.Member = None):
        ': Find what you can do on this server'
        user = ctx.message.author if user is None else user
        if not user:
            user = ctx.author
        mess = []
        for i in user.guild_permissions:
            if i[1]:
                mess.append("\u2705 {}".format(i[0]))
            else:
                mess.append("\u274C {}".format(i[0]))
        embed = discord.Embed(title = f'''{user.name} 's permissions in the server are: ''',description ="\n".join(mess), color = discord.Colour.dark_purple())
        await ctx.send(embed=embed)

@bot.command()
async def invme(self, ctx):
    embed=discord.Embed (title="So you want me huh?", colour=discord.Colour.dark_blue(), description='[Invite me](https://discordapp.com/api/oauth2/authorize?client_id=493470893331447820&scope=bot)')
    await ctx.send (embed=embed)

@bot.command(pass_context=True)
async def avatar(self, ctx, user: discord.Member = None):
        """: Check AVATARS"""
        user = user or ctx.message.author
        embed = discord.Embed(title=f'''{user.name}'s Avatar''', description=f'''{user.name} looks like.....''',color=discord.Colour.dark_purple())
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)

@bot.command()
async def poll(self, ctx, *, poll_message):
        embed = discord.Embed(title=f'''{ctx.author}'s new poll''', colour=discord.Colour.dark_blue(), description=poll_message)
        try:
            await ctx.message.delete()
        except:
            pass
        msg = await ctx.send(embed=embed)        
        try:
            await msg.add_reaction("\N{THUMBS UP SIGN}")
            await msg.add_reaction("\N{THUMBS DOWN SIGN}")
        except:
            await msg.delete()
            await ctx.send("Make sure i can add reactions to the poll")

@bot.command()
async def vote(self, ctx):
    embed = discord.Embed(title='Vote for me!', colour=discord.Colour.blue(), description='[Vote Here](https://discordbots.org/bot/493470893331447820/vote)')
    embed.set_thumbnail(url=f'''{bot.user.avatar_url}''')
    embed.set_footer(text='Thanks for considering voting! - Gavyn S. ✓ᵛᵉʳᶦᶠᶦᵉᵈ#0981')
    await ctx.send(embed=embed)

@bot.command()
async def feedback(self, ctx, * , feedback):
    channel = bot.get_channel(515220018997231676)
    embed = discord.Embed(title="Feedback Submission :robot:", colour=discord.Colour.red(), description=f'''Submitted by- {ctx.author}''')
    embed.add_field(name="Feedback", value=feedback, inline=False)
    embed.set_footer(text=f"From {ctx.guild.name} ({ctx.guild.id})")
    await channel.send(embed=embed)
    await ctx.send("Your Feedback Has Been Submitted")

@bot.command()
async def bug_report(self, ctx, * , feedback):
    channel = bot.get_channel(515220018997231676)
    embed = discord.Embed(title="Bug Submission :robot:", colour=discord.Colour.red(), description=f'''Submitted by- {ctx.author}''')
    embed.add_field(name="Feedback", value=feedback, inline=False)
    embed.set_footer(text=f"From {ctx.guild.name} ({ctx.guild.id})")
    await channel.send(embed=embed)
    await ctx.send("Your Feedback Has Been Submitted")



@bot.command()
async def servers(self, ctx):
    a = []
    for i in bot.guilds:
        a.append(i.name)
        await ctx.send(", ".join(a))


@bot.command()
async def bbff(self, ctx):
    embed=discord.Embed(title='My Best Bot Friends Forever', colour=discord.Colour.red(), description='Add them to your server!')
    embed.add_field(name='PewDiePie#7718', value='[Invite Here](https://discordapp.com/oauth2/authorize?client_id=508143906811019269&scope=bot&permissions=2146958847)')
    embed.add_field(name='T-Series#7576', value='[Invite Here](https://discordapp.com/oauth2/authorize?client_id=500868806776979462&scope=bot&permissions=72710)')
    embed.add_field(name='Touka#9248', value='[Invite Here](https://discordapp.com/oauth2/authorize?client_id=486093523024609292&scope=bot&permissions=2146958591)')
    embed.add_field(name='Fusion#2584', value='[Invite Here](https://discordapp.com/api/oauth2/authorize?client_id=469204895946244106&permissions=8&scope=bot)')
    embed.set_footer(text='Sincerely, Gavyn S. ✓ᵛᵉʳᶦᶠᶦᵉᵈ#0981', icon_url = 'https://cdn.discordapp.com/emojis/519688994120794132.png?v=1')
    await ctx.send (embed=embed)



class BAdmin():

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason):
        ': Kick the member if you have authority '
        if ctx.author.permissions_in(ctx.channel).kick_members:
            if reason is None:
                await member.send(f'''You have been kicked by {ctx.author.name} from {ctx.guild.name} due to __No reason given__ ''')
                em = discord.Embed(title='Kicked', colour=discord.Colour.dark_red(),
                                description=f'''{member} has been kicked''', timestamp= datetime.datetime.utcnow())
                em.set_thumbnail(url=member.avatar_url)
                em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
                em.add_field(name='Culpret', value=f'''{member}''', inline=False)
                em.add_field(name='Reason for kicking', value=f'''_No reason provided_''', inline=False)
                await ctx.send(embed=em)
                await member.kick()
            else:
                await member.send(f'''You have been kicked by {ctx.author.name} from {ctx.guild.name} due to {reason} ''')
                em = discord.Embed(title='Kicked', colour=discord.Colour.dark_red(),
                                   description=f'''{member} has been kicked''', timestamp=datetime.datetime.utcnow())
                em.set_thumbnail(url=member.avatar_url)
                em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
                em.add_field(name='Culprit', value=f'''{member}''', inline=False)
                em.add_field(name='Reason for kicking', value=f'''{reason}''', inline=False)
                await ctx.send(embed=em)
                await member.kick()
        else:
            message = await ctx.send(f'''{ctx.author.mention} you are not eligible for this''', delete_after= 3)
            await message.add_reaction('\u2623')

    @commands.command()
    async def perms(self, ctx, user: discord.Member = None):
        ': Find what you can do on this server'
        user = ctx.message.author if user is None else user
        if not user:
            user = ctx.author
        mess = []
        for i in user.guild_permissions:
            if i[1]:
                mess.append("\u2705 {}".format(i[0]))
            else:
                mess.append("\u274C {}".format(i[0]))
        embed = discord.Embed(title = f'''{user.name} 's permissions in the server are: ''',description ="\n".join(mess), color = discord.Colour.dark_purple())
        await ctx.send(embed=embed)

    @commands.command()
    async def purge(self, ctx, limit: int):
        ': Delete messages'
        if ctx.author.permissions_in(ctx.channel).manage_messages:
            await ctx.channel.purge(limit=limit)
            await ctx.send(f'''Deleted {limit} message(s)''')
        else:
            return

    @commands.command()
    async def prune(self, ctx, days: int):
        ': Prune the inactive members'
        if ctx.author.permissions_in(ctx.channel).ban_members:
         await ctx.guild.prune_members(days=days)
        else:
            await ctx.send(f'''{ctx.author.mention} you are not Eligible for this''',delete_after = 3)

    @commands.command()
    async def estimatedprune(self, ctx, days: int):
        ': Estimate the inactive members to prune'
        await ctx.send(await ctx.guild.estimate_pruned_members(days=days))

    @commands.command()
    async def warn(self, ctx, member: discord.Member , *, reason = None):
        ''': SoftWarn a person'''
        if ctx.author.permissions_in(ctx.channel).kick_members or ctx.author.permissions_in(ctx.channel).manage_messages:
            if reason is None:
                await ctx.send(f'''{ctx.author.mention} \n ```A reason needed to warn``` ''')
            else:
                embed = discord.Embed(title='Warning', colour=discord.Colour.gold(),
                                      description =f'''You have been warned by {ctx.author.name} for {reason}''', timestamp=datetime.datetime.utcnow())
                await member.send(embed=embed)
                em = discord.Embed(title='Warned', colour=discord.Colour.gold(),
                                   description=f'''{member} has been warned''', timestamp=datetime.datetime.utcnow())
                em.set_thumbnail(url=member.avatar_url)
                em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
                em.add_field(name='Culprit', value=f'''{member}''', inline=False)
                em.add_field(name='Reason for warning', value=f'''{reason}''', inline=False)
                await ctx.send(embed=em)
        else:
            await ctx.send(f'''{ctx.author.mention} you aren't eligible for this''', delete_after= 3)

    @commands.command()
    async def swarn(self, ctx, member: discord.Member , *, reason = None):
        ': Warn a person seriously'
        if ctx.author.permissions_in(ctx.channel).kick_members or ctx.author.permissions_in(ctx.channel).manage_messages:
            if reason is None:
                await ctx.send(f'''{ctx.author.mention} \n ```A serious reason needed to warn``` ''')
            else:
                embed = discord.Embed(title='Warning', colour=discord.Colour.red(),
                                      description=f'''You have been warned by {ctx.author.name} for {reason}''', timestamp=datetime.datetime.utcnow())
                await member.send(embed=embed)
                em = discord.Embed(title= 'Seriously Warned', colour= discord.Colour.red(),
                                   description=f'''{member} has been warned''', timestamp=datetime.datetime.utcnow() )
                em.set_thumbnail(url=member.avatar_url)
                em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
                em.add_field(name='Culprit', value=f'''{member}''', inline=False)
                em.add_field(name='Reason for warning', value=f'''{reason}''', inline=False)
                await ctx.send(embed=em)
        else:
            await ctx.send(f'''{ctx.author.mention} you aren't eligible for this''', delete_after=3)


@bot.command(hidden = True)
async def code(ctx, command):
        ''': getting the code for command'''

        a = inspect.getsource(bot.get_command(command).callback)
        embed = discord.Embed(title='Code', description="```py\n"+a+"```",color=discord.Colour.dark_purple())
        embed.set_thumbnail(url='https://scontent.fdel3-1.fna.fbcdn.net/v/t1.0-9/20155639_1952222755056855_6450365686627691750_n.png?oh=0b2c4ecd1409396b05f71c31dd07dd2d&oe=5AE7B998')
        await ctx.send(embed=embed)


@bot.command(hidden=True)
async def reload(ctx, extension):
    if ctx.author.id == 392337139309871106:
       try:
            bot.unload_extension(extension)
            bot.load_extension(extension)
            embed = discord.Embed(title="Reload", description=f'''Reloaded {extension}''',
                                  color=discord.Colour.dark_purple())
            await ctx.send(embed=embed)
       except ModuleNotFoundError:
            await ctx.send("```No such extention exists```")
    else:
        await ctx.send("```You can't do it buddy you better know it```")

    
@bot.event
async def on_command_error(ctx, err):
    if ctx.guild.id == 394087011641851905:
        await ctx.channel.send(f'''```py\n{type(err).__name__}: {err!s}```''')
    else:
        return


@bot.event
async def on_member_join(member):
        if member.guild.id == 453472827526479874:
            channel = member.guild.get_channel(485835315194363925)
            await channel.edit(name=f'Member Count: {len(member.guild.members)}')


@bot.event
async def on_member_remove(member):
    if member.guild.id == 453472827526479874:
        channel = member.guild.get_channel(485835315194363925)
        await channel.edit(name=f'Member Count: {len(member.guild.members)}')


@bot.event
async def on_message(msg):
    if 'firebasic' in msg.content.lower():
        await msg.channel.send('Yup I am here!!')
    await bot.process_commands(msg)




@bot.event
async def on_ready():
    bot.load_extension("fun")
    bot.load_extension("search")
    bot.load_extension('ExampleRepl')
    options = ('help via G.help', 'to Gavyn S. ✓ᵛᵉʳᶦᶠᶦᵉᵈ#0981', f'on {len(bot.guilds)} servers')
    while True:
        await bot.change_presence(activity=discord.Streaming(name=random.choice(options), url='https://www.twitch.tv/gavynlamar05'))
        await asyncio.sleep(10)


bot.add_cog(BAdmin())
bot.add_cog(BAsics())
bot.run(os.getenv('TOKEN'))
