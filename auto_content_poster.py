import pyrogram
from pyrogram import Client,filters
import time
import os
import random


def gettime():
    result = time.ctime()
    hour=result[11]+result[12]
    minutes=result[14]+result[15]
    timerightnow=hour+minutes
    return timerightnow

api_id=
api_hash=''
phonenumber=''
app = Client("my_account",api_id,api_hash,phone_number=phonenumber)

dirs=os.listdir('D:/')
if "$RECYCLE.BIN" in dirs:
    dirs.remove('$RECYCLE.BIN')
if "System Volume Information" in dirs:
    dirs.remove('System Volume Information')
print('program has started working')


while True:
    time.sleep(30)
    timenow=gettime()
    #if '00'==str(timenow)[2:]:
    if str(timenow)[2:]==str(timenow)[2:]:
        dirindex=random.randint(0, len(dirs)-1)
        for i in range(0,5):
            print(dirs[dirindex])
            files = os.listdir('D:/'+dirs[dirindex])
            if len(files)>0:
                index=random.randint(0, len(files)-1) 
                nameofphoto='D:/'+dirs[dirindex]+'/'+files[index]
                if ('.jpeg' in nameofphoto) or ('.png' in nameofphoto) or ('.jpg' in nameofphoto) or ('.gif' in nameofphoto) or ('.GIF' in nameofphoto) or ('.JPG' in nameofphoto) or ('.JPEG' in nameofphoto):      
                    with app:
                        time.sleep(50)
                        app.send_photo("",nameofphoto)
                elif ('.mp4' in nameofphoto) or ('.wmv' in nameofphoto) or ('.m4v' in nameofphoto) or ('.mov' in nameofphoto) or ('.avi' in nameofphoto) or ('.mkv' in nameofphoto)or ('.MP4' in nameofphoto) or ('.MOV' in nameofphoto):
                    with app:
                        time.sleep(50)
                        app.send_video("", nameofphoto )
                
                os.remove(nameofphoto)
                print('nice')
                if i==4:
                    with app:
                        app.send_message("",'#'+dirs[dirindex])
                    


            else:
                with app:
                    app.send_message("me",'There are no files in '+dirs[dirindex]+' diresctory,you have to add new files!')
                    break

