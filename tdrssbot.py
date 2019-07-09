import feedparser, os, time, json, telegram

token = "Your_bot_token"
chat_id = "Your_chat_id"
bot = telegram.Bot(token)

def list_creator():
    fd = feedparser.parse("Your Torrentday RSS feed link")['entries']
    tlist = []
    for i in fd:
        tlist.append(i['title'])
    return tlist

def json_write(file_name, list):
    with open(file_name, 'w') as jlist:
        json.dump(list, jlist)

def torrent_checker(file_name):
    if os.path.exists(file_name):
        with open(file_name) as stored_list:
            initial_list = json.load(stored_list)
        latest_list = list_creator()
        diff = set(latest_list) - set(initial_list)
        if diff != set():
            for i in diff:
                bot.sendMessage(chat_id, i)
            json_write(file_name, latest_list)
    else:
        latest_list = list_creator()
        json_write(file_name, latest_list)

if __name__ == '__main__':
    while True:
        torrent_checker("torrents.json")
        time.sleep(300)


