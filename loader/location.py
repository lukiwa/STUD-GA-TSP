from cmath import sqrt

class Location:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Location=(X:{self.x},Y:{self.y})"

    def calculate_distance(self, other) -> float:
        distance = sqrt((other.x - self.x)**2 + (other.y - self.y)**2).real
        return distance
