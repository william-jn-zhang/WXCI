import xml.dom.minidom as minidom
import time

def __appendChild(dom, root_node, child_name, child_content, use_CDATA=True):
    child_node = dom.createElement(str(child_name))
    content_node = None
    if use_CDATA:
        content_node = dom.createCDATASection(str(child_content))
    else:
        content_node = dom.createTextNode(str(child_content))
    child_node.appendChild(content_node)
    root_node.appendChild(child_node)
    return

def replyTextMessage(ToUserName, FromUserName, Content):
    dom = minidom.Document()
    root_node = dom.createElement("xml")
    dom.appendChild(root_node)
    __appendChild(dom, root_node, "ToUserName", ToUserName)
    __appendChild(dom, root_node, "FromUserName", FromUserName)
    __appendChild(dom, root_node, "CreateTime", time.time(), False)
    __appendChild(dom, root_node, "MsgType", "text")
    __appendChild(dom, root_node, "Content", Content)
    xml_string = root_node.toxml()
    return xml_string
