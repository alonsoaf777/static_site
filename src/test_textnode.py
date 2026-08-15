import unittest
from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_none_entry(self):
        node = TextNode("This is a text node", TextType.LINK)
        assert(node.url is None)
        node2 = TextNode("This is a text node", TextType.BOLD, "Bold text")
        assert(node2.url is not None)

class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        expected = "<b>This is a bold node</b>"
        self.assertEqual(html_node.to_html(), expected)
    
    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        expected = "<i>This is an italic node</i>"
        self.assertEqual(html_node.to_html(), expected)

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        expected = "<code>This is a code node</code>"
        self.assertEqual(html_node.to_html(), expected)
    
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "testurl.com")
        html_node = text_node_to_html_node(node)
        expected = '<a href="testurl.com">This is a link node</a>'
        self.assertEqual(html_node.to_html(), expected)
    
    def test_image(self):
        node = TextNode("This is a image node", TextType.IMAGE, "testurl.com")
        html_node = text_node_to_html_node(node)
        expected = '<img src="testurl.com" alt="This is a image node"></img>'
        self.assertEqual(html_node.to_html(), expected)

class TestSplitter(unittest.TestCase):
    def test_splitter_italic(self):
        node = TextNode("This is a text with _italic_ words.", TextType.BOLD)
        nodes = split_nodes_delimiter([node], "", "")
        self.assertEqual(len(nodes), 3)
        italic_node = nodes[1]
        self.assertEqual(italic_node.text_type, TextType.ITALIC)
    
    def test_splitter_bold(self):
        node = TextNode("This is a text with **bold** words.", TextType.BOLD)
        nodes = split_nodes_delimiter([node], "", "")
        self.assertEqual(len(nodes), 3)
        bold_node = nodes[1]
        self.assertEqual(bold_node.text_type, TextType.BOLD)

    def test_splitter_code(self):
        node = TextNode("This is a text with 'code' words.", TextType.BOLD)
        nodes = split_nodes_delimiter([node], "", "")
        self.assertEqual(len(nodes), 3)
        code_node = nodes[1]
        self.assertEqual(code_node.text_type, TextType.CODE)
    
    def test_splitter_boundaries(self):
        node = TextNode("Testing splitter **boundaries**", TextType.BOLD)
        nodes = split_nodes_delimiter([node], "", "")
        self.assertEqual(len(nodes), 2)
        test_node = nodes[1]
        self.assertEqual(test_node.text_type, TextType.BOLD)
    
    def test_big_splitter(self):
        node = TextNode("This _text has_ all the **existing nodes** for 'testing.'", TextType.BOLD)
        nodes = split_nodes_delimiter([node], "", "")
        self.assertEqual(len(nodes), 6)

    def test_incomplete_splliter(self):
        node = TextNode("This _text type is incomplete.", TextType.ITALIC)
        with self.assertRaises(Exception):
            nodes = split_nodes_delimiter([node], "", "")

if __name__ == "__main__":
    unittest.main()