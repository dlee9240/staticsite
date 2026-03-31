from textnode import TextNode, TextType
#print ("hello world")



def main():
    #print ("hello world")
    
    test = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print (test)


main()
