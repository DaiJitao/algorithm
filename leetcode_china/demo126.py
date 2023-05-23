

def demo126(beginword, endword, wordlist=[]):
    pass



class BaseModel(object):

    def __init__(self):
        self.name = self.get_name()

    def get_name(self):

        return "daijitao"


class BModel(BaseModel):

    def print(self):
        ls = self.name
        print(ls)
        if self.isFlag is None:
            self.isFlag = True
            print(self.isFlag)

        return self.isFlag


if __name__ == '__main__':
    BModel().print()