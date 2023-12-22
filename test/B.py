class B:
    def __init__(self):
        pass

    def foo(self, age: int, mylist):
        age += 1
        for i in range(len(mylist)):
            mylist[i] += 1
