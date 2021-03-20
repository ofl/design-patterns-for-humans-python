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
    def __init__(self, theme: Theme) -> None:
        pass

    @abstractmethod
    def get_content():
        pass


class About(WebPage):
    def __init__(self, theme: Theme) -> None:
        self._theme = theme

    def get_content(self):
        return "About page in " + self._theme.get_color()


class Career(WebPage):
    def __init__(self, theme: Theme) -> None:
        self._theme = theme

    def get_content(self):
        return "Careers page in " + self._theme.get_color()


dark_theme = DarkTheme()
about = About(dark_theme)
careers = Career(dark_theme)

print(about.get_content())
print(careers.get_content())
