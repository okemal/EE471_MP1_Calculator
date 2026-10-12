class Calculator:
    def __init__(self) -> None:
        self._current_val = 0

    def add(self, x, y):
        self._current_val = x + y
    def subtract(self, x, y):
        self._current_val = x - y
    def multiply(self, x, y):
        self._current_val = x * y
        return self._current_val
