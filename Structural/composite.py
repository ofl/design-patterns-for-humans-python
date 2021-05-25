# Composite Pattern

from abc import ABCMeta, abstractmethod


class TaskComponent(metaclass=ABCMeta):
    @abstractmethod
    def get_time_required(self) -> float:
        pass


class LeafTask(TaskComponent):
    def __init__(self, name: str, time: float) -> None:
        self.name = name
        self._time = time

    def get_time_required(self):
        return self._time


class CompositeTask(TaskComponent):
    def __init__(self, name: str) -> None:
        self.name = name
        self._sub_tasks = []

    def get_sub_tasks(self) -> list:
        return self._sub_tasks

    def add_sub_task(self, task: TaskComponent):
        self._sub_tasks.append(task)

    def remove_sub_task(self, task: TaskComponent):
        self._sub_tasks.remove(task)

    def get_time_required(self):
        time = 0

        for sub_task in self._sub_tasks:
            time += sub_task.get_time_required()

        return time


cook = CompositeTask('カレーライスを作る')

cook_curry = CompositeTask('カレーを作る')
cook_curry.add_sub_task(LeafTask('材料を切る', 10))
cook_curry.add_sub_task(LeafTask('玉ねぎを炒める', 10))
cook_curry.add_sub_task(LeafTask('肉を炒める', 5))
cook_curry.add_sub_task(LeafTask('煮る', 20))

cook_rice = CompositeTask('ご飯をたく')
cook_rice.add_sub_task(LeafTask('お米をとぐ', 1))
cook_rice.add_sub_task(LeafTask('炊飯器にかける', 60))

serve = CompositeTask('盛り付ける')
serve.add_sub_task(LeafTask('お皿にご飯をよそおう', 1))
serve.add_sub_task(LeafTask('カレーをかける', 1))

cook.add_sub_task(cook_curry)
cook.add_sub_task(cook_rice)
cook.add_sub_task(serve)

print(cook.get_time_required())
