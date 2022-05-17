from pyrogram import Client,filters
import time
from time import *

api_id=
api_hash=
phonenumber=''
app = Client("first_p_session",api_id,api_hash,phone_number=phonenumber)
source=[]



@app.on_message(filters.chat(source))
async def new_post(client,message):
    check=str(message)
    message_ID=message.message_id
    chat_ID=message.chat.id
    if '"Photo"' in check: 
        Photo_file_ID=message.photo.file_id
        await app.send_photo("",Photo_file_ID, caption="")
        await app.send_photo("",Photo_file_ID, caption="")
    if '"Video"' in check:
        Video_file_ID=message.video.file_id
        await app.send_video("",Video_file_ID, caption="")
        await app.send_video("",Video_file_ID, caption="")
    else:
        print(' ')
      
app.run()

    

