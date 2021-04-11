'''
Description: 
version: 
Author: pqf
Date: 2021-03-25 16:42:23
LastEditors: pqf
LastEditTime: 2021-03-25 16:59:50
'''
class FindRepeatNumber(object):
    
    @staticmethod
    def findRepeatNumber1(nums: list):
        temp = set()
        tp_count = len(temp)
        for item in nums:
            temp.add(item)
            if len(temp) == tp_count:
                return item
            else:
                tp_count =  len(temp)


    @staticmethod
    def findRepeatNumber2(num:list):
        temp = sorted(num)
        for i in range(len(temp)):
            if temp[i] == temp[i+1]:
                return temp[i]


def main():
    test = FindRepeatNumber.findRepeatNumber1([2, 3, 1, 0, 2, 5, 3])
    test2 = FindRepeatNumber.findRepeatNumber2([2, 3, 1, 0, 2, 5, 3])
    print(test)
    print(test2)


if __name__ == "__main__":
    main()