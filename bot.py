import dice
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/roll'):
        dice_strs = message.content.split()
        print(dice_strs)

        for s in dice_strs[1:]:
            try:
                name = message.author.nick if message.author.nick != None else message.author.name
                # response = message.author.nick + " rolled " + s + ": " + dice.roll_expression(s, long_output=True, special_message=True)
                response = name + " rolled " + s + ": " + dice.roll_expression(s, long_output=True, special_message=True)
                # await client.send_message(message.channel, response)
                await message.channel.send(response)
            except dice.DiceError as e:
                print("DiceError:", e.args)
                # await client.send_message(message.channel, e.args[0] + ". Use `/dice_help` for usage information.")
                await message.channel.send(str(e.args[0]) + ". Use `/dice_help` for usage information.")
    elif message.content.startswith('/dice_help'):
        # await client.send_message(message.channel, "Usage: `/roll ndm` where `n` is the number of dice and `m` is the number of sides.")
        await message.channel.send("Usage: `/roll ndm` where `n` is the number of dice and `m` is the number of sides.")

# Dice Bot Secret
# client.run('NTYzNDQ0MDI4MzM5NjUwNTcy.XKZeCw.QCFt2_jdjFv_Fr9qFOROQA6MrOs')
# Dev Bot Secret
client.run('NjE5MzA2MzUyNjg2MTM3MzU0.XXGUkA.cTXv3Ac50wQ2o5ORXGZVPriVhdk')