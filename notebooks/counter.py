class SquatCounter:
    def __init__(self, down_thresh=90, up_thresh=160):
        self.down_thresh = down_thresh
        self.up_thresh = up_thresh

        self.count = 0
        self.state = "UP"

    def update(self, knee_angle):
        """
        Updates count based on knee angle.
        Returns current count and state.
        """

        if knee_angle is None:
            return self.count, self.state

        if knee_angle < self.down_thresh and self.state == "UP":
            self.state = "DOWN"

        elif knee_angle > self.up_thresh and self.state == "DOWN":
            self.count += 1
            self.state = "UP"

        return self.count, self.state
