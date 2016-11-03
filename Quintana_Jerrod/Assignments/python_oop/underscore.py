class Underscore(object):
    def map(self, arr,  iteratee):
        # HIS CODE
        # return [iteratee(arr[index], index, arr) for index in range(len(arr))]
        #The Below code works but the above code is list comprehension, just condensed
        # values = []
        # for  index in range(len(arr)):
        #     val = arr[index]
        #     values.append(iteratee(val, index, arr))
        # return values

        # MY CODE
        newarr = []
        for index in arr:
            newarr.append(iteratee(index))
        return newarr
    def reduce(self, arr, iteratee, memo):
        for x in arr:
            memo = func(x, memo)
        return memo
    def find(self, arr, iteratee):
        for index in arr:
            if iteratee(index) == True:
                return index
        return False
    def filter(self, arr, iteratee):
        newarr = []
        for index in arr:
            if iteratee(index) == True:
                newarr.append(index)
        return newarr
    def reject(self, arr, iteratee):
        newarr = []
        for index in arr:
            if iteratee(index) == False:
                newarr.append(index)
        return newarr
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
# print _.map([1,2,3], lambda val: val * 2)
# print _.reduce([1, 2, 3, 4, 5, 6], (lambda x, y: x + y), 0)
# print _.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# print _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
