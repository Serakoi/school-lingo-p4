import threading

# Timer hell :")

class Timer:
    def __init__(self):
        self.start_time = None
        self.time_elapsed = 0

    # start timer to calculate score
    def start(self):
        self.start_time = threading.Timer(0.1, self.update)
        self.start_time.start()

    def update(self):
        print("update")
        self.start_time = threading.Timer(0.1, self.update)
        self.start_time.start()
        self.time_elapsed += 1

    def stop(self):
        self.start_time.cancel()
        self.start_time = None
        print("stop")
        return

    def reset(self):
        print("reset")
        return self.time_elapsed

    def label(self, label):
        return label.set(f"Beurten over: {self.time_elapsed}")