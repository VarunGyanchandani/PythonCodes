def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Done")

@greet
def hello():
    print("Hello World")

