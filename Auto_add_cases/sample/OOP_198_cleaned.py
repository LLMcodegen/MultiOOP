
import heapq

class NCT:
    def __init__(self, courses):
        self.courses = courses
    def __private_Number_courses_taken(self):
        self.courses.sort(key=lambda x: x[1])
        pq = []
        time = 0
        for duration, lastDay in self.courses:
            if time + duration <= lastDay:
                heapq.heappush(pq, -duration)
                time += duration
            elif pq and -pq[0] > duration:
                time += duration + heapq.heappop(pq)
                heapq.heappush(pq, -duration)
        return len(pq)
    def public_Number_courses_taken(self):
        return self.__private_Number_courses_taken()

#--------------:
print(NCT([[3, 6], [2, 5], [5, 10], [1, 7]]).public_Number_courses_taken() == 3)
print(NCT([[2, 3], [3, 5], [4, 6], [5, 7]]).public_Number_courses_taken() == 2)
print(NCT([[1, 3], [2, 4], [3, 5], [4, 6]]).public_Number_courses_taken() == 2)
