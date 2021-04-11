'''
Description: 
version: 
Author: pqf
Date: 2021-03-25 17:04:46
LastEditors: pqf
LastEditTime: 2021-03-28 19:50:06
'''
class ReplaceSpace(object):
    
    @staticmethod
    def replaceSpace(s :str):
        res = []
        for str in s:
            if str ==" ":
                res.append("%20")
            else:
                res.append(str)
        return "".join(res)


def main():
    print("test")


if __name__=="__main__":
    main()