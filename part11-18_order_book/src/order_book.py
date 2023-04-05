class Task:
    _id = 1

    def __init__(self, description: str, programmer: str, workload: int):
        self.id = Task._id
        Task._id += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True


class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        task = Task(description, programmer, workload)
        self.orders.append(task)

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list(set([order.programmer for order in self.orders]))

    def mark_finished(self, id: int):
        for order in self.orders:
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError("No task found with the given id")

    def finished_orders(self):
        return [order for order in self.orders if order.finished]

    def unfinished_orders(self):
        return [order for order in self.orders if not order.finished]

    def status_of_programmer(self, programmer: str):
        finished_tasks = [order for order in self.orders if order.programmer == programmer and order.finished]
        unfinished_tasks = [order for order in self.orders if order.programmer == programmer and not order.finished]

        if not finished_tasks and not unfinished_tasks:
            raise ValueError("No programmer found with the given name")

        finished_workload = sum([task.workload for task in finished_tasks])
        unfinished_workload = sum([task.workload for task in unfinished_tasks])

        return len(finished_tasks), len(unfinished_tasks), finished_workload, unfinished_workload
