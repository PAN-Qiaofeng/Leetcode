'''
Description: 
version: 
Author: pqf
Date: 2021-03-23 14:47:28
LastEditors: pqf
LastEditTime: 2021-03-25 15:53:39
'''

class Fibonacci(object):
    mod_sum = int(1e9+7)


    @classmethod
    def getModsum(cls):
        print(cls.mod_sum)

    
    def count(self, n):
        """This function is too slow to print the result since too many overlap iterations in the process, e,g., there are two calculations that are same in f(3) and f(4).

        Args:
            n ([int]): [n is te number to count]

        Returns:
            [int]: [the value returned is the result of iteration]
        """
        ## the exit when n ==0
        if n == 0:
            return 0
        ## the exit when n ==1    
        elif n== 1:
            return 1
        ## the interation
        else:
            return (self.count(n-1) + self.count(n-2))%self.mod_sum

    def count2(self, n):
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a+b
        return a%self.mod_sum

def main():
    test = Fibonacci()
    test.getModsum()
    n = test.count2(50)
    print(n)


if __name__ == "__main__":
    main()