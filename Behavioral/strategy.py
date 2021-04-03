# Strategy Pattern

from abc import ABCMeta, abstractmethod


class SortStrategy(metaclass=ABCMeta):
    @abstractmethod
    def sort(self, dataset: list):
        pass


class BubbleSortStrategy(SortStrategy):
    def sort(self, dataset: list):
        print("Sorting using bubble sort")
        return dataset


class QuickSortStrategy(SortStrategy):
    def sort(self, dataset: list):
        print("Sorting using quick sort")
        return dataset


class Sorter():
    def __init__(self, sorter: SortStrategy) -> None:
        self._sorter = sorter

    def sort(self, array: list):
        self._sorter.sort(array)


dataset = [1, 5, 4, 3, 2, 8]

sorter = Sorter(BubbleSortStrategy())
sorter.sort(dataset)
# Output: Sorting using bubble sort

sorter = Sorter(QuickSortStrategy())
sorter.sort(dataset)
# Output: Sorting using quick sort
