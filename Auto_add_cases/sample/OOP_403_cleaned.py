
class PWL:
    def __init__(self, hours):
        self.hours = hours
class SN_PWL(PWL):
    def Performing_well(self):
        hours = self.hours
        presum = 0
        max_len = 0
        hashmap = {}
        for i in range(len(hours)):
            if hours[i] > 8:
                presum += 1
            else:
                presum -= 1
            if presum > 0:
                max_len = i + 1
            else:
                if presum not in hashmap:
                    hashmap[presum] = i
                if (presum - 1) in hashmap:
                    max_len = max(max_len, i - hashmap[presum - 1])
        return max_len

#--------------:
print(SN_PWL([9, 6, 6, 9, 9]).Performing_well() == 5)
print(SN_PWL([9, 6, 6, 6, 9]).Performing_well() == 1)
print(SN_PWL([9, 6, 9, 6, 6]).Performing_well() == 3)
