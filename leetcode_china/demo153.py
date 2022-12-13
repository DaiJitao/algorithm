

def demo153(nums):
    pass


class BaseCLS(object):

    def __init__(self, prefix):
        self.prefix = prefix
        super(BaseCLS, self).__init__()


    def merge_all(self, p):
        inputs, outputs = p
        inputs = self.convert(inputs)
        outputs = self.processOuts(outputs)
        print(inputs, outputs)


    def convert(self, inputs):
        raise NotImplementedError

    def processOuts(self, outputs):
        raise NotImplementedError


class MyCLS(BaseCLS):

    def convert(self, inputs):
        return self.prefix +  ' inputs:{}'.format(inputs)

    def processOuts(self, outputs):
        return self.prefix + ' outputs:{}'.format(outputs)

if __name__ == '__main__':
    p = ('my name', 'Demo')
    cls = MyCLS('start')
    cls.merge_all(p)


