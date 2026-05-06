class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, handler):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(handler)

    def publish(self, event, data):
        if event in self.subscribers:
            for handler in self.subscribers[event]:
                handler(data)

bus = EventBus()

def send_email(data):
    print(f"Email sent to {data['email']}")

def log_event(data):
    print(f"Log: user registered {data['username']}")

bus.subscribe("user_registered", send_email)
bus.subscribe("user_registered", log_event)

bus.publish("user_registered", {
    "username": "Ali",
    "email": "ali@gmail.com"
})
