class Solution(object):
    def intToRoman(self, num):
        dic = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        key_list = list(dic.keys())

        roman = ""
        count = 0

        while num > 0:

            if num >= key_list[count]:
                roman += dic[key_list[count]]
                num -= key_list[count]
            else:
                count += 1

        return roman