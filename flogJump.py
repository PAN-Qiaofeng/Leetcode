'''
Description: 
version: 
Author: pqf
Date: 2021-03-25 16:10:12
LastEditors: pqf
LastEditTime: 2021-03-25 16:35:06
'''
class FlogJump(object):
    md_num = int(1e9+7)

    @classmethod
    def setMdnum(cls, num):
        cls.md_num = num
    
    #compute he sum of methods for jump to n level#
    @classmethod
    def countWays(cls, num):
        a = 1
        b = 1
        for _ in range(num):
            a, b = b, a + b
        return a % cls.md_num


def main():
    test = FlogJump.countWays(100)
    print(test)


if __name__ == "__main__":
    main()