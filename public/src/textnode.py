from enum import Enum

class TextType(Enum):
    TEXT_TYPE_BOLD = "**Bold text**"
    TEXT_TYPE_ITALIC = "_Italic text_"
    TEXT_TYPE_CODE = "'Code text'"
    TEXT_TYPE_LINK = "[anchor text](url)"
    TEXT_TYPE_IMAGE = "![alt text](url)"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self == other

    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value}, {self.url}")

