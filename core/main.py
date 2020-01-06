from variables import webex_bot as bot
import teams_functions
from flask import Flask, request

app = Flask(__name__)

@app.route('/newmessage', methods=['POST'])
def new_message():

    json_data = request.json

    message_id = json_data["data"]["id"]
    room_id = json_data["data"]["roomId"]

    message = teams_functions.get_message(message_id, bot.token).split()[1]

    # I would like to show the operational data of my interfaces
    if message.lower() == "hello":
        teams_functions.post_message_markdown("Hello!", room_id, bot.token)

    else:
        teams_functions.post_help_bot(room_id, bot.token)

    return "message sent"


@app.route('/newroom', methods=['POST'])
def new_room():

    json_data = request.json

    room_id = json_data["data"]["roomId"]

    teams_functions.post_message_markdown("Hey, I have been added to a new room !", room_id, bot.token)
    teams_functions.post_help_bot(room_id, bot.token)

    return "message sent"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)