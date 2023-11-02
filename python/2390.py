class Solution:
    def removeStars(self, s: str) -> str:
        star_i = s.find("*")
        while star_i != -1:
            # if there's a char to the left of the found star
            print(star_i)
            if star_i != 0 and s[star_i - 1] != "*":
                print("before: " + s)
                s = s[0 : star_i - 1] + s[star_i + 1 : len(s)]
                print("after: " + s)

            star_i = s.find("*")
        return s


print(Solution.removeStars(None, "leet**cod*e"))
