# Discord-Moderation

• An open-source, customizable and reliable Discord bot for moderation written in Py-cord.

Current status: **supported**

## Introduction

👋, welcome to the this Discord-Moderation bot! This is a fully open-source code project for you to download or clone and use for your own Discord server. This bot is designed to be easy to use and customize, and is a great way to get started with Discord bots. 

Even if you have no former experience with code, this project will work for you because of the detailed guide. If you have any questions, feel free to hit me up.

At the top of this README, you'll see the current status of the bot. This will tell you if the bot is currently supported or not. If it is not supported, you can still use it, but you will not receive any updates or support. Depending on the support of the bot, I might not always support it with new Discord features coming out or py-cord changes.

## Features

Discord-Moderation is equipped with a variety of features needed for a modern Discord server, including:

- Ban and kick
- Mute and unmute
- Warn and clear warnings
- Clear messages
- And more! A more detailed list [here](https://github.com/KipzonderKop101/Discord-Moderation#commands)

## Installation

To keep things clear, this page does not hold a detailed guide of how to install and set-up the bot, however, you can find a detailed guide [here](https://github.com/KipzonderKop101/Discord-Moderation/blob/main/docs/GUIDE.md), which will walk you through the entire process.

## Support

As mentioned previously, you can use this bot without any prior experience with code. However, it's always possible you get stuck. That's why you can always reach out to me on Discord: **Boon#5705**. I'll be happy to help you out.

## commands

`<>` represent required arguments, `[]` represent optional arguments.

Implemented commands:

- `/ban <user> [reason]` - Bans a user from the server
- `/kick <user> [reason]` - Kicks a user from the server

Planned commands:

- `/mute <user> [reason]` - Mutes a user from the server
- `/unmute <user> [reason]` - Unmutes a user from the server
- `/warn <user> [reason]` - Warns a user from the server
- `/warn <user>  [reason]` - Clears a user's warnings from the server
- `/warns <user>` - Shows a user's warnings from the server
- `/clear [amount]` - Clears a certain amount of messages from the channel, default is 10
- `/lock [channel] [reason]` - Locks a channel, default is the context channel
- `/unlock [channel] [reason]` - Unlocks a channel, default is the context channel
- `/slowmode [channel] [time]` - Sets the slowmode of a channel, default is the current channel, default time is 10 seconds
- `/Setmodlog [channel]` - Set a mod log channel, default is the context channel, can only be one
- `/Setmuterole <role>` - Set a mute role, can only be one
- `/Setmodrole <role>` - Set a mod role, can be multiple
- `/Setadminrole <role>` - Set an admin role, can be multiple
- `/Addwhitelistedrole <role>` - Add a whitelisted role, can be multiple
