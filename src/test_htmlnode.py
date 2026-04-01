import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "Test paragraph", None, None)
        node2 = HTMLNode("a", "Test paragraph", None, None)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()

