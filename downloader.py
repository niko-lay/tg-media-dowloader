from pyrogram import Client
from pyrogram import enums
import os

api_id = os.environ.get("TG_API_ID","17349")
api_hash = os.environ.get("TG_API_HASH","344583e45741c457fe1862106095a5eb")
client = Client("my_account", api_id, api_hash)

client.start()

chat_title_filter_text = input("Enter filter text for chat titles (leave blank for all chats): ").strip()

dialogs = client.get_dialogs()

def get_chat_dispay_name(chat):
    if chat.type==enums.ChatType.GROUP or chat.type==enums.ChatType.SUPERGROUP or chat.type==enums.ChatType.CHANNEL:
        return chat.title

    if chat.type == enums.ChatType.PRIVATE:
        return chat.first_name + ' ' + chat.last_name if chat.last_name else ''

    if chat.type == enums.ChatType.BOT:
        return chat.first_name + f" (@{chat.username})"


for chat in dialogs:
    if chat_title_filter_text.lower() in get_chat_dispay_name(chat.chat).lower():
        chat_name = get_chat_dispay_name(chat.chat)
        print(f"ChatID: {chat.chat.id} | Type: {chat.chat.type} | Title: {chat_name} ")



group_username = input("Enter chatID from list above (with minus if awaliable): ").strip()
message_link = input("Enter message link (i.e. https://t.me/c/12345678/54321) or https://t.me/some_dialog_username/54321 or number: ").strip()
message_id=message_link.split("/")[-1]
if message_link.startswith('https://'):
    chat_id=message_link.split("/")[-2]
else:
    chat_id=group_username
print(chat_id, message_id)

async def download_video_from_group(group_username, message_num):
    try:
        
        # # Fetching message object using its link
        chat = await client.get_chat(group_username)
        print(chat)
        print("____________")
        message = await client.get_messages(chat.id, int(message_num))
        print(message)
        print("____________")

        # Checking if the message has video
        if message.video or message.photo or message.video_note or message.voice or message.audio:
            # Downloading the video
            print("Downloading video, please wait...")
            file_path = await message.download()
            print(f"Video downloaded successfully: {file_path}")
        else:
            print("The message doesn't contain any video.")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        await client.stop()

client.loop.run_until_complete(download_video_from_group(chat_id, message_id))
