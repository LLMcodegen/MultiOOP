from functools import cmp_to_key
class NNI:
    def Non_negative_integers(self, nums):
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        nums_str = list(map(str, nums))
        nums_str.sort(key=cmp_to_key(compare))
        largest_num = ''.join(nums_str)
        return '0' if largest_num[0] == '0' else largest_num
#--------------:
print(NNI().Non_negative_integers([0, 9, 8, 7]) == "9870")
print(NNI().Non_negative_integers([31, 3, 34, 5, 9]) == "9534331")
print(NNI().Non_negative_integers([0, 1, 2, 3, 4, 5]) == "543210")
