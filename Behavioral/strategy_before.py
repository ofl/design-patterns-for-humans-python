#  Pattern

from abc import ABCMeta, abstractmethod


class Sort(metaclass=ABCMeta):
    @abstractmethod
    def sort(self, dataset: list):
        pass


class BubbleSort(Sort):
    def sort(self, dataset: list) -> list:
        print("Sorting using bubble sort")
        return dataset


class QuickSort(Sort):
    def sort(self, dataset: list) -> list:
        print("Sorting using quick sort")
        return dataset


class Sorter():
    def __init__(self, type: str) -> None:
        self._type = type

    def sort(self, array: list) -> list:
        if self._type == 'bubble':
            sorter = BubbleSort()
        else:
            sorter = QuickSort()

        return sorter.sort(array)


dataset = [1, 5, 4, 3, 2, 8]

sorter = Sorter('bubble')
sorter.sort(dataset)
# Output: Sorting using bubble sort

sorter = Sorter('quick')
sorter.sort(dataset)
# Output: Sorting using quick sort
