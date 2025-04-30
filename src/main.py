from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)
    props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    html_child = HTMLNode("tag1", "value1")
    html_node = HTMLNode("Tag", "Value", html_child, props)
    print(html_node)


main()
