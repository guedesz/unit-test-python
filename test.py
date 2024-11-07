
import unittest
from variacao01 import UtilitariosAnaliseTexto


class TestUtilitariosAnaliseTexto(unittest.TestCase):

    def setUp(self):
        self.texto = "A casa e o carro de Ana são vermelhos. Ana ama o carro."
        self.util = UtilitariosAnaliseTexto(self.texto)

    def test_frequencia_palavras(self):
        esperado = {'a': 1, 'casa': 1, 'e': 1, 'o': 2, 'carro': 2, 'de': 1, 'ana': 2, 'são': 1, 'vermelhos': 1, 'ama': 1}
        self.assertEqual(self.util.frequencia_palavras(), esperado)

    def test_encontrar_frases_palindromas(self):
        util = UtilitariosAnaliseTexto("A base do teto desaba. Anna.")
        esperado = ["A base do teto desaba", "Anna"]
        self.assertEqual(util.encontrar_frases_palindromas(), esperado)

    def test_grupos_anagramas(self):
        palavras = ["amor", "roma", "carro", "arco", "mora", "casa"]
        esperado = [["amor", "roma", "mora"], ["carro"], ["arco"], ["casa"]]
        self.assertEqual(self.util.grupos_anagramas(palavras), esperado)

    def test_prefixo_comum(self):
        palavras = ["flor", "florida", "floresta", "flutuante"]
        self.assertEqual(self.util.prefixo_comum(palavras), "fl")
        palavras = ["carro", "caravana", "casa"]
        self.assertEqual(self.util.prefixo_comum(palavras), "ca")
        palavras = ["casa", "animal"]
        self.assertEqual(self.util.prefixo_comum(palavras), "")
        self.assertEqual(self.util.prefixo_comum([]), "")  # Edge case: empty list

    def test_detectar_palavras_chave(self):
        esperado = {'casa': 1, 'carro': 2, 'ana': 2, 'vermelhos': 1, 'ama': 1}
        self.assertEqual(self.util.detectar_palavras_chave(), esperado)

    def test_fatores_primos(self):
        self.assertEqual(self.util.fatores_primos(28), [2, 2, 7])
        self.assertEqual(self.util.fatores_primos(29), [29])  # Prime number case
        self.assertEqual(self.util.fatores_primos(1), [])
        self.assertEqual(self.util.fatores_primos(-5), [])

    def test_contar_frases(self):
        self.assertEqual(self.util.contar_frases(), 2)  # Example text has two sentences
        util = UtilitariosAnaliseTexto("Uma frase.")
        self.assertEqual(util.contar_frases(), 1)

    def test_palavras_unicas_ordenadas(self):
        esperado = ['a', 'ama', 'ana', 'carro', 'casa', 'de', 'e', 'o', 'são', 'vermelhos']
        self.assertEqual(self.util.palavras_unicas_ordenadas(), esperado)

if __name__ == '__main__':
    unittest.main()
