class Solution:
    def kidsWithCandies(self, candies: [int], extraCandies: int) -> [bool]:
        give_list = []
        max_candies = 0
        for kids_candies in candies:
            if kids_candies > max_candies:
                max_candies = kids_candies

        for kids_candies in candies:
            if kids_candies + extraCandies >= max_candies:
                give_list.append(True)
            else:
                give_list.append(False)

        return give_list
