#im creating a discord bot here

import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Greetings, my lord.')

    elif message.content.startswith('$meme'):
        await message.channel.send(get_meme())

    elif message.content.startswith('$hack'):
        await message.channel.send("💻 Initiating hack protocol...\n🔍 Target acquired...\n🟢 Access granted!\n😈 Just kidding... stay safe, kid.")

    elif message.content.startswith('$roast'):
        roast = get_roast()
        await message.channel.send(roast)

    elif message.content.startswith('$choose'):
        choices = message.content[len('$choose '):].split(',')
        if len(choices) < 2:
            await message.channel.send("Give me at least 2 options to choose from, genius.")
        else:
            await message.channel.send(f"I choose: **{random.choice([c.strip() for c in choices])}** 🎯")

    elif message.content.startswith('$vibecheck'):
        await message.channel.send(random.choice([
            "✅ You passed the vibe check.",
            "❌ Vibe check failed. Try again later.",
            "🧘 You're vibing on another level.",
            "😤 Negative energy detected. Breathe, human."
        ]))

    elif message.content.startswith('$summon'):
        await message.channel.send("🌩️ A wild bot has appeared!\n⚔️ Awaiting your command, commander.")

    elif message.content.startswith('$help'):
        help_text = """
        **🔥 MemeBot 2.0 Command List 🔥**
        `$hello` - A classy greeting  
        `$meme` - Drops a meme  
        `$hack` - Pretend to hack like a pro 😎  
        `$roast` - Roasts someone on demand  
        `$choose option1, option2` - I'll decide for you  
        `$vibecheck` - Do you pass the vibe check?  
        `$summon` - Summon the bot with power  
        `$help` - You're already here, genius  
        """
        await message.channel.send(help_text)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('your own token') # Replace with your own token.
