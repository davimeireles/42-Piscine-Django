from elem import Elem
from elem import Text

class Html(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('html', content=content, attr=attr)

class Head(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('head', content=content, attr=attr)

class Body(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('body', content=content, attr=attr)

class Title(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('title', content=content, attr=attr)

class Meta(Elem):
    def __init__(self, attr=None):
        super().__init__('meta', tag_type='single', attr=attr)

class Img(Elem):
    def __init__(self, attr=None):
        super().__init__('img', tag_type='single', attr=attr)

class Table(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('table', content=content, attr=attr)

class Th(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('th', content=content, attr=attr)

class Tr(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('tr', content=content, attr=attr)

class Td(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('td', content=content, attr=attr)

class Ul(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('ul', content=content, attr=attr)

class Ol(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('ol', content=content, attr=attr)

class Li(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('li', content=content, attr=attr)

class H1(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('h1', content=content, attr=attr)

class H2(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('h2', content=content, attr=attr)

class P(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('p', content=content, attr=attr)

class Div(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('div', content=content, attr=attr)

class Span(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('span', content=content, attr=attr)

class Hr(Elem):
    def __init__(self, attr=None):
        super().__init__('hr', tag_type='single', attr=attr)

class Br(Elem):
    def __init__(self, attr=None):
        super().__init__('br', tag_type='single', attr=attr)


if __name__ == '__main__':
    try:
        page = Html(content=[Head(content=Title(content=Text('Hello ground!'))), Body(content=[H1(content=Text('Oh no, not again!')), Img(attr={'src':'http://i.imgur.com/pfp3T.jpg'})])])
        print(page)
    except NameError:
        print("No HTML element")