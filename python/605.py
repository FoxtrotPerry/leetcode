class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        flowerbed_clone = flowerbed
        valid_spots = 0

        for i in range(len(flowerbed)):
            plot = flowerbed_clone[i]
            if plot == 1:
                continue
            last_plot = flowerbed_clone[i - 1] or -1 if i > 0 else -1
            next_plot = flowerbed_clone[i + 1] or -1 if i < len(flowerbed) - 1 else -1
            print([last_plot, plot, next_plot])
            if last_plot != 1 and next_plot != 1:
                flowerbed_clone[i] = 1
                valid_spots += 1

        print(valid_spots)
        return valid_spots >= n


print(Solution.canPlaceFlowers(None, [0, 0, 1, 0, 0], 1))
