from time import monotonic


class Timer:

    start_time = monotonic()
    timer = 0

    def update_timer(self):
        self.timer = monotonic() - self.start_time

    def update_start_time(self):
        self.start_time = monotonic()


timer = Timer()

