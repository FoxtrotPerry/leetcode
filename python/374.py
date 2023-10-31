# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        clue = 32
        min_val = 1
        max_val = n
        while clue != 0:
            guess_num = (min_val + max_val) / 2
            clue = guess(guess_num)
            if clue == 0:
                return int(guess_num)
            elif clue == -1:
                max_val = guess_num
            else:
                min_val = guess_num
