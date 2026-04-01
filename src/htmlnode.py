class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        #a string that reps the HTML Tag name
        self.tag = tag
        #a string that reps the value of the HTML tag - text inside the paragraph
        self.value = value
        #a list of HTMLNode objects representing the children of this node
        self.children = children
        #A dictionary of key-value pairs reps the attributes of the HTML tag.  link <a> might have {"href": etc
        self.props = props


    def to_html(self):
        raise NotImplementedError("Not implemented yet")

    def props_to_html(self):
        #return (f"href={self.props[href]} target={self.props[target]}")

        if self.props is None:
            return ""
        
        props_html = ""
        
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        #print(f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props}") 
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"





