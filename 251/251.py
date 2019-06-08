class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.length = 0
        for vector in v:
            self.length += len(vector)
        def it():
            for vector in v:
                for num in vector:
                    self.length -= 1
                    yield num
        self.iterator = it()

    def next(self) -> int:
        return next(self.iterator)

    def hasNext(self) -> bool:
        return self.length > 0
