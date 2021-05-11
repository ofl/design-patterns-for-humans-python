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


class Default(WritingState):
    def write(self, words: str) -> str:
        print(words)


class TextEditor():
    def __init__(self) -> None:
        self._mode = 'default'
        self._default = Default()
        self._upper_case = UpperCase()
        self._lower_case = LowerCase()

    def set_mode(self, mode: str):
        self._mode = mode

    def type(self, words: str):
        if self._mode == 'upper_case':
            self._upper_case.write(words)
        elif self._mode == 'lower_case':
            self._lower_case.write(words)
        else:
            self._default.write(words)


editor = TextEditor()

editor.type('First line')

editor.set_mode('upper_case')

editor.type('Second line')
editor.type('Third line')

editor.set_mode('lower_case')

editor.type('Fourth line')
editor.type('Fifth line')

# Output:
# First line
# SECOND LINE
# THIRD LINE
# fourth line
# fifth line
