# Mediator Pattern


class User():
    def __init__(self, name: str) -> None:
        self.name = name
        self._friends = []

    def add_friend(self, user):
        self._friends.append(user)

    def send_message(self, message: str):
        for user in self._friends:
            user.receive_message(self, message)

    def receive_message(self, sender, message: str):
        if self != sender:
            print(f"[{self.name}]: {message}(by {sender.name})")


john = User('John')
jane = User('Jane')
jannet = User('Jannet')

john.add_friend(jane)
john.add_friend(jannet)
jane.add_friend(john)
jane.add_friend(jannet)
jannet.add_friend(john)
jannet.add_friend(jane)

john.send_message('Hello!')
jane.send_message('Hey!')

# add new friend

julian = User('Julian')

john.add_friend(julian)
jane.add_friend(julian)
jannet.add_friend(julian)

julian.add_friend(john)
julian.add_friend(jane)
julian.add_friend(jannet)

julian.send_message('Hi there!')
