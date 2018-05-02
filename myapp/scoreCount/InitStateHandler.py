#coding=utf-8
from utils.BasicStateHandler import BasicStateHandler
from utils.NamelistDocxReader import NamelistDocxReader
from wxapi.FieldName import FieldName

class InitStateHandler(BasicStateHandler):

    namelistpath = "myapp/scoreCount/data/namelist.docx"

    def __init__(self):
        self.name = "init"

    def transition(self, session, msg_dict):
        content = msg_dict[FieldName.Content]
        content = content.strip()
        if content == "start":
            return ("start", None)
        if content == "loadnamelist":
            nr = NamelistDocxReader()
            nl = nr.extract(self.namelistpath)
            #print("in file %s" % __file__)
            #print(nl)
            nl_dict = {}
            for (seq, id, name) in nl:
                id = str(int(id))
                nl_dict[id] = name
            session["name_list"] = nl_dict
            return ("start", None)
        return (self.name, u"回复start开始统计，回复loadnamelist加载姓名册")
