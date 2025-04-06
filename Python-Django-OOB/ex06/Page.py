import unittest
from elements import *

class Page:
    """Represents an HTML page and provides methods for validation."""
    def __init__(self, elem_instance):
        """Initializes a Page instance with an Elem (HTML element)."""
        self.elem_instance = elem_instance
    
    def __str__(self):
        """
        Returns the string representation of the underlying Elem instance,
        prepending the doctype if the root element is Html.
        """
        html_string = str(self.elem_instance)
        if isinstance(self.elem_instance, Html):
            return '<!DOCTYPE html>\n' + html_string
        else:
            return html_string
    
    def write_to_file(self, file_name):
        """
        Creates a file .html with the file_name passed by paramater,
        using the content of the elem_instance.
        """
        html_string = str(self.elem_instance)
        if isinstance(self.elem_instance, Html):
            doctype_string = '<!DOCTYPE html>\n' + html_string
            with open(file_name + '.html', 'w') as html:
                html.write(doctype_string)
        else:
            with open(file_name + '.html', 'w') as html:
                html.write(html_string)
        
    @staticmethod
    def check_head_and_body(page_content):
        """
        Checks if the page content contains exactly one <head> and one <body> tag.
        """
        i = 0
        for instance in page_content:
            if i == 0 and instance.tag != 'head':
                return False
            i += 1

        head_count = sum(1 for instance in page_content if instance.tag == 'head')
        body_count = sum(1 for instance in page_content if instance.tag == 'body')
        return head_count == 1 and body_count == 1

    @staticmethod
    def check_head_title(page_content):
        """Checks if the <head> section contains exactly one <title> tag."""
        for instance in page_content:
            if instance.tag == 'head':
                title_count = sum(1 for content in instance.content if isinstance(content, Title))
                # Exit early if head is found
                return title_count == 1
        # No head tag found, so no title either
        return False

    @staticmethod
    def is_valid_body_and_div_content(element):
        """
        Checks if the element is a valid content for <body> and <div>.
        """
        body_and_div_valid_tags = ['h1', 'h2', 'div', 'table', 'ul', 'ol', 'span', 'p']
        return element.tag in body_and_div_valid_tags or isinstance(element, Text)

    @staticmethod
    def is_valid_structural_tag_content(element):
        """
        Checks if the element is a valid content for structural tags (title, h1, h2, li, th, td).
        """
        return isinstance(element, Text)
    
    @staticmethod
    def is_valid_span_content(element):
        """
        Checks if the element is a valid content for span tag
        """
        return isinstance(element, Text) or isinstance(element, P)
    
    @staticmethod
    def is_valid_ul_ol_content(element):
        """
        Checks if the element is a valid content for ul, ol tag
        """
        return isinstance(element, Li)
    
    @staticmethod
    def is_valid_tr_content(element):
        """
        Checks if the element is a valid content for tr tag
        """
        return isinstance(element, Th) or isinstance(element, Td)
    
    @staticmethod
    def is_valid_table_content(element):
        """
        Checks if the element is a valid content for table tag
        """
        return isinstance(element, Tr)

    @staticmethod
    def recursive_validate(element):
        """
        Recursively validates the HTML structure and its elements.
        """
        if isinstance(element, list):
            for item in element:
                if not Page.recursive_validate(item):
                    return False
            return True

        if not hasattr(element, 'tag'):
            return True

        # Apply specific content validations based on the tag
        if element.tag in ['body', 'div']:
            if hasattr(element, 'content'):
                if isinstance(element.content, list):
                    if not all(Page.is_valid_body_and_div_content(item) for item in element.content if hasattr(item, 'tag')):
                        return False
                    return Page.recursive_validate(element.content)
                else:
                    if not Page.is_valid_body_and_div_content(element.content):
                        return False
                    return Page.recursive_validate(element.content)

        if element.tag in ['title', 'h1', 'h2', 'li', 'th', 'td']:
            if hasattr(element, 'content'):
                if isinstance(element.content, list):
                    if not all(Page.is_valid_structural_tag_content(item) for item in element.content):
                        return False
                    text_instance_count = sum(1 for element in element.content if isinstance(element, Text))
                    return text_instance_count == 1
                else:
                    if not Page.is_valid_structural_tag_content(element.content):
                        return False
                    return Page.recursive_validate(element.content)
        
        if element.tag == 'p':
            if hasattr(element, 'content'):
                if isinstance(element.content, list):
                    if not all(Page.is_valid_structural_tag_content(item) for item in element.content):
                        return False
                    return Page.recursive_validate(element.content)
                else:
                    if not Page.is_valid_structural_tag_content(element.content):
                        return False
                    return Page.recursive_validate(element.content)
        
        if element.tag == 'span':
            if hasattr(element, 'content'):
                if isinstance(element.content, list):
                    if not all(Page.is_valid_span_content(item) for item in element.content):
                        return False
                    return Page.recursive_validate(element.content)
                else:
                    if not Page.is_valid_span_content(element.content):
                        return False
                    return Page.recursive_validate(element.content)
        
        if element.tag in ['ul', 'ol']:
            if hasattr(element, 'content'):
                if isinstance(element.content, list):
                    if not all(Page.is_valid_ul_ol_content(item) for item in element.content):
                        return False
                    li_instance_count = sum(1 for element in element.content if isinstance(element, Li))
                    return li_instance_count >= 1
                else:
                    if not Page.is_valid_ul_ol_content(element.content):
                        return False
                    return Page.recursive_validate(element.content)
        
        if element.tag == 'table':
            if hasattr(element, 'content'):
                if isinstance(element.content, list):
                    if not all(Page.is_valid_table_content(item) for item in element.content):
                        return False
                else:
                    if not Page.is_valid_table_content(element.content):
                        return False
                    return Page.recursive_validate(element.content)
                
        if element.tag == 'tr':
            if hasattr(element, 'content'):
                if isinstance(element.content, list):
                    if not all(Page.is_valid_tr_content(item) for item in element.content):
                        return False
                    td_instance_count = sum(1 for element in element.content if isinstance(element, Td))
                    th_instance_count = sum(1 for element in element.content if isinstance(element, Th))
                    if td_instance_count >= 1 and th_instance_count >= 1:
                        return False
                    return td_instance_count >=1 or th_instance_count >= 1
                else:
                    if not Page.is_valid_tr_content(element.content):
                        return False
                    return Page.recursive_validate(element.content)
                    
        if hasattr(element, 'content'):
            return Page.recursive_validate(element.content)
        
        return True

    def is_valid(self):
        """
        Checks if the Page instance is a valid HTML structure based on several criteria, using a single recursive function.
        """
        if not isinstance(self.elem_instance, Html):
            return False
        content = self.elem_instance.content

        if not self.check_head_and_body(content) or not self.check_head_title(content):
            return False

        return self.recursive_validate(content)

