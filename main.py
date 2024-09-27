import os
import logging
from random import shuffle, randint
from datetime import timedelta
from dotenv import load_dotenv
from telethon import TelegramClient, events, functions
from bots_config import bots

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Retrieve environment variables
admin_username=os.getenv("ADMIN_USERNAME")
main_bot_api_id=os.getenv("MAIN_BOT_API_ID")
main_bot_api_hash=os.getenv("MAIN_BOT_API_HASH")
channels = os.getenv('CHANNELS').split(',')

# Initialize main Telegram client
client = TelegramClient(main_bot_api_id, main_bot_api_id, main_bot_api_hash)

def manage_times():
    """
        Randomly shuffles the bots and assigns them randomized delay times.
        Returns a list of bots with corresponding times.
    """
    my_dic = []
    shuffle(bots)

    time = 0
    amount = len(bots)

    first = int(amount * (15/100))
    for i in range(0,first):
        randnum = randint(60, 300)
        my_dic.append([bots[i]['id'],bots[i]['hash'],randnum])

    second = int(amount * (20/100))
    time = 300

    for i in range(first,second+first):
        randnum = randint(301, 1800)
        my_dic.append([bots[i]['id'],bots[i]['hash'],randnum + time])

    third = int(amount * (30/100))
    time = time + 1800
    for i in range(second+first,second+first+third):
        randnum = randint(1800, 10800)
        my_dic.append([bots[i]['id'],bots[i]['hash'],randnum + time])

    fourth = amount - (second+first+third)
    time = time + 10800
    for i in range(second+first+third,second+first+third+fourth):
        randnum = randint(10800, 18000)
        my_dic.append([bots[i]['id'],bots[i]['hash'],randnum + time])
    return my_dic


async def active_client(event):
    """
        Handles the bot's interaction with the client and channels.
        It sends messages to the specified user and logs them.
    """
    times = manage_times()
    channel_id = event.message.peer_id.channel_id
    sender = await event.get_sender()
    username = sender.username
    print(channel_id)
    print(times)
    for key, user in enumerate(times):
        try:
           if not user[0] == main_bot_api_id:
                post_id = event.message.id
                print("start : ",user[0])
                logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                        level=logging.WARNING)
                client2 = TelegramClient(user[0],user[0], user[1])
                await client2.start()
                await client2.send_message(username, 'Done',comment_to = post_id, schedule=timedelta(seconds=user[2]))
                await client2(functions.messages.GetMessagesViewsRequest(
                        peer=channel_id,
                        id=[post_id],
                        increment=True
                    ))
                await client2.disconnect()
                print("comment")
           else:
                post_id = event.message.id

                await client.send_message(username, 'Done',comment_to = post_id, schedule=timedelta(seconds=user[2]))
                await client(functions.messages.GetMessagesViewsRequest(
                        peer=channel_id,
                        id=[post_id],
                        increment=True
                    ))
                print("comment")

        except Exception as e:
                print(e)
                text = username + " | "+ str(post_id)+" | "+str(e)
                await client.send_message(entity="n0rouzy", message=text)
                continue
            
@client.on(events.NewMessage(chats=channels))
async def handle_new_message(event):
    """
        Event handler for new messages in the specified channels.
        It triggers the `active_client` function.
    """
    try:
        await active_client(event)
    except Exception as e:
        print(e)
        text = username + " | "+ str(post_id)+" | "+str(e)
        await client.send_message(entity=admin_username, message=text)
    
client.start()
client.run_until_disconnected()