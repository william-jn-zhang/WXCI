#coding=utf-8
from utils.BasicStateHandler import BasicStateHandler
from wxapi.FieldName import FieldName

class StartStateHandler(BasicStateHandler):

    def __init__(self):
        self.name = "start"

    def transition(self, session, msg_dict):
        if "score_list" not in session:
            session['stuId'] = ""
            session['score_list'] = []
        #case get text
        if msg_dict[FieldName.MsgType] == FieldName.text:
            content = msg_dict[FieldName.Content]
            content = content.strip()
            if content == "help":
                return (self.name, u"回复学生ID，回复finish完成统计，回复delpre删除上一条记录")
            if content == "delpre":
                (stuId, score) = session['score_list'].pop(len(session['score_list']) - 1)
                session['stuId'] = ""
                return (self.name, u"删除记录：" + str(stuId) + "," + str(score))
            if content == "finish":
                return ("finish", u"统计完毕！")
            try:
                int(content)
            except Exception, e:
                return (self.name, u"请告诉我学号，统计完毕回复finish")
            session['stuId'] = content
            return ("score", None)
