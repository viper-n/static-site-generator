from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

def main():
    nodes = [
        TextNode("This is *italic* and this is **bold**", TextType.TEXT)
    ]

    # First, let's see the output when processing just the bold delimiter
    bold_processed = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    print("After bold processing:")
    for node in bold_processed:
        print(f"- {node.text} ({node.text_type.name})")

    # Then, we should process the italic delimiter on the result of the first pass
    italic_processed = split_nodes_delimiter(bold_processed, "*", TextType.ITALIC)
    print("\nAfter italic processing:")
    for node in italic_processed:
        print(f"- {node.text} ({node.text_type.name})")

main()
