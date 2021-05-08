# Mediator Pattern

from abc import ABCMeta, abstractmethod


class ChatMediator(metaclass=ABCMeta):
    @abstractmethod
    def add_friend(self, user):
        pass

    @abstractmethod
    def send_message(self, sender, message: str):
        pass


class ChatRoom(ChatMediator):
    def __init__(self) -> None:
        self._friends = []

    def add_friend(self, user):
        self._friends.append(user)

    def send_message(self, sender, message: str):
        for user in self._friends:
            if user != sender:
                print(f"[{user.name}]: {message}(by {sender.name})")


class User():
    def __init__(self, name: str) -> None:
        self.name = name

    def send_message(self, chat_room: ChatRoom, message: str):
        chat_room.send_message(self, message)

    def receive_message(self, sender, message: str):
        if self != sender:
            print(f"[{self.name}]: {message}(by {sender.name})")


john = User('John')
jane = User('Jane')
jannet = User('Jannet')

chat_room = ChatRoom()

chat_room.add_friend(john)
chat_room.add_friend(jane)
chat_room.add_friend(jannet)

john.send_message(chat_room, 'Hello!')
jane.send_message(chat_room, 'Hey!')

# add new friend

julian = User('Julian')
chat_room.add_friend(julian)
julian.send_message(chat_room, 'Hi there!')
