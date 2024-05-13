# topicos-especiais-sd
## Correção Ortográfica Automática de Palavras Baseada em Dicionário

Foi feito um estudo dos possíveis algoritmos que poderiam ser implementados para este projeto. Por conseguinte, foi escolhido o melhor algoritmo para implementação.

### Distância de Levenshtein

A **distância de Levenshtein** é uma métrica fundamental neste projeto. É possível perceber que ela foi utilizada em quase todos os algoritmos pesquisados. Ela mede o número mínimo de edições necessárias para transformar uma string em outra. Estas edições incluem inserções, deleções e substituições de caracteres.

### BK-Tree

A estrutura de dados **BK-Tree** é utilizada para melhorar a eficiência da busca por palavras próximas no dicionário, permitindo correções rápidas e eficazes mesmo em grandes volumes de dados.

### FuzzyWuzzy


### Fórmula de Cálculo da Similaridade

A similaridade entre duas strings é calculada usando a seguinte fórmula:

```plaintext
Similaridade = (1 - (Distância de Levenshtein / Comprimento máximo das duas strings)) * 100
```
Esta fórmula fornece um valor percentual que reflete quão semelhantes são as duas strings, onde 100% representa uma correspondência perfeita e 0% indica nenhuma similaridade. ajeita pra mim que fique bonito
