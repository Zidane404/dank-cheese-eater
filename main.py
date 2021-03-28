import discord, asyncio, json

from discord.ext import commands

with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')
cheese_delay = config.get('use_cheese_delay')
confirm_cheese_delay = config.get('confirm_cheese_delay')
cheese_amount = config.get('cheese_amount')


bot = commands.Bot(command_prefix=config.get('prefix'), self_bot=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Successfully Authorised as: " + bot.user.name + " UID: (" + str(bot.user.id) + ")")
    print('Use $cheese [amount] in any channel to begin! ')

@bot.command()
async def cheese(ctx, amount: int):
    await ctx.message.delete()
    for i in range(0,amount):
        async with ctx.typing():
            await asyncio.sleep(3)
        await ctx.send("pls use cheese")
        async with ctx.typing():
            await asyncio.sleep(confirm_cheese_delay)
        await ctx.send('y')
        await asyncio.sleep(cheese_delay)
    return

bot.run(token, bot=False)

