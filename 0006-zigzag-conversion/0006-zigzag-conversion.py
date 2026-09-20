class Solution:
    def convert(self, s: str, numRows: int) -> str:

        empty = [""] * numRows
        index = 0
        i = 0
        while i < len(s):
            empty[index] += s[i]
            i += 1
            index += 1
            if index == numRows:
                index = index - 2
                while index > 0 and i < len(s):
                    empty[index] += s[i]
                    i += 1
                    index -= 1

        return "".join(empty)

        