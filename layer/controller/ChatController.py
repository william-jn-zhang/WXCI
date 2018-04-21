'''
author: william.jn.zhang@gmail.com
'''
from flask import session
from wxapi.FieldName import FieldName
import time

class SessionControlFields:
    CURRENT_APP_KEY = "current_app"
    APP_SESSION = "app_session"
    LAST_INTERACT_TIME = "last_interact_time"
    

def new_app_session(session):
    session[SessionControlFields.CURRENT_APP_KEY] = None
    session[SessionControlFields.APP_SESSION] = {}
    session[SessionControlFields.LAST_INTERACT_TIME] = time.time()
    return

def sig_c(session):
    new_app_session(session)
    return

class ChatController:
    SIG_MARKER = "$"
    SIG_C = "C"

    def set_caller(self, Caller):
        self.caller = Caller
        return

    def call_caller(self, session, entity_dict):
        return self.caller.handle_call(session, entity_dict)

    def handle_entity(self, entity_dict):
        MsgType = entity_dict[FieldName.MsgType]
        if MsgType == FieldName.text:
            content = entity_dict[FieldName.Content]
            content = content.strip().lower()
            if content[0] == self.SIG_MARKER: # this is an instruction
                sig = content[1:]
                if sig == self.SIG_C:
                    sig_c(session)
                    return FieldName.success
                # add signals here
        '''
        session duration check can add here
        '''
        session[SessionControlFields.LAST_INTERACT_TIME] = time.time()
        return self.call_caller(session, entity_dict)
