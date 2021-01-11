import threading, time

class MyCounter(threading.Thread):
    def __init__(self, id, start, stop, wait_time):
        super().__init__()
        self._id = id
        self._start = start
        self._stop = stop
        self._wait_time = wait_time

    def run(self):
        for x in range(self._start, self._stop):
            print(f"[{self._id}] - {x}")
            time.sleep(self._wait_time)

c1 = MyCounter('c1', 10, 15, 1)
c2 = MyCounter('c2', 10, 15, 0.5)
c1.start()
c2.start()

c1.join()
c2.join()
print("--- The end ---")


