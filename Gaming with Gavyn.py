import discord
from discord.ext import commands
from discord import Game
import datetime
import time
import traceback
import sys
import aiohttp
import subprocess



bot = commands.Bot(command_prefix="G.")
bot.remove_command('help')

TOKEN = "NDkzNDcwODkzMzMxNDQ3ODIw.DtSgag.0F8JwjI0DrU34eCIyNIIEFd9v8o"



@bot.event
async def on_ready():
    print("logged in as")
    print(client.user.name)
    print("----------")
    

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Made by: Gavyn S.✓ᵛᵉʳᶦᶠᶦᵉᵈ#0981"))


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd)

#@bot.event
#async def on_member_join(ctx):
    #await ctx.send(f'''Welcome to {ctx.guild.name}!''')
        
            
#commands
    

@bot.command()
async def socialmedia(ctx):
    await ctx.send("https://twitch.tv/gavynlamar05 \nhttps://www.instagram.com/gavynstanley25/ \nhttps://www.youtube.com/channel/UCefZJztrf4KmjeWt_8qk4kA?view_as=subscriber \nhttps://twitter.com/gavyn_stanley")


@bot.command()
async def commands(ctx):
    embed = discord.Embed(title="Prefix", colour=discord.Colour.dark_blue(), description="G.")
    embed.add_field(name='Commands', value='socialmedia \ngbot \nserverinfo \nowner \nllrp \nuserinfo \nusers \nhelp \n joined_at \nstats \nping \ninvme')
    embed.add_field(name='Admin/Mod Commands',value='ban \nkick \npurge \nswarn - soft warn \nwarn - reg. warn \n add_role \nmute \nunmute')
    await ctx.send(embed=embed)


@bot.command()
async def hi(ctx):
    await ctx.send("hi")


@bot.command()
async def llrp(ctx):
    await ctx.send("https://discord.gg/uy63CSm \nhttps://lifelinerp.com")


@bot.command()
async def gbot(ctx):
    embed = discord.Embed(title="GG Bot", colour=discord.Colour.dark_blue(),description="Created by: Gavyn S. ✓ᵛᵉʳᶦᶠᶦᵉᵈ#0981")
    embed.add_field(name='Contributor(s)', value="<@217462890364403712> | <@411496838550781972>")
    embed.add_field(name='Version', value="0.1.0 [Pre-ALPHA]")
    await ctx.send(embed=embed)


@bot.command()
async def ban(ctx, member: discord.Member, *, reason):
    if ctx.author.permissions_in(ctx.channel).ban_members:
        if reason is None:
            await member.send(f'''You have been banned by {ctx.author.name} from {ctx.guild.name} due to __No reason given__ ''')
            em = discord.Embed(title='Banned', colour=discord.Colour.dark_red(),
                            description=f'''{member} has been banned''', timestamp= datetime.datetime.utcnow())
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
            em.add_field(name='Culpret', value=f'''{member}''', inline=False)
            em.add_field(name='Reason for Banning', value=f'''_No reason provided_''', inline=False)
            await ctx.send(embed=em)
            await member.ban()
        else:
            await member.send(f'''You have been Banned by {ctx.author.name} from {ctx.guild.name} due to {reason} ''')
            em = discord.Embed(title='Banned', colour=discord.Colour.dark_red(),
                                description=f'''{member} has been banned''', timestamp=datetime.datetime.utcnow())
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
            em.add_field(name='Culprit', value=f'''{member}''', inline=False)
            em.add_field(name='Reason for Banning', value=f'''{reason}''', inline=False)
            await ctx.send(embed=em)
            await member.ban()
    else:
        message = await ctx.send(f'''{ctx.author.mention} you are not eligible for this''', delete_after= 3)
        await message.add_reaction('\u2623') 


@bot.command()
async def kick(ctx, member: discord.Member, *, reason):
    ': Kick the member if you have authority '
    if ctx.author.guild_permissions.administrator:
        if reason is None:
            await member.send(
                f'''You have been kicked by {ctx.author.name} from {ctx.guild.name} due to __No reason given__ ''')
            em = discord.Embed(title='Kicked', colour=discord.Colour.dark_blue(),
                               description=f'''{member} has been kicked''', timestamp=datetime.datetime.utcnow())
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
        message = await ctx.send(f'''{ctx.author.mention} you are not eligible for this''', delete_after=3)
        await message.add_reaction('\u2623')


@bot.command()
async def purge(ctx, limit: int):
    ': Delete messages'
    if ctx.author.permissions_in(ctx.channel).manage_messages:
        await ctx.channel.purge(limit=limit)
        await ctx.send(f'''Deleted {limit} message(s)''')
    else:
        return


