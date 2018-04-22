#coding=utf-8
'''
author: william.jn.zhang@gmail.com
'''
from myapp.scoreCount.utils.BasicStateHandler import BasicStateHandler
from wxapi.FieldName import FieldName

class FinishStateHandler(BasicStateHandler):

    def __init__(self):
        self.name = "finish"

    def transition(self, session, msg_dict):
        #case get text
        if msg_dict[FieldName.MsgType] == FieldName.text:
            content = msg_dict[FieldName.Content]
            content = content.strip()
            if content == "help":
                return (self.name, u"回复display打印统计结果，回复clear清空统计内容")
            if content == "display":
                display_str = ""
                for (stuId, score) in session['score_list']:
                    display_str += (str(stuId) + "," + str(score) + "\n")
                display_str += " "
                return (self.name, display_str)
            if content == "clear":
                #del userData['score_list']
                session['score_list'] = []
                session['stuId'] = ""
                return ("start", None)
            else:
                return (self.name, u"回复display打印统计结果，回复clear清空统计内容")
