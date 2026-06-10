from textnode import TextNode, TextType

def main():
    dummyNode = TextNode("This is some anchor text", TextType.LINK.value, "https://www.boot.dev")
    print(dummyNode)

if __name__ == "__main__":
    main()