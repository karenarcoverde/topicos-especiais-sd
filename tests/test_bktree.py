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
        self.assertIn("hello", self.bktree.get_similar_words("hello"))

    def test_get_similar_words_within_tolerance(self):
        # Testa a função get_similar_words para verificar se retorna palavras dentro da tolerância especificada
        similar = self.bktree.get_similar_words("help")
        self.assertTrue("hell" in similar)
        self.assertTrue("help" in similar)
        self.assertTrue("felt" in similar)  # Assume TOL >= 1

    def test_get_similar_words_no_match(self):
        # Garante que palavras fora da tolerância não sejam retornadas
        no_similar = self.bktree.get_similar_words("xyz")
        self.assertEqual(len(no_similar), 0)

if __name__ == '__main__':
    unittest.main()