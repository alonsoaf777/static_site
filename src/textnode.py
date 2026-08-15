from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
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

def split_nodes_delimiter(
    old_nodes: list[TextNode], 
    delimiter: str, 
    text_type: TextType,
) -> list[TextNode]:

    textNodes = []
    curr_delimiter = ""
    delimiters = ["'","*","_"]
    delimiters_to_type = {
        "'": TextType.CODE,
        "**": TextType.BOLD,
        "_": TextType.ITALIC,
    }
    for oldNode in old_nodes:
        curr_text = oldNode.text
        while curr_text:
            found_delimiter = False
            for char_idx, char in enumerate(curr_text):
                if char in delimiters:
                    if char == "*":
                        if len(curr_text) == char_idx+1 or curr_text[char_idx+1] != "*":
                            continue
                    found_delimiter = True
                    curr_delimiter = char
                    if curr_delimiter == "*":
                        curr_delimiter = "**"
                    delimiter_cut_1 = curr_text.split(curr_delimiter, maxsplit=1)
                    if len(delimiter_cut_1) > 1 and delimiter_cut_1[0]:
                        textNodes.append(TextNode(delimiter_cut_1[0], TextType.TEXT))
                    delimiter_cut_2 = delimiter_cut_1[1].split(curr_delimiter, maxsplit=1)
                    if len(delimiter_cut_2) == 1:
                        raise Exception(f"No closing delimiter {curr_delimiter} in the text.")
                    textNodes.append(TextNode(delimiter_cut_2[0], delimiters_to_type[curr_delimiter]))
                    curr_text = delimiter_cut_2[1]
                    break
            if not found_delimiter:
                textNodes.append(TextNode(curr_text, TextType.TEXT)) 
                curr_text = ""
            
    return textNodes
