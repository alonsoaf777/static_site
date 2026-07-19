class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        if not self.props:
            return ""
        return "".join(
            [f' {key}="{val}"' for key, val in self.props.items()]
        )
    
    def __repr__(self):
        return f"tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props_to_html()}"


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("No value provided.")
        if self.tag is None or not self.tag:
            return f"{self.value}"
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"tag: {self.tag}\nvalue: {self.value}\nprops: {self.props_to_html()}"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props = None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if self.tag is None or not self.tag:
            raise ValueError("No tag provided.")
        if self.children is None or not self.children:
            raise ValueError("No children detected.")
        children_format = ''
        for leafChild in self.children:
            children_format+= leafChild.to_html()

        return f'<{self.tag}{self.props_to_html()}>{children_format}</{self.tag}>'