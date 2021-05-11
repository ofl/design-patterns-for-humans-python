# Memento Pattern

import datetime


class EditorMemento():
    def __init__(self, content: str) -> None:
        self._content = content
        now = datetime.datetime.now()
        self._saved_at = now.strftime('%m %d, %Y %H:%M')

    def get_content(self):
        return self._content

    def get_saved_at(self):
        return self._saved_at


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
        print(f'Restored {memento.get_saved_at()} data')


editor = Editor()
editor.type('This is the first sentence.')
editor.type('This is second.')

saved = editor.save()

editor.type('And this is third.')
print(editor.get_content())

editor.restore(saved)
print(editor.get_content())
