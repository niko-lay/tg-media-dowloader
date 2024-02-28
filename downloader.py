from pyrogram import Client
import os

api_id = os.environ.get("TG_API_ID","17349")
api_hash = os.environ.get("TG_API_HASH","344583e45741c457fe1862106095a5eb")
client = Client("my_account", api_id, api_hash)

client.start()

# with Client("my_account", api_id, api_hash) as app:
    
chat_title_filter_text = input("Enter filter text for chat titles (leave blank for all chats): ").strip()

chats = client.get_dialogs()

for chat in chats:
    if chat.chat.id < 0 and chat_title_filter_text.lower() in chat.chat.title.lower():
        print(f"ChatID: {chat.chat.id} | Title: {chat.chat.title}")

group_username = input("Enter chatID from list above (with minus if awaliable): ").strip()
message_link = input("Enter message link (i.e. https://t.me/c/12345678/54321) or number: ").strip().split("/")[-1]


async def download_video_from_group(group_username, message_num):
    try:
        # await client.start()
        
        # # Fetching message object using its link
        chat = await client.get_chat(group_username)
        print(chat)
        print("____________")
        message = await client.get_messages(chat.id, int(message_num))
        print(message)
        print("____________")

        # Checking if the message has video
        if message.video or message.photo or message.video_note or message.voice:
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

client.loop.run_until_complete(download_video_from_group(group_username, message_link))
