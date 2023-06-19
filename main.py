import discord



token = ""
message = '''
message here
'''




client = discord.Client()

@client.event
async def on_connect():
  user_messaged = 0
  for user in client.user.friends:
    try:
        await user.send(message)
        print(f"messaged: {user.name}")
        user_messaged += 1
    except:
        pass
  print(f"\n\n\n{user_messaged} User messaged!")


client.run(token, bot=False)

