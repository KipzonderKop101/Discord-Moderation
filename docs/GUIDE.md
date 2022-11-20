# Guide

In this guide you'll find a detailed explanation on how to use/install this bot and customize it to your needs.

## Installation

In this part of the guide you'll find a definitive guide on how to install this bot and get it running. While also seeing how to customize it to your liking.

### Requirements

- Python 3.6 or higher
- pip 19.0 or higher
- py-cord 2.0 or higher
- python_dotenv 0.17.0 or higher

### Setup

1. Clone the repository
2. Install the requirements with `pip install -r requirements.txt`, or `pip3 install -r requirements.txt` if you're on Linux (or Mac with ZSH)
3. Create a new application on the [Discord Developer Portal](https://discord.com/developers/applications)
4. Create a new bot user and copy the token
5. Add the bot to your server

### Configuration

1. Create a new file called `.env` in the root directory
2. Add the following content to the file:

```env
TOKEN=your-token-here
```

3. Replace `your-token-here` with the token you copied earlier

Make sure to not share your token with anyone! This token is your access to the bot, so sharing it might end up with you losing control over your bot.

Next, go into `main.py`, and find the client declaration. You'll see something like this:

```py
client = discord.Bot(intents=intents, debug_guilds=[1234567890])
```

Replace `1234567890` with the ID of your server. This will enable debug mode for your server, which should reload commands on your server faster.

### Running

1. Go into your terminal, and run the bot with `python main.py`, or `python3 main.py` if you're on Linux (or Mac with ZSH)
2. If everything went well, you should see the bot come online in your server
3. Now, you can use the bot with the `/` commands. For example, `/ping`

### customizing

In this part of the guide you'll find a definitive guide on how to customize this bot to your liking.

This bot has many parts you can go and customize, for example, every command has embeds or messages you can customize, and you can also customize the bot's status.

For example, to customize a text. In the `src/cogs/General/help.py` file you can find this piece of code:

```py
discord.SelectOption(label='Help', value='help', description='Get help on a command or category')
```

This is the help command's select menu option. You can change the label, value, and description to whatever you want. If you do so, keep in mind to also change the part's of code responsible for the help command's select menu. For example, the part that checks for the value selected, because if you change the value, it won't work anymore.

Another example are embeds. In the `src/cogs/General/help.py` file you can find this piece of code:

```py
embed = discord.Embed(title='Help', description='Select a category to get help on a command', color=discord.Color.blurple())
```

This is the help command's embed. You can change the title, description, and color to whatever you want.

Furthermore, you can also change the bot's status. In the `main.py` file you can find this piece of code:

```py
await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='over the server'))
```

You can also go and change the type, and name to whatever you want. You can find more info on the types [here](https://discordpy.readthedocs.io/en/latest/api.html#discord.ActivityType).
