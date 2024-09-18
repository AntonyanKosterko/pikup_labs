class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state):
        self._state = state
        self.notify()

class Observer:
    def update(self, state):
        print(f"Observer: Reacted to the state change: {state}")

if __name__ == "__main__":
    subject = Subject()
    observer1 = Observer()
    observer2 = Observer()

    subject.attach(observer1)
    subject.attach(observer2)

    subject.set_state("State 1")
    subject.set_state("State 2")
