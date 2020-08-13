# インストールした discord.py を読み込む
import discord
import random

global frag

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'aaa'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    global frag
    frag = 0

    

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

     # 「/help」と発言したらマニュアル表示
    if message.content == '/help':
        manual = ('使い方\n'
                  '/open ルーレット(重複禁止)を開始\n'
                  '/open2 ルーレット(重複可)を開始\n'
                  '/join ルーレットに参加\n'
                  '/start ルーレット結果を表示\n'
                  '/end ルーレット結果を表示せず終了\n'
                  '/help マニュアルを表示\n'
                 )
        await message.channel.send(manual)


    # 「/open」と発言したらルーレットの参加者を募集開始
    if message.content == '/open':
        global par_list
        global frag

        if frag == 0:
            par_list = []
            frag = 1
            await message.channel.send('参加者を募集(重複禁止)\n/joinでルーレットに参加\n/startでルーレットを開始\n/endでルーレットを強制終了')
        else :
            await message.channel.send('ルーレットが継続中\n/endでルーレットを終了')
    
    if message.content == '/open2':
        if frag == 0:
            par_list = []
            frag = 2
            await message.channel.send('参加者を募集(重複可)\n/joinでルーレットに参加\n/startでルーレットを開始\n/endでルーレットを強制終了')
        else :
            await message.channel.send('ルーレットが継続中\n/endでルーレットを終了')
            

    # 「/join」と発言したらルーレットの参加者リストに追加
    if message.content == '/join':
        if message.author.name in par_list and frag == 1:
            await message.channel.send('重複禁止') 
        else:
            par_list.append(message.author.name)
        await message.channel.send(par_list)

    # 「/start」と発言したらルーレットを開始し結果を表示
    if message.content == '/start':
        if len(par_list) == 0:
            await message.channel.send('参加者がいません\nルーレットを終了します')
        else :
            result = int(random.uniform(0,len(par_list)))
            print(par_list, len(par_list))
            await message.channel.send("結果:{}".format(par_list[result]))
        par_list = []
        frag = 0

    # 「/end」と発言したらルーレットをせずに終了
    if message.content == '/end':
        await message.channel.send('ルーレットを終了します')
        par_list = []
        frag = 0

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)