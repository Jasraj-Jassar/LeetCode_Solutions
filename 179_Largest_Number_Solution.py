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
        print("Digit length normalized map:", result)
        return result

    def multiply_value_Fun(self, digit_map):
        result = []
        for num in digit_map:
            Newnnum = int(str(num).replace('.', ''))
            print("TESTING_D:", Newnnum )
            result.append(Newnnum)
        print("Multiplied list:", result)
        return result

    def largestNumber(self, nums):
        print("Original input:", nums)

        digit_map = self.get_digit_length_map(nums)
        
        divided_sort = sorted(digit_map, key=lambda x: (-float(x), x[::-1].find('.')), reverse=False)
        print("Sorted digit map (A):", divided_sort)

        divided_sort_b = sorted(digit_map, key=lambda x: (-float(x), x[::-1].find('.')), reverse=True)
        print("Sorted digit map (B):", divided_sort_b)

        multiply_sort_list = self.multiply_value_Fun(divided_sort)
        print("Result from multiply A:", multiply_sort_list)

        multiply_sort_list_b = self.multiply_value_Fun(divided_sort_b)
        print("Result from multiply B:", multiply_sort_list_b)

        res = ''.join(map(str, multiply_sort_list))
        res_b = ''.join(map(str, multiply_sort_list_b))
        print("Concatenated Result A:", res)
        print("Concatenated Result B:", res_b)

        if int(res) > int(res_b):
            return res
        elif int(res) == 0:
            return "0"
        else:
            return res_b

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