class TestPage(unittest.TestCase):
    """Unit tests for the Page class."""
            
    def test_html_structure(self):
        valid_tree = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Div(content=Text("Valid")))])
        self.assertTrue(Page(valid_tree).is_valid())
        
        # head must be first and body second
        invalid_tree = Html(content=[Body(content=Div(content=Text("Valid"))), Head(content=Title(content=Text("Valid Title")))])
        self.assertFalse(Page(invalid_tree).is_valid())

    def test_head_structure(self):
        valid_head = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Div(content=Text("Valid")))])
        self.assertTrue(Page(valid_head).is_valid())

        invalid_head = Html(content=[Head(content=[Title(content=Text("Valid Title")), Title(content=Text("Another Title"))]), Body(content=Div(content=Text("Valid")))])
        self.assertFalse(Page(invalid_head).is_valid())

    def test_body_and_div_content(self):
        valid_body = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Div(content=H1(content=Text("Valid"))))])
        self.assertTrue(Page(valid_body).is_valid())

        invalid_body = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Div(content=Img()))])
        self.assertFalse(Page(invalid_body).is_valid())

    def test_structural_tags_content(self):
        valid_title = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=H1(content=Text("Valid")))])
        self.assertTrue(Page(valid_title).is_valid())

        invalid_title = Html(content=[Head(content=Title(content=Div(content=Text("Invalid")))), Body(content=H1(content=Text("Valid")))])
        self.assertFalse(Page(invalid_title).is_valid())
        
        invalid_title2 = Html(content=[Head(content=Title(content=Text('Valid Head'))), Body(content=H1(content=[Text("invalid"), Text("invalid")]))])
        self.assertFalse(Page(invalid_title2).is_valid())

    def test_p_content(self):
        valid_p = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=P(content=Text("Valid")))])
        self.assertTrue(Page(valid_p).is_valid())

        invalid_p = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=P(content=Div()))])
        self.assertFalse(Page(invalid_p).is_valid())

    def test_span_content(self):
        valid_span = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Span(content=Text("Valid")))])
        self.assertTrue(Page(valid_span).is_valid())

        valid_span_with_p = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Span(content=P(content=Text("Valid"))))])
        self.assertTrue(Page(valid_span_with_p).is_valid())

        invalid_span = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Span(content=Div()))])
        self.assertFalse(Page(invalid_span).is_valid())

    def test_ul_and_ol_content(self):
        valid_ul = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Ul(content=Li(content=Text("Valid"))))])
        self.assertTrue(Page(valid_ul).is_valid())

        invalid_ul = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Ul(content=Div()))])
        self.assertFalse(Page(invalid_ul).is_valid())

        invalid_ul_no_li = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Ul())])
        self.assertFalse(Page(invalid_ul_no_li).is_valid())
        
        invalid_ol_no_li = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Ol(content=[Li(), Div()]))])
        self.assertFalse(Page(invalid_ol_no_li).is_valid())

    def test_tr_content(self):
        valid_tr = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Table(content=Tr(content=Th(content=Text("Valid")))))])
        self.assertTrue(Page(valid_tr).is_valid())

        invalid_tr_mixed = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Table(content=Tr(content=[Th(content=Text("Valid")), Td(content=Text("Invalid"))])))])
        self.assertFalse(Page(invalid_tr_mixed).is_valid())

        invalid_tr_no_th_td = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Table(content=Tr(content=Text("Invalid"))))])
        self.assertFalse(Page(invalid_tr_no_th_td).is_valid())

    def test_table_content(self):
        valid_table = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Table(content=Tr(content=Th(content=Text("Valid")))))])
        self.assertTrue(Page(valid_table).is_valid())

        invalid_table = Html(content=[Head(content=Title(content=Text("Valid Title"))), Body(content=Table(content=Div()))])
        self.assertFalse(Page(invalid_table).is_valid())


if __name__ == '__main__':
    
    # unittest.main(verbosity=2)
    
    html = Page(Html(content=[Head(content=Title(content=Text('Valid Title'))), Body(content=Div(content=P(content=Text('Just a content.'))))]))
    if html.is_valid():
        print(html)
    else:
        print("Invalid HTML Structure")
        
    if html.is_valid():
        html.write_to_file('myhtml')
    else:
        print('Invalid HTML structure')