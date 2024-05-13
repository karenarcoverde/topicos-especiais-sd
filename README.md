# topicos-especiais-sd
Correção ortográfica automática de palavras baseada em dicionário

levschtein
**distância de Levenshtein** para calcular a similaridade entre strings. A distância de Levenshtein mede o número mínimo de edições necessárias para transformar uma string em outra, o que inclui inserções, deleções e substituições de caracteres.


bk-tree

fuzzy wuzzy

### Fórmula de Cálculo da Similaridade

A similaridade é calculada usando a seguinte fórmula:

```plaintext
Similaridade = (1 - (Distância de Levenshtein / Comprimento máximo das duas strings)) × 100
```
Esta fórmula fornece um valor percentual que reflete quão semelhantes são as duas strings, onde 100% representa uma correspondência perfeita e 0% indica nenhuma similaridade.

