import unittest
from models.article import Article

class ArticleTestCase(unittest.TestCase):
    def setUp(self):
        print "setUp"

    def tearDown(self):
        print "tearDown"

    def test_put(self):
        print 'test start'
        article = Article(testid=1, sectionid=2, content='test')
        article.put()
        query = article.all()
        self.assertEquals(query.count(), 1)
        query = query.filter("testid =", 1)
        self.assertEquals(query.count(), 1)
        for result in query:
            self.assertEquals(result.content, 'test')

