from dingtalkchatbot.chatbot import DingtalkChatbot
from datetime import datetime
import time

webhook="https://oapi.dingtalk.com/robot/send?access_token=f48c198d47016e649a1741f42b0264f5d863f4574b2e41b3705eabdb9c7869d7"
secret="SEC87b923af90935ef00fc629de0c906191e6b98eaf1e76305a0ab5d7ec67e7e145"

bot=DingtalkChatbot(webhook,secret)

def slp(hr,mi):
    while datetime.today().hour<hr or (datetime.today().hour==hr and datetime.today().minute<mi):
        time.sleep(30)

def sedmsg(mssg):
    bot.send_text(msg=mssg,is_at_all=False)

def workday():
    slp(5,50)
    sedmsg("同学们早安")
    slp(6,30)
    message="还有10分钟就要上早读啦，今天是"
    if datetime.today().weekday()%2==0:
        message=message+"英语"
    else:
        message=message+"语文"
    message=message+"早读"
    sedmsg(message)
    slp(6,40)
    sedmsg("早读上课啦")
    slp(7,25)
    sedmsg("早读下课，第一节课是英语，7:30上课")
    slp(7,30)
    sedmsg("英语课上课啦")
    slp(8,40)
    sedmsg("第一节课下课，下一节课是语文，8:50上课")
    slp(8,50)
    sedmsg("语文课上课啦")
    slp(10,0)
    sedmsg("第二节课下课，下一节课是数学，10:30上课，现在是上午的体育锻炼时间")
    slp(10,30)
    sedmsg("数学课上课啦")
    slp(11,40)
    sedmsg("第三节课下课，午休")
    slp(13,10)
    sedmsg("午休结束,下午第一节课是化学，13:30上课")
    slp(13,30)
    sedmsg("化学课上课啦")
    slp(14,20)
    sedmsg("下午第一节课下课，下一节课是生物，14:30上课")
    slp(14,30)
    sedmsg("生物课上课啦")
    slp(15,20)
    sedmsg("下午第二节课下课，下一节课是物理，15:50上课，现在是下午的体育锻炼时间")
    slp(15,50)
    sedmsg("物理课上课啦")
    slp(16,40)
    sedmsg("下午第三节课下课，下一节是自主整理，16:50上课")
    slp(16,50)
    sedmsg("自主整理时间xdm")
    slp(17,30)
    sedmsg("下午的课程结束了，快去干饭吧！")

def slf_1():
    slp(18,15)
    sedmsg("还有5分钟就要上晚自习了，第一节晚自习是语文")
    slp(18,20)
    sedmsg("语文晚自习")
    slp(19,10)
    sedmsg("第一节自习下课，第二节自习是数学")
    slp(19,20)
    sedmsg("数学晚自习")
    slp(20,20)
    sedmsg("第二节自习下课，下一节是选科自习")
    slp(20,30)
    sedmsg("化学晚自习")
    slp(21,00)
    sedmsg("生物晚自习")
    slp(21,30)
    sedmsg("物理晚自习")
    slp(22,00)
    sedmsg("晚自习下课！")
    slp(22,30)
    sedmsg("同学们晚安")
    time.sleep(14400)

def slf_2():
    slp(18,15)
    sedmsg("还有5分钟就要上晚自习了，第一节晚自习是英语")
    slp(18,20)
    sedmsg("英语晚自习")
    slp(19,10)
    sedmsg("第一节自习下课，第二节自习是数学")
    slp(19,20)
    sedmsg("数学晚自习")
    slp(20,20)
    sedmsg("第二节自习下课，下一节是选科自习")
    slp(20,30)
    sedmsg("生物晚自习")
    slp(21,00)
    sedmsg("物理晚自习")
    slp(21,30)
    sedmsg("化学晚自习")
    slp(22,00)
    sedmsg("晚自习下课！")
    slp(22,30)
    sedmsg("同学们晚安")
    time.sleep(14400)

def slf_3():
    slp(18,15)
    sedmsg("还有5分钟就要上晚自习了，第一节晚自习是语文")
    slp(18,20)
    sedmsg("语文晚自习")
    slp(19,10)
    sedmsg("第一节自习下课，第二节自习是数学")
    slp(19,20)
    sedmsg("数学晚自习")
    slp(20,20)
    sedmsg("第二节自习下课，下一节是英语自习")
    slp(20,30)
    sedmsg("英语晚自习")
    slp(21,10)
    sedmsg("第三节自习下课，下一节是自主整理")
    slp(21,20)
    sedmsg("自主整理")
    slp(22,00)
    sedmsg("晚自习下课！")
    slp(22,30)
    sedmsg("同学们晚安")
    time.sleep(14400)

def slf_4():
    slp(18,15)
    sedmsg("还有5分钟就要上晚自习了，第一节晚自习是物理")
    slp(18,20)
    sedmsg("物理晚自习")
    slp(19,10)
    sedmsg("第一节自习下课，第二节自习是数学")
    slp(19,20)
    sedmsg("数学晚自习")
    slp(20,20)
    sedmsg("第二节自习下课，下一节是化学自习")
    slp(20,30)
    sedmsg("化学晚自习")
    slp(21,10)
    sedmsg("第三节自习下课，下一节是生物自习")
    slp(21,20)
    sedmsg("生物晚自习")
    slp(22,00)
    sedmsg("晚自习下课！")
    slp(22,30)
    sedmsg("同学们晚安")
    time.sleep(14400)

def slf_5():
    slp(18,15)
    sedmsg("还有5分钟就要上晚自习了，第一节晚自习是语文")
    slp(18,20)
    sedmsg("语文晚自习")
    slp(19,00)
    sedmsg("第一节自习下课，第二节自习是英语")
    slp(19,10)
    sedmsg("英语晚自习")
    slp(19,50)
    sedmsg("第二节自习下课，下一节是数学培优")
    slp(20,0)
    sedmsg("数学培优")
    slp(22,00)
    sedmsg("晚自习下课！")
    slp(22,30)
    sedmsg("同学们晚安")
    time.sleep(14400)

def slf_7():
    slp(18,15)
    sedmsg("还有5分钟就要上晚自习了，第一节晚自习是语文")
    slp(18,20)
    sedmsg("语文晚自习")
    slp(20,20)
    sedmsg("第一节自习下课，第二节自习是数学")
    slp(20,30)
    sedmsg("数学晚自习")
    slp(21,30)
    sedmsg("自主整理")
    slp(22,00)
    sedmsg("晚自习下课！")
    slp(22,30)
    sedmsg("同学们晚安")
    time.sleep(14400)

sedmsg("项目地址:https://github.com/ABlyh-LEO/Dingbot 当前版本:beta v0.1 Powered by ABlyh 若机器人出现问题，请私信我")
sedmsg("如果看到这条信息，则说明机器人部署完成")
slf_1()

while True:
    dt=datetime.today()
    wkdy=dt.weekday()
    if 0<=wkdy<=5:
        workday()
        if wkdy==0:
            slf_1()
        elif wkdy==1:
            slf_2()
        elif wkdy==2:
            slf_3()
        elif wkdy==3:
            slf_4()
        elif wkdy==4:
            slf_5()
        else:
            sedmsg("忙了一周了，休息一下吧")
            time.sleep(32400)
    else:
        slf_7()
