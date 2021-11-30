class Configuration:
    def __init__(self, x: float, y: float, h: float):
        self.x = x  # The x-coordinate.
        self.y = y  # The y-coordinate.
        self.h = h  # The heading angle i.e. orientation.

    def to_string(self):
        return f"Cfg(x = {self.x}, y = {self.y}, h = {self.h})"
