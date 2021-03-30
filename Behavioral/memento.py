# Memento Pattern

class EditorMemento():
    def __init__(self, content: str) -> None:
        self._content = content

    def get_content(self):
        return self._content


class Editor():
    def __init__(self) -> None:
        self._content = ''

    def type(self, word: str):
        self._content = self._content + ' ' + word

    def get_content(self):
        return self._content

    def save(self):
        return EditorMemento(self._content)

    def restore(self, memento: EditorMemento):
        self._content = memento.get_content()


editor = Editor()
editor.type('This is the first sentence.')
editor.type('This is second.')

saved = editor.save()

editor.type('And this is third.')
print(editor.get_content())

editor.restore(saved)
print(editor.get_content())
