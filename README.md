# topicos-especiais-sd
## Correção Ortográfica Automática de Palavras Baseada em Dicionário

Este projeto utiliza várias técnicas e algoritmos para implementar a correção ortográfica automática de palavras, assegurando que as entradas de texto estejam livres de erros antes de serem processadas ou armazenadas.

### Distância de Levenshtein

A **distância de Levenshtein** é uma métrica fundamental neste projeto, utilizada para calcular a similaridade entre strings. Ela mede o número mínimo de edições necessárias para transformar uma string em outra. Estas edições incluem inserções, deleções e substituições de caracteres.

### BK-Tree

A estrutura de dados **BK-Tree** é utilizada para melhorar a eficiência da busca por palavras próximas no dicionário, permitindo correções rápidas e eficazes mesmo em grandes volumes de dados.

### FuzzyWuzzy

O algoritmo **FuzzyWuzzy** é empregado para comparar strings de maneira mais flexível, considerando variações e pequenos erros nas entradas de texto.

### Fórmula de Cálculo da Similaridade

A similaridade entre duas strings é calculada usando a seguinte fórmula:

```plaintext
Similaridade = (1 - (Distância de Levenshtein / Comprimento máximo das duas strings)) * 100
```

