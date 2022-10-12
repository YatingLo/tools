import unittest

import grep

class TestGrepNovel(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_infos(self):
        title, chaps = grep.get_infos('https://czbooks.net/n/c542oi')
        self.assertEqual(title, "《鑄愛星空》")
        self.assertEqual(chaps[0], '//czbooks.net/n/c542oi/cnj7?chapterNumber=0')

    def test_get_content(self):
        content = grep.get_content('//czbooks.net/n/c542oi/cnj7?chapterNumber=0')
        self.assertEqual(content[:6], "《鑄愛星空》")

if __name__ == "__main__":
    unittest.main()
