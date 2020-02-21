import asyncio
import discord
import os
import re

client = discord.Client()

@client.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(client.user.name)
    print(client.user.id)
    print("===========")

@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("680439770853146645")
    fmt = '{0.mention} 님이 서버에서 나가셨습니다.'
    await client.send_message(channel, fmt.format(member, member.server))   

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == "$help":
        await client.send_message(message.channel, "command")
        embed = discord.Embed(title="명령어", description="아직 아무것도 없지요 헤헤", color=0x00ff00) 
        embed.set_footer(text = "by mimiru") 
        embed.set_image(url="https://cdn.discordapp.com/attachments/680419909284528148/680433158373900318/00000.jpg") 
        await client.send_message(message.channel, embed=embed)



@client.event
async def on_member_join(member):
    fmt = '{1.name} 에 오신걸 환영합니다., {0.mention} 님'
    channel = member.server.get_channel("680439770853146645")
    await client.send_message(channel, fmt.format(member, member.server))
    await client.send_message(member, "Kaphen(케이픈)에 온걸 환영합니다!")
    await client.send_message(member, "케이픈에서 통화/채팅/게임 플레이시 모든내용은 유튜브에 업로드될 수 있습니다.")
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
