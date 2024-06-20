import unittest
from bk_tree import BKTree

class TestBKTree(unittest.TestCase):
    def setUp(self):
        # Inicializa uma BK-Tree com algumas palavras de exemplo para os testes
        self.words = ["hell", "help", "shell", "smell", "fell", "felt", "oops", "pop", "oouch", "halt"]
        self.bktree = BKTree(words=self.words)

    def test_edit_distance(self):
        # Testa se a distância de edição é calculada corretamente
        self.assertEqual(BKTree.edit_distance("hell", "hello"), 1)
        self.assertEqual(BKTree.edit_distance("hell", "help"), 1)
        self.assertEqual(BKTree.edit_distance("oops", "pop"), 2)

    def test_add_word(self):
        # Verifica se palavras adicionais são inseridas corretamente
        self.bktree.add_word("hello")
        result = self.bktree.get_similar_words("hello")
        print("Similar words for 'hello':", result)
        self.assertIn("hello", result)

    def test_get_similar_words_help(self):
        # verifica as palavras similares a "help"
        similar = self.bktree.get_similar_words("help")
        print("Similar words for 'help':", similar)
        self.assertTrue("hell" in similar)
        self.assertTrue("help" in similar)
        self.assertTrue("felt" in similar)

    def test_get_similar_words_no_match_xyz(self):
        # verifica as palavras similares a "xyz"
        no_similar = self.bktree.get_similar_words("xyz")
        print("Similar words for 'xyz':", no_similar)
        self.assertEqual(len(no_similar), 0)

    def test_get_similar_words_helt(self):
        # verifica as palavras similares a "helt"
        similar = self.bktree.get_similar_words("helt")
        print("Similar words for 'helt':", similar)
        self.assertTrue("hell" in similar)
        self.assertTrue("felt" in similar)
        self.assertTrue("halt" in similar)

    def test_get_similar_words_ops(self):
        # verifica as palavras similares a "ops"
        similar = self.bktree.get_similar_words("ops")
        print("Similar words for 'ops':", similar)
        self.assertTrue("oops" in similar)
        self.assertTrue("pop" in similar)

if __name__ == '__main__':
    unittest.main()
