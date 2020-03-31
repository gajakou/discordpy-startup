# 終了コマンド実装
import sys
# discordのAPI
import discord
# Google検索
from googlesearch import search

# discordに接続
client = discord.Client()

# モード切替
ModeFlag = 0

# 起動時のメッセージ
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name='パワハラ会議'))
# メッセージを受けた時の動作
@client.event
async def on_message(message):
    # イベント入るたびに初期化はまずいのでグローバル変数で
    global ModeFlag
    # botの発言は無視する(無限ループ回避)
    if message.author.bot:
        return
    # 終了コマンド
    if message.content == '!end':
        await message.channel.send('会議終わり！')
        sys.exit()
    # google検索モード(次に何か入力されるとそれを検索)
    if ModeFlag == 1:
        kensaku = message.content
        ModeFlag = 0
        count = 0
        # 日本語で検索した上位5件を順番に表示
        for url in search(kensaku, lang="jp",num = 5):
            await message.channel.send(url)
            count += 1
            if(count == 5):
               break
    # google検索モードへの切り替え
    if message.content == '!og':
        ModeFlag = 1
        await message.channel.send('気になることをgoogleで検索したいというのか？チャットに発言してみよ。')
    # 単純な応答
    if message.content == 'ギルガメッシュ？':
        await message.channel.send('人違いだ、死に値する。')
    # 特定の文字から始まる文章が発言されたとき
    if message.content.startswith('無惨'):
        lose = message.author.name + "軽々しく私の名を呼ぶでない、死に値する。"
        await message.channel.send(lose)
    #リプライを受け取った時
    if client.user in message.mentions:
        reply = f'{message.author.mention} 気に入った、私の血をふんだんに分けてやろう。'
        await message.channel.send(reply)
# botの起動と接続
client.run('NjkyNjU4NzY0MDc1MjM3Mzk3.XoLeJg.6Y7jEt1LzRwOetL9sr7XnTQiZhw')