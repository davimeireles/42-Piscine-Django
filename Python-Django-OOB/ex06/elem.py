#!/usr/bin/python3

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """
    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return (super().__str__()
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace('\n', '\n<br />\n'))


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """

    class ValidationError(Exception):
        def __init__(self, message="Error in validation\n"):
            self.message = message
            super().__init__(self.message)

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        # Initialize as empty list
        self.content = []
        if content is not None:
            self.add_content(content)
        self.tag_type = tag_type

    def format_string(self):

        _result = ''
        _attr = ''
        _content = ''

        if self.attr:
            _attr = self.__make_attr()

        _content = self.__make_content()

        if self.tag_type == 'double':
            _result += '<' + self.tag + _attr + '>' + _content + '</' + self.tag + '>'
        elif self.tag_type == 'single':
            _result += '<' + self.tag + _attr + '/>'

        return _result

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """

        _result = self.format_string()
        _result = self.indent_string(_result)

        return _result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        if len(self.content) == 0:
            return ''

        if self.content[0] == '':
            return ''

        result = '\n'

        for elem in self.content:
            if isinstance(elem, Elem):
                result += str(elem) + '\n'
            else:
                result += str(elem) + '\n'
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError

        if isinstance(content, list):
            for elem in content:
                if elem:
                    self.content.append(elem)
        else:
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

    @staticmethod
    def indent_string(final_text, num_spaces=2):
        lines = final_text.split('\n')
        result = []
        indent = 0

        for line in lines:
            line = line.strip()
            if line.startswith('</'):
                indent -= 1
            result.append(" " * (num_spaces * indent) + line)
            if line.find('<div></div>') == -1 and not line.startswith('</') and line.startswith('<') and not line.endswith('/>'):
                indent += 1
        return "\n".join(result)

if __name__ == '__main__':

    html = Elem(tag='html', content=[Elem(tag='head', content=Elem(tag='title', content=Text('Hello ground!'))), Elem(tag='body', content=[Elem(tag='h1', content=Text('Oh no, not again!')), Elem(tag='img', attr={'src':'http://i.imgur.com/pfp3T.jpg'}, tag_type='single')])])
    print(html)