from functools import reduce

inp = [int(c) for c in "467528193"]


def input_nodes():
    arr = [i for i in inp]
    first = Cup(arr[0])
    last = reduce(lambda acc, i: acc.extend(Cup(i)), arr[1:], first)
    return last.extend(first)


class Cup:
    def __init__(self, i):
        self.i = i
        self.succ = None

    def extend(self, succ):
        self.succ = succ
        return succ

    def destination_cup(self):
        imapping = {self.i: self}
        csr = self.succ
        while csr != self:
            imapping[csr.i] = csr
            csr = csr.succ

        ids = list(sorted(imapping.keys()))
        resid = ids[ids.index(self.i) - 1]
        return imapping[resid]

    def __getitem__(self, key):
        if isinstance(key, slice):
            res = []
            csr = self
            for i in range(0, key.stop):
                if i in range(key.start, key.stop):
                    res += [csr]
                csr = csr.succ
        else:
            res = self
            for _ in range(key):
                res = res.succ

        return res

    def remove(self, start, stop):
        res = []
        csr = self
        for i in range(0, stop):
            if i in range(start, stop):
                res += [csr]
            csr = csr.succ
        # keep the chain intact
        res[0].prev().succ = res[-1].succ
        return res

    def prev(self):
        res = self
        while res.succ != self or res is None:
            res = res.succ
        return res

    def all(self):
        res = [self]
        csr = self.succ
        while csr != self:
            res.append(csr)
            csr = csr.succ
        return res

    def find(self, i):
        csr = self
        while i != csr.i:
            csr = csr.succ
        return csr

    def __setitem__(self, key, value):
        if isinstance(value, list):
            for v in reversed(value):
                self[key] = v
        else:
            prev = self[key - 1]
            after = self[key]
            prev.succ = value
            value.succ = after

    def __iter__(self):
        return iter(self.all())

    def __int__(self):
        return self.i

    def __str__(self):
        return str(self.i)

    def __repr__(self):
        me = "({})".format(self.i)
        other = " ".join([str(n.i) for n in self[1:9]])
        return " ".join([me, other])


def part1(moves=100):
    csr = input_nodes()
    for i in range(moves):
        taken = csr.remove(1, 4)
        dest = csr.destination_cup()
        dest[1] = taken

        csr = csr[1]
        if i % 1_000_000 == 0:
            print(i)

    return "".join([str(n) for n in csr.find(1)]).replace("1", "")


# 43769582
print(part1(100))
#
#print(part1(10_000_000))
