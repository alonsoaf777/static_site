import unittest
from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()