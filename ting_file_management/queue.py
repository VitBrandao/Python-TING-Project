class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        first_item = self.data[0]
        self.data.remove(first_item)

        return first_item

    def search(self, index):
        last_item = self.data[-1]
        last_item_index = self.data.index(last_item)

        if 0 <= index <= last_item_index:
            return self.data[index]

        raise IndexError
