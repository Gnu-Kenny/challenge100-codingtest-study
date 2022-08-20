# https://www.acmicpc.net/problem/1966

from collections import deque
from queue import SimpleQueue
import sys
input = sys.stdin.readline


class Doc:
    def __init__(self, priority, idx):
        self._priority = priority
        self._idx = idx

    def __lt__(self, other):
        return self._priority < other._priority

    def __str__(self):
        return f'priority = {self._priority}, idx = {self._idx}'


class MaxQueue:
    def __init__(self):
        self._queue = SimpleQueue()
        self._max = deque()

    def enqueue(self, value: list):
        self._queue.put(value)

        # _max의 뒤에서부터 유효성 검사를 진행
        # _max 가장 끝자리가 현재 들어오려는 값보다 작다면 반환
        #   ex) _max = [3,2] <- 7 이라면 뒷자리 2부터 순차적으로 값을 반환하고 [7]
        while len(self._max) > 0 and value > self._max[-1]:
            self._max.pop()
        self._max.append(value)

    def dequeue(self):
        if self._queue.qsize() == 0:
            raise RuntimeError("queue is empty")

        value = self._queue.get()

        if value == self._max[0]:
            self._max.popleft()
        return value

    def getMax(self):
        if self._queue.qsize() == 0:
            raise RuntimeError("queue is empty")
        return self._max[0]

    def qsize(self):
        return self._queue.qsize()

    def __str__(self):
        return "qsize = " + str(self._queue.qsize())


def main():

    # 테스트케이스 개수 만큼 순환
    for _ in range(int(input())):
        docs_num, doc_idx = map(int, input().split())

        # 중복된 숫자에 대해 구별이 가능하도록 각 숫자를 idx와 함께 저장하는 배열 초기화
        docs = list(map(int, input().split()))

        queue = MaxQueue()

        for i, pr in enumerate(docs):
            doc = Doc(pr, i)
            queue.enqueue(doc)

        cnt = 0
        while queue.qsize() != 0:
            max_priority: int = queue.getMax()._priority
            doc: Doc = queue.dequeue()  # [1,2,3,4] -> 1, [2,3,4]

            if doc._priority == max_priority:  # 4, [1,2,3] -> return 4
                cnt += 1
                if doc._idx == doc_idx:
                    break
            else:                             # 2, [3,4,1] -> [3,4,1,2]
                queue.enqueue(doc)

        print(cnt)


if __name__ == "__main__":
    main()
