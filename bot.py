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

bot = commands.Bot(description='GBot...', command_prefix=commands.when_mentioned_or('G.'))


class Basics():


    @commands.command()
    async def ping(self, ctx):
        ': Check your connection '
        t1 = ctx.message.created_at
        m = await ctx.send('**Pong!**')
        time = (m.created_at - t1).total_seconds() * 1000
        await m.edit(content='**Pong! Took: {}ms**'.format(int(time)))

    @commands.command(pass_contex=True)
    async def invite(self, ctx):
        ': Invite me '
        embed=discord.Embed (title="So you want me huh?", colour=discord.Colour.dark_blue(), description='[Invite me](https://discordapp.com/api/oauth2/authorize?client_id=493470893331447820&scope=bot)')
        await ctx.send(embed=embed)

    @commands.command()
    async def uptime(self,ctx):
        res = os.popen("uptime").read()
        matches = re.findall(r"up (\d+) days, (\d+):(\d+)", res)
        time = matches[0]
        fmtime = "{0[0]} days, {0[1]} hours {0[2]} minutes".format(time)
        await ctx.send(f'''```py\n{fmtime}```''')

    @commands.command()
    async def serverinfo(self, ctx):
        ': Get the server info'
        guild = ctx.guild
        embed = discord.Embed(title=f'''{guild}''', colour=discord.Colour.dark_purple(), description='More Info Below', timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=f'''{guild.icon_url}''')
        embed.add_field(name='Server Created At :', value=f'''  {guild.created_at}''', inline=False)
        embed.add_field(name='Created by :', value=f'''{guild.owner.mention}''', inline=False)
        embed.add_field(name='Region :', value=f'''  {guild.region}''', inline=False)
        embed.add_field(name='Server ID :', value=f'''{guild.id}''', inline=False)
        embed.add_field(name='Server Members :', value=f'''  {len(guild.members)}''', inline=False)
        embed.add_field(name='Online Members :',
                        value=f'''{len([I for I in guild.members if I.status is discord.Status.online])}''',inline=False)
        embed.add_field(name='Server Channel :', value=f'''  {len(guild.channels)}''', inline=False)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def avatar(self, ctx, user: discord.Member = None):
        """: Check AVATARS"""
        user = user or ctx.message.author
        embed = discord.Embed(title=f'''{user.name}'s Avatar''', description=f'''{user.name} looks like.....''',color=discord.Colour.dark_purple())
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def stats(self, ctx):
        ''': Get the info about my servers'''
        total = sum(1 for m in set(ctx.bot.get_all_members()) if m.status != discord.Status.offline)
        embed = discord.Embed(title=f'''Count''', colour=discord.Colour.dark_purple(),description=f'''I am in **{len(bot.guilds)}** servers \nI am used by **{len(bot.users)}** users \nI am currently entertaining **{total}** users''')

        embed.set_thumbnail(url=f'''{bot.user.avatar_url}''')
        await ctx.send(embed=embed)
   

    @commands.command()
    async def wanted(self, ctx, member: discord.Member = None):
        ''': Hunt someone'''
        member = member or ctx.message.author
        x = Image.open("pngs/Wanted.png")
        x.load()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(member.avatar_url_as(format='png')) as r:
                b = io.BytesIO(await r.read())
        x1 = Image.open(b)
        x3 = x.resize((400, 600))
        x3.paste(x1.resize((300, 250)), (50, 160))
        x3.save("wanted.png")
        await ctx.send(file=discord.File("wanted.png"))
        os.system("rm wanted.png")

    @commands.command()
    async def shit(self,ctx, member: discord.Member):
        ''': Show em how shitty they are'''
        x = Image.open("pngs/shit.png")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(member.avatar_url_as(format='png')) as r:
                b = io.BytesIO(await r.read())
        # open the pic and give it an alpha channel so it's transparent
        im1 = Image.open(b).convert('RGBA')
        im4 = im1.resize((120, 200))
        # rotate it and expand it's canvas so the corners don't get cut off:
        im2 = im4.rotate(-45, expand=1)

        # note the second appearance of im2, that's necessary to paste without a bg
        x.paste(im2, (200, 655), im2)
        x.save("SHIT.png")
        await ctx.send(file=discord.File("SHIT.png"))
        os.system("rm SHIT.png")
        
    @commands.command(pass_context=True, aliases=['whois'])
    async def userinfo(ctx, member: discord.Member = None):

        name="user",
        if member is None:
            member = ctx.author

        e = discord.Embed(title=f"User: {member.name}",description=f"This is all the information I could find on {member.name}...",)
        e.set_thumbnail(url=member.avatar_url_as(static_format="png"))
        e.add_field(name="Name",value=member.name)
        e.add_field(name="Discriminator",value=f"#{member.discriminator}")
        e.add_field(name="ID",value=str(member.id))
        e.add_field(name="Bot",value=str(member.bot).capitalize())
        e.add_field(name="Highest Role",value=member.top_role.mention)
        e.add_field(name="Join Position",value=f"#{sorted(member.guild.members, key=lambda m: m.joined_at).index(member) + 1}")
        e.add_field(name="Created Account",value=member.created_at.strftime("%c"))
        e.add_field(name="Joined This Server",value=member.joined_at.strftime("%c"))
        e.add_field(name="Roles",value=f"{len(member.roles)-1} Roles: {', '.join([r.mention for r in member.roles if not r.is_default()])}")
        await ctx.send(embed=e)
        



class BAmath():

    @commands.command()
    async def fact(self, ctx, num: int):
        ': Get factorial of any number '
        if num < 0:
            await ctx.send('Sorry, factorial does not exist for negative numbers')
        elif num == 0:
            await ctx.send('The factorial of 0 is 1')
        else:
            from math import factorial
            await ctx.send(f'''The factorial of {num} is : ```{factorial(num)}```''')
    @commands.command()
    async def add(self, ctx, num: int, num2: int):
        ': Add two numbers'
        await ctx.send(num + num2)

    @commands.command()
    async def factor(self, ctx, num: int):
        ': Find prime factors '
        await ctx.send('Factors are:')
        i = 1
        while i <= num:
            k = 0
            if (num % i) == 0:
                j = 1
                while j <= i:
                    if (i % j) == 0:
                        k = k + 1
                    j = j + 1
                if k == 2:
                    await ctx.send('`1`')
                    await ctx.send(f'''`{i}`''')
            i = i + 1


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
    if ctx.author.id == 293800689266851850:
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
bot.add_cog(BAmath())
bot.add_cog(Basics())
bot.run(os.getenv('TOKEN'))
