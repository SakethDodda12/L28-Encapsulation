class myClass:
    __privateVar = 27

    def __privMeth(self):
        print("Im inside class Myclass")
    def Hello(self):
        print("Private variable value: ", myClass.__privateVar)

foo = myClass()
foo.Hello()

foo._myClass__privMeth()
    