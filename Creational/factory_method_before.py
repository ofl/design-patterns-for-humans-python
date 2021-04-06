# Factory Method Pattern

from abc import ABCMeta, abstractmethod


class Interviewer(metaclass=ABCMeta):
    @abstractmethod
    def ask_questions(self) -> None:
        pass


class Developer(Interviewer):
    def ask_questions(self) -> None:
        print('Asking about design patterns!')


class CommunityExecutive(Interviewer):
    def ask_questions(self) -> None:
        print('Asking about community building')


developer = Developer()
developer.ask_questions()

community_executive = CommunityExecutive()
community_executive.ask_questions()
