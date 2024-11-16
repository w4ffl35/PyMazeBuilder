class Cell:
    def __init__(self, x, y, z, visited=False):
        self.x = x
        self.y = y
        self.z = z
        self._blocked = True
        self.visited = visited
        self.stairs = None

    @property
    def blocked(self) -> bool:
        return self._blocked

    @blocked.setter
    def blocked(self, value: bool):
        self._blocked = value
    
    def to_dict(self):
        return dict(
            x=self.x,
            y=self.y,
            z=self.z,
            blocked=self.blocked,
            visited=self.visited,
            stairs=self.stairs["next_floor"].to_dict() if self.stairs and "next_floor" in self.stairs else None
        )

    @classmethod
    def from_dict(cls, data: dict):
        cell = cls(data['x'], data['y'], data['z'], data['visited'])
        cell.blocked = data['blocked']
        cell.stairs = data['stairs']
        return cell
