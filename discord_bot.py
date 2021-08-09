#導入Discord.py
import asyncio
import time
import discord
import random, os, asyncio
import keep_alive
from discord.ext import commands
import json

#bot是我們與Discord連結的橋樑
bot = discord.bot()



#調用event函式庫
@bot.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：',bot.user)
    print('目前運作正常 如有問題請找39.peko')
    game = discord.Game('努力學習py中')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.dnd, activity=game)





@bot.event
#當有訊息時
async def on_message(message):
    #如果以「說」開頭
    if message.content.startswith('說'):
      #分割訊息成兩份
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send("你要我說什麼啦？")
      else:
        await message.channel.send(tmp[1])
    if message.content.startswith('更改狀態'):
        #切兩刀訊息
        tmp = message.content.split(" ",2)
        #如果分割後串列長度只有1
        if len(tmp) == 1:
            await message.channel.send(f"{message.author.mention} 別碰我狀態")
        else:
            game = discord.Game(tmp[1])
            #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
            await bot.change_presence(status=discord.Status.idle, activity=game)
    
    if message.content == '所在群組':
        #獲取當前所在群組(極限150個，預設為100個)，並用flatten將它全部移到guilds這個list裡面
        guilds = await bot.fetch_guilds(limit=150).flatten()
        #遍尋 guilds
        for i in guilds:
            #由於我們只要 guilds 的name 就好，當然也可以獲取 id~
            
            await message.channel.send(i.name)

    if message.content.startswith('說http'):
        time.sleep(3)
        await message.channel.send(f"{message.author.mention} 別傳連結")
        await message.delete()


        
                
        
        
if __name__ == '__main__':
    keep_alive.keep_alive()
    bot.run('ODcyNDg4NjA0NDUzMTg3NTg0.YQqmVQ.4MCJ9peKQ4Vu05bwU97TbVJZBjI') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面