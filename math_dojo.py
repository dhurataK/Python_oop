# PART I
class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *nums):
        for num in nums:
            self.result += num
        return self

    def subtract(self, *nums):
        for num in nums:
            self.result -= num
        return self

print MathDojo().add(2).add(2, 5).subtract(3, 2).result

# PART II
class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *nums):
        for num in nums:
            if isinstance(num, list):
                for idx in num:
                    self.result += idx
            else:
                self.result += num
        return self

    def subtract(self, *nums):
        for num in nums:
            if isinstance(num, list):
                for idx in num:
                    self.result -= idx
            else:
                self.result -= num
        return self


print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result

#PART III
class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *nums):
        for num in nums:
            if isinstance(num, (list, tuple)):
                for idx in range(0,len(num)):
                    self.result += num[idx]
            else:
                self.result += num
        return self

    def subtract(self, *nums):
        for num in nums:
            if isinstance(num, (list, tuple)):
                for idx in range(0,len(num)):
                    self.result -= num[idx]
            else:
                self.result -= num
        return self

print MathDojo().add([1,3,4],3,(1,1,1),4).subtract([3, 1, 1], (2, 4),1).result
