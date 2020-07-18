def announce(f):
    def wrapper():
        print("about to run it")
        f()
        print("done / with")

    return wrapper()


@announce
def hello():
    print("say Hello")


hello()
