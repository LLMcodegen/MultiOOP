class TAC:
    def The_array_contains(self, nums):
        if not nums:
            return []
        ranges = []
        start = nums[0]
        end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{end}")
                start = nums[i]
                end = nums[i]
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{end}")
        return ranges
#--------------:
#--------------:
print(TAC().The_array_contains([10, 11, 12, 14, 15, 17]) == ['10->12', '14->15', '17'])
print(TAC().The_array_contains([100, 101, 102, 105, 106, 108]) == ['100->102', '105->106', '108'])
print(TAC().The_array_contains([50, 52, 53, 55]) == ['50', '52->53', '55'])
