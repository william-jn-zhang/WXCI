import json
from flask.sessions import SessionInterface
from flask.sessions import SessionMixin
from wxapi.messageManagement.ReceiveMessage import receiveMessage

class MySession(dict, SessionMixin):
    def __init__(self, initial=None, sid=None):
        self.sid = sid
        self.initial = initial
        super(MySession, self).__init__(initial or ())

    def __setitem__(self, key, value):
        super(MySession, self).__setitem__(key, value)

    def __getitem__(self, item):
        return super(MySession, self).__getitem__(item)

    def __delitem__(self, key):
        super(MySession, self).__delitem__(key)


class MySessionInterface(SessionInterface):
    session_class = MySession
    container = {}

    def open_session(self, app, request):
        msg_dict = receiveMessage(request.data)
        userId = msg_dict['FromUserName']
        session_json_str = self.container.get(userId)
        if session_json_str is not None:
            data = json.loads(session_json_str)
            return self.session_class(data, sid=userId)
        return self.session_class(sid=userId)

    def save_session(self, app, session, response):
        session_json_str = json.dumps(dict(session))
        self.container[session.sid] = session_json_str
        return
