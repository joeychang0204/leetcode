class Vector2D:
    # convert to 1d array
    def __init__(self, v: List[List[int]]):
        self.ptr = 0
        self.v = []
        for vector in v:
            self.v += vector

    def next(self) -> int:
        self.ptr += 1
        return self.v[self.ptr-1]

    def hasNext(self) -> bool:
        return self.ptr < len(self.v)
