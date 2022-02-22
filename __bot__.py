from discord import Member

import asyncio

import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Ich bin der neue Bot auf dem Server mit dem Namen {}'.format(client.user.name))
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('FeG Teenkreis'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('Mein cooler Bot!'), status=discord.Status.online)
        await asyncio.sleep(3)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if '!help' in message.content:
        await message.channel.send('**Hilfe zum Bot**\r\n'''
                                   '!help - Zeigt diese Hilfe an')
    if message.content.startswith('!userinfo'):
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                embed = discord.Embed(title='Userinfo für {}'.format(member.name),
                                      description='Dies ist eine Information für den User {}'.format(member.mention),
                                      colour=0x22a7f0)
                embed.add_field(name='Server beigetreten', value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                embed.add_field(name='Discord beigetreten', value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                rollen = ''
                for role in member.roles:
                    if not role.is_default():
                    rollen += '{} \r\n'.format(role.mention)



client.run('OTQ1NjE1ODM2MzI3MDU5NDU2.YhSvYA.qSxZ_xe1wtvCX49Zx4DrT1BEM5M')