import werobot
from werobot.replies import ImageReply
# import cv2
import os
from PIL import Image
from io import BytesIO,BufferedReader

robot = werobot.WeRoBot(token='')

robot.config["APP_ID"]=""
robot.config["APP_SECRET"]=""

# https://blog.csdn.net/IkerIkerIker/article/details/110914641
# https://werobot.readthedocs.io/zh_CN/latest/index.html

client=robot.client


# @robot.text
# def hello_world():
#     return 'Hello World!'

# @robot.text
# def reply(message):
#     if message.content == "boss":
#         return "正文为boss"

# @robot.text
# def hello(message, session):
#     count = session.get("count", 0) + 1
#     session["count"] = count
#     return "Hello! You have sent %s messages to me" % count

# access_token = client.grant_token()
# print("Access Token:", access_token)

vip_list=["ost0r5sREFtC__TJ1HejJId1fY**","ost0r5m85utVLhtAgz0oPic6JU**"]


@robot.handler
def reply(message,session):
    # print(message.source,message.content)
    if message.content == "boss" and message.source in vip_list:
    
        os.system("wget -P /root -O /root/temp.log http://192.168.192.65/temp.log")
        os.system("gnuplot /root/plot.sh")
        # img = Image.open("/root/2.jpg")
        # str_encode = img.tobytes()
        # f4 = BytesIO(str_encode)
        # f4.name = 'test.jpg'
        # f5 = BufferedReader(f4)
        # return_json = client.upload_media("image",f5)
        # mediaid = return_json["media_id"]
        with open("/root/2.jpg", 'rb') as file_obj:
            return_json = client.upload_media("image",file_obj)
            mediaid = return_json["media_id"]
        return ImageReply(message=message, media_id=mediaid)



robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()