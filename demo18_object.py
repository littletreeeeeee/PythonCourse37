class Foo:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '[Foo]:Str 格式:%s' % (self.name)

    def __repr__(self):
        return '[Foo]:repr 格式:s%s' % (self.name)


f1 = Foo('hello world \n')
f2 = Foo('mark')
print(f1, f2)
print('%s,%r' % (f1, f1))
print('{0!s}, {0!r}, {0!a}'.format(f1))
