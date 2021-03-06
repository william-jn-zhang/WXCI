#coding=utf8
'''
author: william.jn.zhang@gmail.com
'''
from config.cfg import APPS
from config.cfg import APP_MODULE_PATH
from layer.controller.ChatController import SessionControlFields
from layer.controller.ChatController import sig_c
from wxapi.messageManagement.ReplyMessage import replyTextMessage
from wxapi.FieldName import FieldName

class ChatCaller:

    class ChatCallerShell:

        INSTR_LISTAPP = "listapp"

        def get_applist(self):
            applist_str = u"以下app可以使用：\n"
            for (k, (c, d)) in APPS.items():
                applist_str += (k + ": " + d) + "\n"
            applist_str += u"回复相应的app以启动"
            return applist_str

        def do(self, entity_dict):
            if entity_dict[FieldName.MsgType] == FieldName.text:
                content = entity_dict[FieldName.Content]
                content = content.strip()
                if content == self.INSTR_LISTAPP:
                    applist_str = self.get_applist()
                    return replyTextMessage(
                            entity_dict[FieldName.FromUserName],
                            entity_dict[FieldName.ToUserName],
                            applist_str
                        )

            return replyTextMessage(
                    entity_dict[FieldName.FromUserName],
                    entity_dict[FieldName.ToUserName],
                    u"回复listapp显示可用app"
                )

    def createAppInstance(self, module_name, class_name, *args, **kwargs):
        module_meta = __import__(module_name)
        class_meta = getattr(module_meta, class_name)
        class_meta = getattr(class_meta, class_name)
        obj = class_meta(*args, **kwargs)
        return obj

    def run_chatshell(self, entity_dict):
        ccs = ChatCaller.ChatCallerShell()
        return ccs.do(entity_dict)

    def handle_call(self, session, entity_dict):
        if session[SessionControlFields.CURRENT_APP_KEY] is None:
            if entity_dict[FieldName.MsgType] != FieldName.text:
                return self.run_chatshell(entity_dict)
            content = entity_dict[FieldName.Content]
            content = content.strip()
            if content not in APPS.keys():
                return self.run_chatshell(entity_dict)
            else: #  open app
                session[SessionControlFields.CURRENT_APP_KEY] = content
                rep_str = u"进入应用：" + content
                return replyTextMessage(
                        entity_dict[FieldName.FromUserName],
                        entity_dict[FieldName.ToUserName],
                        rep_str
                    )
        # entering the app
        current_app_key = session[SessionControlFields.CURRENT_APP_KEY]
        app_class = APPS[current_app_key][0]
        module_name = APP_MODULE_PATH + "." + app_class
        app_obj = self.createAppInstance(module_name, app_class)
        rep_str = app_obj.do(session[SessionControlFields.APP_SESSION], entity_dict)
        if app_obj.LABEL_EXIT:
            sig_c(session)
        return rep_str
