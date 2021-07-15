from math import sqrt
import heapq


class Point2:
    def __init__(self, x, y, previous=None):
        self.x = x
        self.y = y
        self.area = 0
        self.next = None
        self.previous = previous

    def set_next(self, next):
        self.next = next

    def delete_from_list(self):
        if self.next is not None:
            self.next.previous = self.previous
        if self.previous is not None:
            self.previous.next = self.next

    def update_area(self):
        if self.previous is not None and self.next is not None:
            a = sqrt(pow(abs(self.previous.x - self.x), 2) + pow(abs(self.previous.y - self.y), 2))
            b = sqrt(pow(abs(self.next.x - self.x), 2) + pow(abs(self.next.y - self.y), 2))
            c = sqrt(pow(abs(self.previous.x - self.next.x), 2) + pow(abs(self.previous.y - self.next.y), 2))
            p = (a + b + c) / 2
            self.area = sqrt(abs(p * (p - a) * (p - b) * (p - c)))

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __eq__(self, other):
        if isinstance(other, Point2):
            return self.x == other.x and self.y == other.y
        else:
            return False

    @staticmethod
    def list_points_to_lists(points: list) -> tuple:
        return [(p.x, p.y) for p in points]

    @staticmethod
    def xy_to_points2_double_list(x: list, y: list):
        head = Point2(x[0], y[0])
        prev = head
        listAll = [head]
        for i in range(1, len(x)):
            newPoint = Point2(x[i], y[i], prev)
            prev.set_next(newPoint)
            prev = newPoint
            listAll.append(prev)
        return listAll


def visvalingam_whyatt2(list, epsilon):
    head, tail = list.pop(0), list.pop(-1)
    for point in list:
        point.update_area()

    heapq.heapify(list)
    point = heapq.heappop(list)
    while point.area < epsilon and len(list) > 0:
        prev = point.previous
        point.delete_from_list()
        prev.update_area()
        prev.next.update_area()
        heapq.heapify(list)
        point = heapq.heappop(list)
    heapq.heappush(list, point)

    returnList = [head]
    while head.next is not None:
        returnList.append(head.next)
        head = head.next

    return returnList
