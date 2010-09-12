# Copyright Action Without Borders, Inc., the Alfajor authors and contributors.
# All rights reserved.  See AUTHORS.
#
# This file is part of 'alfajor' and is distributed under the BSD license.
# See LICENSE for more details.
from django.test import TransactionTestCase

from . import browser
import nose.tools as nt

from pageobjects.foo import Page, NotFoundOnPage


def test_reset():
    # TODO: flesh this out when cookie querying is working and has
    # test coverage.  until then, just verify that the method doesn't
    # explode.
    browser.open('/')
    browser.reset()


def test_user_agent():
    browser.open('/')
    ua = browser.user_agent
    assert ua['browser'] != 'unknown'


class test_basics(TransactionTestCase):
    fixtures = ['initial_foos.json']

    def setUp(self):
        # put any code you want to execute before every test block here.
        browser.open('/')
        browser.page = Page()
        browser.page.click_on_home()
        # browser.page will be redefined by click_on_home

    def tearDown(self):
        # put any code you want to execute after every test block here.
        pass

    def test_home_page(self):
        nt.assert_equal(
                ["Red Foo", "Green Foo", "Blue Foo"], browser.page.foos_names)





'''
def test_simple():
    settings.DEBUG = True
    browser.open('/')

    if 'status' in browser.capabilities:
        assert browser.status_code == 200
        assert browser.status == '200 OK'
    if 'headers' in browser.capabilities:
        assert 'text/html' in browser.headers['Content-Type']
    assert not browser.cookies

    # This is generally not a safe assertion... the browser could (and does)
    # normalize the returned html in some fashion.
    assert browser.response == ('<html><head></head>'
                                '<body><p>hi there</p></body></html>')

    assert browser.document.cssselect('p')[0].text == 'hi there'


from foo.models import Foo
from django.conf import settings

def test_that_database_access_works():
    settings.DEBUG = True
    browser.open('/foocount')
    assert browser.document['#foocount'].text == '0'
'''
