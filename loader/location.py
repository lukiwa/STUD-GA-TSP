class Location:
  def __init__(self, x: float, y: float):
    self.x = x
    self.y = y
  def __repr__(self):
    return f"Location=(X:{self.x},Y:{self.y})"