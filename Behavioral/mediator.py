# Mediator Pattern

from abc import ABCMeta, abstractmethod

import datetime


class ChatMediator(metaclass=ABCMeta):
    @abstractmethod
    def show_message(user, message: str):
        pass


class ChatRoom(ChatMediator):
    def show_message(self, user, message: str):
        now = datetime.datetime.now()
        time = now.strftime('%m %d, %Y %H:%M')
        sender = user.get_name()
        print(f"{time}[{sender}]: {message}")


class User():
    def __init__(self, name: str, chat_mediator: ChatMediator) -> None:
        self._name = name
        self._chat_mediator = chat_mediator

    def get_name(self):
        return self._name

    def send(self, message: str):
        self._chat_mediator.show_message(self, message)


mediator = ChatRoom()

john = User('John Doe', mediator)
jane = User('Jane Doe', mediator)

john.send('Hi there!')
jane.send('Hey!')
