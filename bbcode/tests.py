import bbcode
import unittest

parse = lambda x: bbcode.parse(x, auto_discover=True)[0]

class LinkTestCase(unittest.TestCase):
    def testAutoLinks(self):
        self.assertEquals(parse('Check out ]http://example.com'), 'Check out ]http://example.com')
        self.assertEquals(parse('Check outhttp://example.com'), 'Check outhttp://example.com')
        self.assertEquals(parse('Check out http://example.com'), 'Check out <a href="http://example.com">http://example.com</a>')
        self.assertEquals(parse('Check out www.example.com'), 'Check out <a href="http://www.example.com">www.example.com</a>')

    def testURL(self):
        self.assertEquals(parse('Check out [url]http://example.com[/url]'), 'Check out <a href="http://example.com">http://example.com</a>')

if __name__ == '__main__':
    unittest.main()
