
from collections import Counter
import heapq

class ABD:
    def __init__(self, barcodes):
        self.barcodes = barcodes
class SN_ABD(ABD):
    def Adjacent_barcodes(self):
        count = Counter(self.barcodes)
        heap = [(-freq, barcode) for barcode, freq in count.items()]
        heapq.heapify(heap)
        result = []
        prev_freq, prev_barcode = 0, None
        while heap:
            freq, barcode = heapq.heappop(heap)
            result.append(barcode)
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_barcode))
            freq += 1
            prev_freq, prev_barcode = freq, barcode
        return result

#--------------:
print(SN_ABD([5,5,5,6,6,6,7,7,7]).Adjacent_barcodes() == [5, 6, 7, 5, 6, 7, 5, 6, 7])
print(SN_ABD([9,9,9,1,1,1,2,2]).Adjacent_barcodes() == [1, 9, 1, 2, 9, 1, 2, 9])
print(SN_ABD([4,4,4,5,5,6,6]).Adjacent_barcodes() == [4, 5, 4, 6, 4, 5, 6])
