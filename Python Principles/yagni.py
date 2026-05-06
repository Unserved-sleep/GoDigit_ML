class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True


# Usage
task = Task("Buy groceries", "Get milk, eggs, and bread")
task.complete()