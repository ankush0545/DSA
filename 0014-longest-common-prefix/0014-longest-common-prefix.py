class Solution(object):
    def longestCommonPrefix(self, strs):

        min_leng = min([len(i) for i in strs])

        str1 = ""

        for index in range(min_leng):

            check = True

            for j in range(len(strs) - 1):

                if strs[j][index] != strs[j + 1][index]:
                    check = False
                    break

            if check:
                str1 += strs[0][index]
            else:
                break

        return str1