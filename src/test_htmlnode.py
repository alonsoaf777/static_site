import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_none_props(self):
        htmlnode = HTMLNode()
        assert(htmlnode.props_to_html() == "")
    
    def test_empty_props(self):
        htmlnode = HTMLNode(props = {})
        assert(htmlnode.props_to_html() == "")
    
    def test_w_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        expected = ' href="https://www.google.com" target="_blank"'
        htmlnode = HTMLNode(props = props)
        assert(htmlnode.props_to_html() == expected)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_w_props(self):
        expected = '<a href="https://www.google.com">Click me!</a>'
        leafNode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        assert(leafNode.to_html() == expected)
    
    def test_leaf_without_tag_value(self):
        expected = '<a href="https://www.google.com">Click me!</a>'
        leafNode = LeafNode("a", None, {"href": "https://www.google.com"})
        with self.assertRaises(ValueError):
            leafNode.to_html()
        leafNode = LeafNode(None, "Click me!", {"href": "https://www.google.com"})
        assert(leafNode.to_html() == "Click me!")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        expected = '<div><span>child</span></div>'
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), expected)

    def test_to_html_with_grandchildren(self):
        expected = "<div><span><b>grandchild</b></span></div>"
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            expected,
        )
    
    def test_href_parent_node(self):
        expected = '<a href="https://boot.dev">Click here</a>'
        leafChild = LeafNode(None, "Click here")
        parentNode = ParentNode("a", [leafChild], {'href': 'https://boot.dev'})
        print(parentNode.to_html())
        self.assertEqual(parentNode.to_html(), expected)

if __name__ == "__main__":
    unittest.main()