# Bridge Pattern

from abc import ABCMeta, abstractmethod


class Theme(metaclass=ABCMeta):
    @abstractmethod
    def get_color(self) -> str:
        pass


class DarkTheme(Theme):
    def get_color(self) -> str:
        return 'Dark Black'


class LightTheme(Theme):
    def get_color(self) -> str:
        return 'Off white'


class AquaTheme(Theme):
    def get_color(self) -> str:
        return 'Light blue'


class WebPage(metaclass=ABCMeta):
    def __init__(self, theme_type: str) -> None:
        pass

    @abstractmethod
    def get_content():
        pass

    def get_color(self) -> str:
        if self._theme_type == 'dark':
            return DarkTheme().get_color()
        elif self._theme_type == 'light':
            return LightTheme().get_color()
        elif self._theme_type == 'aqua':
            return AquaTheme().get_color()


class About(WebPage):
    def __init__(self, theme_type: str) -> None:
        self._theme_type = theme_type

    def get_content(self):
        return "About page in " + self.get_color()


class Career(WebPage):
    def __init__(self, theme_type: str) -> None:
        self._theme_type = theme_type

    def get_content(self):
        return "Careers page in " + self.get_color()


about = About('light')
careers = Career('light')

print(about.get_content())
print(careers.get_content())


about = About('dark')
careers = Career('dark')

print(about.get_content())
print(careers.get_content())
