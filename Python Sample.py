print("hello")
name="Pranesh"
a=10
print(f"my name is {a}")

class calci:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return "blast"


class calxi2(calci):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
p1=calxi2(2,3,4)
print(p1.c)


