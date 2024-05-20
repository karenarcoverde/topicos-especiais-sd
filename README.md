# topicos-especiais-sd
## Correção Ortográfica Automática de Palavras Baseada em Dicionário

Foi feito um estudo dos possíveis algoritmos que poderiam ser implementados para este projeto. Por conseguinte, foi escolhido o melhor algoritmo para implementação.

### Distância de Levenshtein

A **distância de Levenshtein** é uma métrica fundamental neste projeto. É possível perceber que ela foi utilizada em quase todos os algoritmos pesquisados. Ela mede o número mínimo de edições necessárias para transformar uma string em outra. Estas edições incluem inserções, deleções e substituições de caracteres.

### BK-Tree

A BK-Tree consiste em botar as palavras em uma árvore com pesos (distância de Levenshtein) e pecorrer a árvore pegando todas as distâncias menores ou iguais a distância limite estipulada. 

### FuzzyWuzzy


### Fórmula de Cálculo da Similaridade

A similaridade entre duas strings é calculada usando a seguinte fórmula:

```plaintext
Similaridade = (1 - (Distância de Levenshtein / Comprimento máximo das duas strings)) * 100
```
Esta fórmula fornece um valor percentual que reflete quão semelhantes são as duas strings, onde 100% representa uma correspondência perfeita e 0% indica nenhuma similaridade.

### Referências
http://blog.notdot.net/2007/4/Damn-Cool-Algorithms-Part-1-BK-Trees
https://www.youtube.com/watch?v=oIsPB2pqq_8
https://medium.com/datenworks/fuzzy-search-buscando-texto-por-aproxima%C3%A7%C3%A3o-6c7214e0ea01
