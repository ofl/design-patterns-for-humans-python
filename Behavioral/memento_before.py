# Memento Pattern

import datetime


class Editor():
    def __init__(self) -> None:
        self._content = ''

    def type(self, word: str):
        self._content = self._content + ' ' + word

    def get_content(self):
        return self._content

    def save(self):
        now = datetime.datetime.now()
        data = {
            'content': self._content,
            'saved_at': now.strftime('%m %d, %Y %H:%M')
        }
        return data

    def restore(self, saved_data):
        self._content = saved_data['content']
        print(f'Restored {saved_data["saved_at"]} data')


editor = Editor()
editor.type('This is the first sentence.')
editor.type('This is second.')

saved = editor.save()

editor.type('And this is third.')
print(editor.get_content())

editor.restore(saved)
print(editor.get_content())
