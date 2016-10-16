# class MathDojo(object):
#     def __init__(self):
#         self.sum=0
#     def add(self, num1, num2=0):
#         self.sum+=num1+num2
#         return self
#     def subtract(self, num1, num2=0):
#         self.sum+=-num1-num2
#         return self
#     def result(self):
#         print self.sum
#
# md=MathDojo()
# md.add(2).add(2,5).subtract(3,2).result()

class MathDojo(object):
    def __init__(self):
        self.sum=0
    def add(self, *num): #the * is a splat" operator and turns remaining arguements into a tuple
        list(num) #turns a tuple into a list
        for i in num:
            if type(i)==list:
                for num in i:
                    self.sum+=num
            else:
                self.sum+=i
        return self
    def subtract(self, *num):
        list(num)
        for i in num:
            if type(i)==list:
                for num in i:
                    self.sum-=num
            else:
                self.sum-=i
        return self
    def result(self):
        print self.sum

md=MathDojo()
md.add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2, [2,3],[1.1,2.3]).result()
