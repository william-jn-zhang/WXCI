from app.AppEntryBase import AppEntryBase
from wxapi.messageManagement.ReplyMessage import replyTextMessage
from wxapi.FieldName import FieldName

class TestAppEntry(AppEntryBase):

    def do(self, session, req_dict):
        return replyTextMessage(
                req_dict[FieldName.FromUserName],
                req_dict[FieldName.ToUserName],
                "Congratulations! Test success!"
            )
