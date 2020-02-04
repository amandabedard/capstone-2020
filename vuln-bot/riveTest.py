from rivescript import RiveScript

rs = RiveScript()
rs.load_directory("./capstone-2020/vuln-bot/rive")
rs.sort_replies()

while True:
    msg = input("You> ")
    if msg == "/quit":
        quit()
    reply = rs.reply('localusr', msg)
    print("Bot>", reply)