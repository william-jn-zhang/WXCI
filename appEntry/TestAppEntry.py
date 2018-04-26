from appEntry.AppEntryBase import AppEntryBase
from wxapi.messageManagement.ReplyMessage import replyTextMessage
from wxapi.FieldName import FieldName

class TestAppEntry(AppEntryBase):

    EXIT = "exit"

    def do(self, session, req_dict):
        content = req_dict[FieldName.Content]
        content = content.strip()
        if content == self.EXIT:
            self._exit()
            return replyTextMessage(
                    req_dict[FieldName.FromUserName],
                    req_dict[FieldName.ToUserName],
                    "bye!"
                )

        return replyTextMessage(
                req_dict[FieldName.FromUserName],
                req_dict[FieldName.ToUserName],
                "Congratulations! Test success!"
            )
