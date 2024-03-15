class Cell:
    def __init__(self, x, y, z, visited=False):
        self.x = x
        self.y = y
        self.z = z
        self.blocked = True
        self.visited = visited
        self.stairs = None
    
    def to_dict(self):
        return dict(
            x=self.x,
            y=self.y,
            z=self.z,
            blocked=self.blocked,
            visited=self.visited,
            stairs=self.stairs["next_floor"].to_dict() if self.stairs and "next_floor" in self.stairs else None
        )
