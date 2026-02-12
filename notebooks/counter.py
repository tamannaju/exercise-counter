

class BaseCounter:
    def __init__(self, up_threshold, down_threshold):
        #super().__init__(up_threshold=150, down_threshold=90)
        self.stage = "up"
        self.count = 0
        #self.stage = None  # "up" or "down"
        self.up_threshold = up_threshold
        self.down_threshold = down_threshold

    def update(self, angle):
        if angle is None:
            return

        # Fully extended position
        if angle > self.up_threshold:
            self.stage = "up"

        # Bent position
        if angle < self.down_threshold and self.stage == "up":
            self.stage = "down"
            self.count += 1


class SquatCounter(BaseCounter):
    def __init__(self):
        # Squat knee angle thresholds
        super().__init__(up_threshold=160, down_threshold=90)


class PushupCounter(BaseCounter):
    def __init__(self):
        # Pushup elbow angle thresholds
        super().__init__(up_threshold=150, down_threshold=100)

class PullupCounter(BaseCounter):
    def __init__(self):
        # Pushup elbow angle thresholds
        super().__init__(up_threshold=150, down_threshold=70)
