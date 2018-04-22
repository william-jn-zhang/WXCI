#coding=utf-8
from utils.BasicStateHandler import BasicStateHandler
from wxapi.FieldName import FieldName

class ScoreStateHandler(BasicStateHandler):

    def __init__(self):
        self.name = "score"

    def transition(self, session, msg_dict):
        #case get text
        if msg_dict[FieldName.MsgType] == FieldName.text:
            content = msg_dict[FieldName.Content]
            content = content.strip()
            if content == "help":
                return (self.name, u"回复学生成绩，回复wrongid重新输入学生ID")
            if content == "wrongid":
                session['stuId'] = ""
                return ("start", u"请重新输入学生ID")
            try:
                float(content)
            except Exception, e:
                return (self.name, u"请告诉我" + str(session['stuId']) + u"的成绩是多少分")
            session['score_list'].append((session['stuId'], content))
            session['stuId'] = ""
            return ("start", None)
