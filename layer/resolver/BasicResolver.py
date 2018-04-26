'''
author: william.jn.zhang@gmail.com
'''
from flask import request
from wxapi.VerifyServer import verifyServer
from wxapi.messageManagement.ReceiveMessage import receiveMessage
from wxapi.FieldName import FieldName

# resolver implement:
#     extract request xml string
#     verify wechat server
#     encrypt and decrypt
#     send resolved data to controller
class BasicResolver:

    def handle_request(self, request):
        signature = ""
        timestamp = ""
        nonce = ""

        try:
            signature = request.args.get(FieldName.signature)
            timestamp = request.args.get(FieldName.timestamp)
            nonce = request.args.get(FieldName.nonce)
        except KeyError, e:
            print("in file %s, request.args.get() KeyError!" % __file__)
            return FieldName.success

        # verify wechat server
        if signature == "":
            return FieldName.success
        verify = verifyServer(signature, timestamp, nonce)
        if not verify:
            print("in file %s, verify failed!" % __file__)
            return FieldName.success
        if request.data == "":
            echostr = ""
            try:
                echostr = request.args.get(FieldName.echostr)
            except KeyError, e:
                print("in file %s, request.args.get(echostr) failed" % __file__)
            return echostr

        # resolve request
        msg_dict = receiveMessage(request.data)
        print("in file %s, %s" % (__file__, str(msg_dict)))
        return self.call_controller(msg_dict)

    def set_controller(self, Controller):
        self.controller = Controller
        return

    def call_controller(self, msg_dict):
        return self.controller.handle_entity(msg_dict)
