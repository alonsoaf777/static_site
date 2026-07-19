from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if self.text != other.text:
            return False
        if self.text_type != other.text_type:
            return False
        if self.url != other.url:
            return False
        return True
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type not in list(TextType):
        raise Exception("Invalid TextType.")
    textType = text_node.text_type
    textVal = text_node.text
    textURL = text_node.url
    if textType == TextType.TEXT:
        return LeafNode(None, textVal)
    elif textType == TextType.BOLD:
        return LeafNode("b", textVal)
    elif textType == TextType.ITALIC:
        return LeafNode("i", textVal)
    elif textType == TextType.CODE:
        return LeafNode("code", textVal)
    elif textType == TextType.LINK:
        return LeafNode("a", textVal, {"href":textURL})
    elif textType == TextType.IMAGE:
        return LeafNode("img", "", {"src":textURL, "alt":textVal})