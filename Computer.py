# 2021/01/25(월)

class Computer:
    def __init__(self, nlist=[]):
        self.nlist = nlist

    def add(self):
        tot = 0
        for i in self.nlist:
            tot += i
        return tot

    def mean(self):
        ave = self.add() / len(self.nlist)
        return ave

if __name__ == '__main__':
    a = Computer([10, 20, 30, 40, 50])
    print(a.add())
    print(a.mean())



