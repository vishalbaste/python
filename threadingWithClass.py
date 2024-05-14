import threading
import time

# Define a class that inherits from threading.Thread
class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    # Override the run method to define the thread's behavior
    def run(self):
        print(f"Thread {self.name} started.")
        for i in range(5):
            print(f"Thread {self.name}: {i}")
            time.sleep(1)  # Simulate some time-consuming task
        print(f"Thread {self.name} finished.")

# Create and start multiple threads
thread1 = MyThread("Thread 1")
thread2 = MyThread("Thread 2")

thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("All threads have finished.")
