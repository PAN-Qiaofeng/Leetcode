'''
Description: 
version: 
Author: pqf
Date: 2021-03-26 13:54:17
LastEditors: pqf
LastEditTime: 2021-03-26 14:58:29
'''
class MinArray(object):
    
    @staticmethod
    def minArrayError(numbers :list):
        length = len(numbers)
        flag = length % 2
        if flag:
            end = int((length - 1)/2)
            for i in range(end):
                numbers[i], numbers[i + end + 1] = numbers[i + end + 1], numbers[i]
        else:
            end = int(length / 2)
            for i in range(end):
                numbers[i], numbers[i + end + 1] = numbers[i + end + 1], numbers[i]

        return numbers[0]


    @staticmethod
    def minArray(numbers :list):
        i = 0
        j = len(numbers) -1 
        while i < j:
            m = (i + j) // 2
            if numbers[m]  > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j  = m
            else:
                j -= 1


        return numbers[i]
        

def main():
    test = [2, 2, 2, 0, 1]
    print(MinArray.minArray(test))


if __name__ == "__main__":
    main()