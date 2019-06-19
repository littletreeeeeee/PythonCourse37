class MyClass:
    pass


print("my class type:", type(MyClass))
i1 = MyClass()
print("i1 type:", type(i1))
print("i1 class:", i1.__class__)
print("i1 class bases:", i1.__class__.__bases__)
print("i1 type equal to myClass?", type(i1) == MyClass)
