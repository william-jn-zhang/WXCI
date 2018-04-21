'''
author: william.jn.zhang@gmail.com
'''
import xml.sax


class __TextMessageHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.val = {}
        self.currentData = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag

    def endElement(self, tag):
        self.CurrentData = ""

    def characters(self, content):
        self.val[self.CurrentData] = content

# put message into a dict
def receiveMessage(xmlString):
    handler = __TextMessageHandler()
    xml.sax.parseString(xmlString, handler)
    val = handler.val
    return val
