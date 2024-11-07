
from collections import Counter, defaultdict
import re

class UtilitariosAnaliseTexto:
    def __init__(self, texto):
        self.texto = texto

    def frequencia_palavras(self):
        """Retorna a frequência de cada palavra em um dicionário, ignorando maiúsculas/minúsculas e pontuação."""
        palavras = re.findall(r'\b\w+\b', self.texto.lower())  # Extract words, ignoring punctuation
        return dict(Counter(palavras))

    def encontrar_frases_palindromas(self):
        """Retorna uma lista de frases que são palíndromas, ignorando espaços e pontuação."""
        frases = self.texto.split('.')
        palindromas = []
        for frase in frases:
            frase_limpa = ''.join(filter(str.isalnum, frase.lower()))
            if frase_limpa == frase_limpa[::-1] and frase_limpa:
                palindromas.append(frase.strip())
        return palindromas

    def grupos_anagramas(self, lista_palavras):
        """Agrupa palavras que são anagramas entre si em uma lista de listas."""
        dicionario_anagramas = defaultdict(list)
        for palavra in lista_palavras:
            palavra_ordenada = ''.join(sorted(palavra.lower()))
            dicionario_anagramas[palavra_ordenada].append(palavra)
        return list(dicionario_anagramas.values())

    def prefixo_comum(self, lista_palavras):
        """Retorna o maior prefixo comum entre uma lista de palavras."""
        if not lista_palavras:
            return ''
        prefixo = lista_palavras[0]
        for palavra in lista_palavras[1:]:
            while not palavra.startswith(prefixo):
                prefixo = prefixo[:-1]
                if not prefixo:
                    return ''
        return prefixo

    def detectar_palavras_chave(self, palavras_comuns=None):
        """Detecta palavras-chave no texto, ignorando palavras comuns fornecidas na lista palavras_comuns."""
        if palavras_comuns is None:
            palavras_comuns = {"de", "a", "o", "e", "do", "da", 'são'}
        palavras = [palavra.lower() for palavra in re.findall(r'\b\w+\b', self.texto) if palavra.lower() not in palavras_comuns]
        return dict(Counter(palavras))

    def fatores_primos(self, numero):
        """Retorna os fatores primos de um número."""
        if numero <= 1:
            return []
        fatores = []
        divisor = 2
        while numero > 1:
            while numero % divisor == 0:
                fatores.append(divisor)
                numero //= divisor
            divisor += 1
        return fatores

    def contar_frases(self):
        """Conta o número de frases no texto, considerando '.' como delimitador."""
        return len([frase for frase in self.texto.split('.') if frase.strip()])

    def palavras_unicas_ordenadas(self):
        """Retorna uma lista de palavras únicas ordenadas alfabeticamente, ignorando maiúsculas/minúsculas e pontuação."""
        palavras = set(re.findall(r'\b\w+\b', self.texto.lower()))  # Unique words ignoring punctuation
        return sorted(palavras)
