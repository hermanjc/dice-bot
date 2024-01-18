import dice
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "curl parrot.live":
        print("curling parrot.live")
        parrot = discord.Embed()
        parrot.set_image(url="https://thumbs.gfycat.com/IndelibleAliveAmericancrow-max-1mb.gif")
        print(parrot.image)
        await message.channel.send(embed=parrot)

    if message.content == "curl jackv.co":
        print("curling jackv.co")
        await message.channel.send("I'm Jack VanDrunen. I am a graduate student in the department of logic and philosophy of science at the University of California, Irvine (UCI). I received my B.S. in computer science from UCI in spring 2020, with a specialization in intelligent systems. Please add me on LinkedIn and follow me on GitHub.")

    if message.content.startswith('/roll '):
        dice_str = message.content[message.content.find(' ') + 1:]

        try:
            name = message.author.nick if message.author.nick != None else message.author.name
            response = name + " rolled " + dice_str + ":\n" + '`' + dice.roll_expression(dice_str, long_output=True, special_message=True)[1] + '`'
            await message.channel.send(response)
        except dice.DiceError as e:
            print("DiceError:", e.args)
            await message.channel.send(str(e.args[0]) + ". Use `/dice_help` for usage information.")
    elif message.content == '/roll' or message.content == '/dice_help':
        await message.channel.send("Usage: `/roll ndm` where `n` is the number of dice and `m` is the number of sides.")

# Put bot token in the quotes below
# client.run('')
