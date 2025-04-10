class Heap:
    def __init__(self):
        self.heap = [0]  # Заглушка на индексе 0

    def up(self, index):
        while index > 1 and self.heap[index] > self.heap[index // 2]:
            self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
            index = index // 2

    def down(self, index):
        while 2 * index < len(self.heap):
            left = 2 * index
            right = left + 1
            largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[left]:
                largest = right
            if self.heap[index] < self.heap[largest]:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def insert(self, k):
        self.heap.append(k)
        self.up(len(self.heap) - 1)

    def extract(self):
        result = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        if len(self.heap) > 1:
            self.down(1)
        return result

# Основная программа
n = int(input())
heap = Heap()
ans = []

for _ in range(n):
    command = input().split()
    if command[0] == '0':
        k = int(command[1])
        heap.insert(k)
    elif command[0] == '1':
        result = heap.extract()
        ans.append(result)

for res in ans:
    print(res)