#coding=utf-8
from myapp.scoreCount.utils.FSM import FSM
from myapp.scoreCount.InitStateHandler import InitStateHandler
from myapp.scoreCount.StartStateHandler import StartStateHandler
from myapp.scoreCount.ScoreStateHandler import ScoreStateHandler
from myapp.scoreCount.FinishStateHandler import FinishStateHandler
from wxapi.messageManagement.ReplyMessage import replyTextMessage
from wxapi.FieldName import FieldName
import pickle

def __create_new_fsm():
    fsm = FSM()
    init = InitStateHandler()
    start = StartStateHandler()
    score = ScoreStateHandler()
    finish = FinishStateHandler()
    fsm.regist_state_handler(init)
    fsm.regist_state_handler(start)
    fsm.regist_state_handler(score)
    fsm.regist_state_handler(finish)
    fsm.set_state("init")
    return fsm

def scoreCount(session, msg_dic):
    fsm = None
    if "fsm" not in session:
        fsm = __create_new_fsm()
    else:
        fsm = pickle.loads(session["fsm"])
    rep_str = fsm.get_message(session, msg_dic)
    session["fsm"] = pickle.dumps(fsm)
    if rep_str is None:
        return FieldName.success
    rep_xml = replyTextMessage(
            msg_dic[FieldName.FromUserName],
            msg_dic[FieldName.ToUserName],
            rep_str
        )
    return rep_xml
