from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

import os
import re
import logging

FORMAT = '%(asctime)s %(levelname)s: %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.INFO,format=FORMAT,datefmt=DATE_FORMAT,filename='logfile.log', filemode='a')

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
 
def createForm(filename):
    with open(r'PracticeLineBot/AutoReplyer/YourForm.txt','rb') as f:
        Thetext = f.read().decode('utf-8','ignore')
        with open(r'PracticeLineBot/AutoReplyer/{}.txt'.format(filename),'wb') as f2:
            f2.write(Thetext.encode('utf-8','ignore'))

def errorMessage(event):
    line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TextSendMessage(text="請重新輸入有效指令")
                )

@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                '''
                line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TextSendMessage(text=event.message.text)
                )
                '''
                TheMessage = event.message.text.strip()
                userID = event.source.user_id
                userTXT = userID + ".txt"
                Formpath = os.path.join(r'PracticeLineBot/AutoReplyer',userTXT)
                if not(os.path.isfile(Formpath)):
                    createForm(userID)

                
                print(userID)
                if("查看" == TheMessage):
                    with open(Formpath,'rb') as f:
                        Thetext = f.read().decode('utf-8','ignore')
                        line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=Thetext)
                        )

                elif("回報" == TheMessage):
                    from .AutoReplyer import Script
                    import scriptlocator
                    Myfile = scriptlocator.Locator()
                    Myfilepath = Myfile.getfilelocation(os.path.join(r"AutoReplyer",userTXT))
                    MyScript = Script.AutoFillForm(Myfilepath)
                    try:
                        result = MyScript.start()
                        line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text="回報成功")
                        )
                        logging.info(result + "  SUCCESS")
                    except:
                        line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text="回報失敗")
                        )
                        logging.error(userID + "  ", exc_info=True)

                elif(re.match(r"[1-9]:",TheMessage)):
                    modifyText = TheMessage.split(":")
                    Formtext = None
                    with open(Formpath,'rb') as f:
                        lineidx = int(modifyText[0])-1
                        Formtext = f.readlines()
                        tmp = Formtext[lineidx].decode('utf-8','ignore').split("|")[0]
                        modifyText_tmp = modifyText[1].split("\n")[0]
                        tmp2 = tmp+"|"+(modifyText_tmp.strip())
                        if(len(Formtext)>lineidx+1):
                            tmp2 = tmp2 +"\n"
                        Formtext[lineidx] = tmp2.encode('utf-8','ignore')
                    
                    with open(Formpath,'wb') as f:
                        f.writelines(Formtext)

                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="修改成功")
                    )

                else:
                    errorMessage(event)
        return HttpResponse()
    else:
        return HttpResponseBadRequest()