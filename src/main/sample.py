import objc
NSObject = objc.lookUpClass('NSObject')

class FooBar(object):

    def __init__(self):
        self.strings = ['foo', 'bar', 'baz']

    def count(self):
        return len(self.strings)

    def string_at_index(self, index):
        return self.strings[index]

class PyFoobar(NSObject):
    def init(self):
        self = super(PyFoobar, self).init()
        self.py = FooBar()
        return self

    @objc.signature('i@:')
    def count(self):
        return self.py.count()

    @objc.signature('@@:i')
    def stringAtIndex_(self, index):
        return self.py.string_at_index(index)