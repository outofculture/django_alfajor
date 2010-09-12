from .. import browser


class NotFoundOnPage(Exception): pass


class Page(object):

    def click_on_home(self):
        for a in browser.cssselect('div#header a'):
            if a.text == 'example project home':
                a.click(wait_for='page')
                browser.page = ListPage()
                return True
        raise NotFoundOnPage()


class ListPage(Page):

    @property
    def foos_names(self):
        foos = browser.document['div#foo-list ul li']
        foo_names = [x.text for x in foos]
        return foo_names

