# Factory Method Pattern(https://github.com/kamranahmedse/design-patterns-for-humans)

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


class HiringManager(metaclass=ABCMeta):
    def take_interview(self) -> None:
        interviewer = self._make_interviewer()
        interviewer.ask_questions()

    @abstractmethod
    def _make_interviewer(self) -> Interviewer:
        pass


class DevelopmentManager(HiringManager):
    def _make_interviewer(self) -> Interviewer:
        return Developer()


class MarketingManager(HiringManager):
    def _make_interviewer(self) -> Interviewer:
        return CommunityExecutive()


dev_manager = DevelopmentManager()
dev_manager.take_interview()

marketing_manager = MarketingManager()
marketing_manager.take_interview()
