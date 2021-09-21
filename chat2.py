import pickle


def savepickle(msg):
    f = open("chat2.txt", "a")
    f.write(msg)


messages = []


while 1:
    start = input("type view to list all messages\ntype new to create a new message\n:")

    if start == "view":
        f = open("chat1.txt", "r")
        print(f.read())
    elif start == "new":
        new = input("new message: ")
        savepickle(new)