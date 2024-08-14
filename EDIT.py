class Solution:

    def editDistance(self, str1, str3):
        if str1 == str3:
            return 0

        len1 = len(str1)
        len2 = len(str3)

        if len1 < len2:
            str1, str3 = str3, str1
            len1, len2 = len2, len1

        prev = list(range(len2 + 1))
        curr = [0] * (len2 + 1)

        for i in range(1, len1 + 1):
            curr[0] = i
            for j in range(1, len2 + 1):
                if str1[i - 1] == str3[j - 1]:
                    cost = 0
                else:
                    cost = 1

                curr[j] = min(prev[j] + 1, curr[j - 1] + 1, prev[j - 1] + cost)

            prev, curr = curr, prev

        return prev[len2]
        # Code here
