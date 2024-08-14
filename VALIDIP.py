#User function Template for python3
class Solution:

    def isValid(self, str):

        def to_string(num):

            result = ""
            while num > 0:
                result = chr(num % 10 + ord('0')) + result
                num //= 10
            return result if result else "0"

        list1 = str.split('.')
        count = 0
        if len(list1) != 4:
            return False

        for i in list1:
            if not i.isdigit():
                return False
            num = int(i)
            if i != to_string(num):
                return False

            if not (0 <= num <= 255):
                return False

        return True
