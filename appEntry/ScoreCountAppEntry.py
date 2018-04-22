'''
author: william.jn.zhang@gmail.com
'''
from appEntry.AppEntryBase import AppEntryBase
from myapp.scoreCount.ScoreCount import scoreCount
from wxapi.messageManagement.ReplyMessage import replyTextMessage
from wxapi.FieldName import FieldName

class ScoreCountAppEntry(AppEntryBase):
    _EXIT = "exit"

    def do(self, session, req_dict):
        content = req_dict[FieldName.Content]
        content = content.strip()
        if content == self._EXIT:
            self._exit()
            return replyTextMessage(
                    req_dict[FieldName.FromUserName],
                    req_dict[FieldName.ToUserName],
                    "bye!"
                )

        return scoreCount(session, req_dict)
