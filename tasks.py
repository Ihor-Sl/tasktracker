TASKS = []


def add_task(title, priority=1):
    task = {"title": title, "priority": priority, "done": False}
    TASKS.append(task)
    return task


def complete_task(index):
    TASKS[index]["done"] = True
