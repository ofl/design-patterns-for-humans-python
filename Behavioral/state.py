# State Pattern

from abc import ABCMeta, abstractmethod


class WritingState(metaclass=ABCMeta):
    @abstractmethod
    def write(self, words: str):
        pass


class UpperCase(WritingState):
    def write(self, words: str) -> str:
        print(words.upper())


class LowerCase(WritingState):
    def write(self, words: str) -> str:
        print(words.lower())


class DefaultText(WritingState):
    def write(self, words: str) -> str:
        print(words)


class Sorter():
    def __init__(self, sorter: WritingState) -> None:
        self._sorter = sorter

    def sort(self, array: list) -> list:
        return self._sorter.sort(array)


class TextEditor():
    def __init__(self, state: WritingState) -> None:
        self._state = state

    def set_state(self, state: WritingState):
        self._state = state

    def type(self, words: str):
        self._state.write(words)


editor = TextEditor(DefaultText())

editor.type('First line')

editor.set_state(UpperCase())

editor.type('Second line')
editor.type('Third line')

editor.set_state(LowerCase())

editor.type('Fourth line')
editor.type('Fifth line')

# Output:
# First line
# SECOND LINE
# THIRD LINE
# fourth line
# fifth line
