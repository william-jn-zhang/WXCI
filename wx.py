import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask
from flask import request
from config.MySessionInterface import MySessionInterface
from layer.resolver.BasicResolver import BasicResolver
from layer.controller.ChatController import ChatController
from layer.caller.ChatCaller import ChatCaller
app = Flask(__name__)
app.secret_key = 'william'
app.session_interface = MySessionInterface()


@app.route("/", methods=["GET", "POST"])
def run():
    br = BasicResolver()
    ccon = ChatController()
    ccal = ChatCaller()
    
    ccon.set_caller(ccal)
    br.set_controller(ccon)

    return br.handle_request(request)