@bot.command()
async def serverinfo(ctx):
    ': Get the server info'
    guild = ctx.guild
    embed = discord.Embed(title=f'''{guild}''', colour=discord.Colour.dark_blue(), description='More Info Below',
                          timestamp=datetime.datetime.utcnow())
    embed.set_thumbnail(url=f'''{guild.icon_url}''')
    embed.add_field(name='Server Created At :', value=f'''  {guild.created_at}''', inline=False)
    embed.add_field(name='Created by :', value=f'''{guild.owner.mention}''', inline=False)
    embed.add_field(name='Region :', value=f'''  {guild.region}''', inline=False)
    embed.add_field(name='Server ID :', value=f'''{guild.id}''', inline=False)
    embed.add_field(name='Server Members :', value=f'''  {len(guild.members)}''', inline=False)
    embed.add_field(name='Online Members :',
                    value=f'''{len([I for I in guild.members if I.status is discord.Status.online])}''', inline=False)
    embed.add_field(name='Server Channel :', value=f'''  {len(guild.channels)}''', inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def owner(ctx):
    ': Name of my creator'
    await ctx.send('My owner is <@293800689266851850> ')
    await ctx.message.delete()


@bot.command()
async def warn(ctx, member: discord.Member, *, reason=None):
    ''': SoftWarn a person'''
    if ctx.author.guild_permissions.administrator:
        if reason is None:
            await ctx.send(f'''{ctx.author.mention} \n
A reason needed to warn
 ''')
        else:
            embed = discord.Embed(title='Warning', colour=discord.Colour.gold(),
                                  description=f'''You have been warned by {ctx.author.name} for {reason}''',
                                  timestamp=datetime.datetime.utcnow())
            await member.send(embed=embed)
            em = discord.Embed(title='Warned', colour=discord.Colour.gold(),
                               description=f'''{member} has been warned''', timestamp=datetime.datetime.utcnow())
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
            em.add_field(name='Culprit', value=f'''{member}''', inline=False)
            em.add_field(name='Reason for warning', value=f'''{reason}''', inline=False)
            await ctx.send(embed=em)
    else:
        await ctx.send(f'''{ctx.author.mention} you aren't eligible for this''', delete_after=3)


@bot.command()
async def swarn(ctx, member: discord.Member, *, reason=None):
    ': Warn a person seriously'
    if ctx.author.guild_permissions.administrator:
        if reason is None:
            await ctx.send(f'''{ctx.author.mention} \n
A serious reason needed to warn
 ''')
        else:
            embed = discord.Embed(title='Warning', colour=discord.Colour.red(),
                                  description=f'''You have been warned by {ctx.author.name} for {reason}''',
                                  timestamp=datetime.datetime.utcnow())
            await member.send(embed=embed)
            em = discord.Embed(title='Seriously Warned', colour=discord.Colour.red(),
                               description=f'''{member} has been warned''', timestamp=datetime.datetime.utcnow())
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
            em.add_field(name='Culprit', value=f'''{member}''', inline=False)
            em.add_field(name='Reason for warning', value=f'''{reason}''', inline=False)
            await ctx.send(embed=em)
    else:
        await ctx.send(f'''{ctx.author.mention} you aren't eligible for this''')


@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    name = "user",
    aliases = 'member', 'memberinfo', 'userinfo'
    if member is None:
        member = ctx.author

    e = discord.Embed(
        title=f"User: {member.name}", colour=discord.Colour.red(),
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


@bot.command()
async def add_role(ctx, member: discord.Member, role: discord.Role):
    if ctx.author.permissions_in(ctx.channel).kick_members or ctx.author.permissions_in(ctx.channel).manage_messages:
        await member.add_roles(role)

@bot.command()
async def help(ctx):
    embed=discord.Embed(title='So, you need help?', colour=discord.Colour.red(), description='[Discord Server](https://discord.gg/uHqmhgf)')
    await ctx.send(embed=embed)

@bot.command()
async def stats(ctx):
        ''': Get the info about my servers'''
        total = sum(1 for m in set(ctx.bot.get_all_members()) if m.status != discord.Status.offline)
        embed = discord.Embed(title=f'''Count''', colour=discord.Colour.dark_purple(),description=f'''I am in **{len(bot.guilds)}** servers \nI am used by **{len(bot.users)}** users \nI am currently entertaining **{total}** users''')

        embed.set_thumbnail(url=f'''{bot.user.avatar_url}''')
        await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def joined_at(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
        em = discord.Embed(title='Member', colour=discord.Colour.dark_red(),
                            description=f'''{member} joined at {member.joined_at}''', timestamp=datetime.datetime.utcnow(), inline=False)
        em.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=em)

@bot.command()
async def mute(ctx, user: discord.Member):
        'Mutes a user'
        try:
            if ctx.author.guild_permissions.administrator:
                role = discord.utils.get(ctx.guild.roles, name='Muted')
                await user.add_roles(role)
                await ctx.send('Muted {}'.format(user.name))
            else:
                await ctx.send('Permission Denied.')
        except KeyboardInterrupt:
            await ctx.send('User Not Found')

@bot.command()
async def unmute(ctx, user: discord.Member):
        'Unmutes a User'
        try:
            if ctx.author.guild_permissions.administrator:
                role = discord.utils.get(ctx.guild.roles, name='Muted')
                await user.remove_roles(role)
                await ctx.send('Unmuted {}'.format(user.name))
            else:
                await ctx.send('Permission Denied.')
        except discord.ext.commands.errors.BadArgument:
            await ctx.send('User Not Found')

@bot.command()
async def ping(ctx):
        ': Check your connection '
        t1 = ctx.message.created_at
        m = await ctx.send('**Pong!**')
        time = (m.created_at - t1).total_seconds() * 1000
        await m.edit(content='**Pong! Took: {}ms**'.format(int(time)))

@bot.command()
async def perms(ctx, user: discord.Member = None):
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
async def invme(ctx):
    embed=discord.Embed (title="So you want me huh?", colour=discord.Colour.dark_blue(), description='[Invite me](https://discordapp.com/api/oauth2/authorize?client_id=493470893331447820&scope=bot)')
    await ctx.send (embed=embed)

@bot.command()
async def quit(ctx):
    '''Quits bot'''
    if ctx.author.id == 293800689266851850:
        await bot.close()
    else:
        await ctx.send('Permission Denied')

                
        
bot.run(TOKEN)
