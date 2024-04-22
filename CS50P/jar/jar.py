class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        cookies = ""
        for _ in range(self.size):
            cookies += "🍪"
        return cookies

    def deposit(self, n):
        if (n + self.size) > self.capacity:
            raise ValueError("Jar too small")
        self.size += n


    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError("Too few cookies")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        try:
            int(capacity)
            if int(capacity) < 0:
                raise ValueError("Invalid capacity")
        except:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size <= self._capacity:
            self._size = size


