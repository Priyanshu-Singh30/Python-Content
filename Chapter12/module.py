def myfun():
    print("hello world!")

# myfun()
# print(__name__)

if __name__=="__main__":
    print("we are directly running this code")
    myfun()
    print(__name__)