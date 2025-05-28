class Solution(object):

    def get_digit_length_map(self, nums):
        result = []
        for num in nums:
            length = len(str(num))
            place = 10 ** (length - 1)
            decimal_places = length - 1
            format_string = "{:." + str(decimal_places) + "f}"
            Newnnum = format_string.format(float(num) / place)
            result.append(Newnnum)
        return result

    def multiply_value_Fun(self, digit_map):
         result = []
         for num in digit_map:
            length = len(str(num))
            if length == 1:
                place = 10 ** (length - 1)
            else:
                place = 10 ** (length - 2)
            Newnnum = int(float(num) * place)
            result.append(Newnnum)
         return result

    def largestNumber(self, nums):
        digit_map = self.get_digit_length_map(nums)
        divided_sort = sorted(digit_map, key=lambda x: (-float(x), x[::-1].find('.')), reverse=False)
        multiply_sort_list = self.multiply_value_Fun(divided_sort)
        print(divided_sort)
        res = ''.join(map(str, multiply_sort_list))
        print(res)
        return(res)


        # divided_list = self.divide_value_Fun(nums)
        # print(divided_list)
        # divided_sort = sorted(divided_list.items(), key=lambda x: x[1], reverse=True)
        # print(divided_sort)
        # multiply_sort_list = self.multiply_value_Fun(digit_map)
        # print(divided_list)

    #     doublenums = []
    #     for i in nums[:]:
    #         if i >= 10:
    #             doublenums.append(i)
    #             nums.remove(i)
    #     nums.sort(reverse=True)
    #     doublenums.sort(reverse=True)
    #     print("Sorted Doublenums:", doublenums)
    #     print("Sorted nums:", nums)
    #     return self.merger(nums, doublenums)   # ← return it

    # def merger(self, nums, doublenums):
    #     pointer = 0
    #     for i in doublenums:
    #         for r in nums:
    #             pointer += 1
    #             if i / 10 > r:
    #                 nums.insert(len(nums) - pointer, i)
    #             else:
    #                 nums.insert(len(nums), i)
    #                 break
    #         pointer = 0
    #     print("Final nums:", nums)
    #     return ''.join(map(str, nums))  # e.g. [10, 5, 2] → "1052"
