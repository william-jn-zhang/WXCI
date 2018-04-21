'''
author: william.jn.zhang@gmail.com
'''
from flask import session


class ControllSessionFields:
    


class ChatController:

    def set_caller(self, Caller):
        self.caller = Caller
        return

    def call_caller(self, session, entity_dict):
        return self.caller.handler_call(session, entity_dict)

    def handle_entity(self, entity_dict):
        
