# Minecraft Bedrock Discord Bot

Discord bot plugin for Minecraft bedrock edition on Docker.

## Overview

I built a Minecraft bedrock edition server with Docker, but there was no proper plugin for that environment, so I created a Bot plugin for Discord. It currently supports the following features.

- Send a message when a specific command is entered.
- Notify when someone log in and log out of the Minecraft server.

![mcdbot00](https://kosukelab.com/share/minecraft-discord-bot.png)

- [develop] Added the ability to check free storage space and free memory space.

## Preparation

- Require Python 3.5.3 or higher
- Require pip3
- Require `discord.py`

  ```(text)
  $ pip3 install -U "discord.py[voice]"
  ```

- Get Discord token at developer site, and edit `bot_config.py`
- Edit `MC_LOG` at `login_check.sh` : enter path of your minecraft log file.
  - Check path of container's log file.
  
  ```(text)
  $ docker inspect <container_name> | grep 'LogPath'
  ```

- It is recommended that you add the following entry in visudo.

  ```(text)
  $ sudo visudo

  <your_user_name>  ALL=NOPASSWD:  /bin/tail
  ```

## How to use

- I recommend to start a separate session using screen command etc.
  
  ```(text)
  $ screen -S <session_name>
  ```

- Just execute the following command.

  ```(text)
  $ python3 discordbot.py
  ```

- The bot program will be left running, so detach it with Ctrl+A → D.

## Donate

- Bitcoin (BTC) : `bc1qnv945v0askdkcdazn9psqh0wacsr5dz70uw4gf`    (Native SegWit)
- Ethereum (ETH) : `0x7C85446DDCC62D749227cBc55c1FF0D711B59979`
- Symbol (XYM) : `NCTFRL5RGOAKAW4B3HZLUMEM6YGWI3WRK4V2OKY`
