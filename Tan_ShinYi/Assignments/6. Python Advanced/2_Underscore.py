class Underscore(object):
    def mapping(self, list, callback):
        new=[]
        for i in list:
            new.append(callback(i))
        return new
    def reduce(self, list, callback):
        new=[]
        for i in list:
            new.append(callback(i))
        return new
    def finding(self, list, val):
        for i in list:
            if i==val:
                return True
        return False
    def filter(self, list, callback):
        new=[]
        for i in list:
            if callback(i):
                new.append(i)
        return new
    def reject(self, list, val):
        for i in list:
            if i==val:
                list.remove(i)
        return list

_ = Underscore()

evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print evens

mapping = _.mapping([1, 2, 3, 4, 5, 6], lambda x: x *2)
print mapping

finding = _.finding([1, 2, 3, 4, 5, 6], 0)
print finding

reject = _.reject([1, 2, 3, 4, 5, 6], 3)
print reject

reducing = _.reduce([1, 2, 3, 4, 5, 6], lambda x: x - 3)
print reducing
