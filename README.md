# topicos-especiais-sd
## Correção Ortográfica Automática de Palavras Baseada em Dicionário

Foi feito um estudo dos possíveis algoritmos que poderiam ser implementados para este projeto. Por conseguinte, foi escolhido o melhor algoritmo para implementação.

### Distância de Levenshtein

A **distância de Levenshtein** é a parte principal desse projeto, pois todos os algoritmos usados derivam-se dele. É possível perceber que ela foi utilizada em quase todos os algoritmos pesquisados. Ela mede o número mínimo de edições necessárias para transformar uma string em outra. Estas edições incluem inserções, deleções e substituições de caracteres.

The Levenshtein distance between two strings \(a, b\) (of length \(|a|\) and \(|b|\) respectively) is given by \( \text{lev}(a, b) \) where

\[ 
\text{lev}(a, b) = 
\begin{cases} 
|a| & \text{if } |b| = 0, \\
|b| & \text{if } |a| = 0, \\
\text{lev}(\text{tail}(a), \text{tail}(b)) & \text{if } \text{head}(a) = \text{head}(b), \\
1 + \min \{ & \\
\quad \text{lev}(\text{tail}(a), b), & \\
\quad \text{lev}(a, \text{tail}(b)), & \\
\quad \text{lev}(\text{tail}(a), \text{tail}(b)) & \\
\} & \text{otherwise}
\end{cases}
\]

where the tail of some string \(x\) is a string of all but the first character of \(x\) (i.e. \(\text{tail}(x_0x_1 \ldots x_n) = x_1x_2 \ldots x_n\)), and \(\text{head}(x)\) is the first character of \(x\) (i.e. \(\text{head}(x_0x_1 \ldots x_n) = x_0\)). Either the notation \(x[n]\) or \(x_n\) is used to refer the nth character of the string \(x\), counting from 0, thus \(\text{head}(x) = x_0 = x[0]\).

The first element in the minimum corresponds to deletion (from \(a\) to \(b\)), the second to insertion and the third to replacement.

This definition corresponds directly to the [naive recursive implementation](https://en.wikipedia.org/wiki/Levenshtein_distance).

### BK-Tree

A BK-Tree consiste em botar as palavras em uma árvore com pesos (distância de Levenshtein) e pecorrer a árvore pegando todas as distâncias menores ou iguais a distância limite estipulada. 

Para descobrir a distância entre duas palavras, é criada a matriz dp. A matriz dp[m][n] representa a distância total (Levenshtein) entre duas strings(a e b). A matriz dp tem dimensões (m+1)x(n+1), sendo m o comprimento da string a e n o comprimento da string b. Cada célula dp[i][j] armazena a distância de edição mínima entre as substrings a[0:i] e b[0:j]. A matriz é inicializada com dp[i][0] = i e dp[0][j] = j, indicando as transformações para strings vazias. O preechimento da matriz começa no dp[1][1] até dp[m][n], para cada célula dp[i][j], os caracteres da string a[i-1] e b[j-1] são comparados. Para o caso de serem iguais, dp[i-1][j-1] é transferido diretamente para dp[i][j], o que significa que não precisa ter nenhuma edição. Se forem diferentes, a célula é preenchida com o mínimo entre as possíveis operações(inserção, deleção e substituição).

Depois para buscar palavras semelhantes na árvore, é verificado a distância de edição entre o nó root e a palavra, caso ela seja menor que a variável "TOL" (tolerância), a palavra do root é adicionada a lista de resultados. Após essa verificação, é analisada os nós filhos de root investigando quais palavras tem as distâncias dentro do intervalo [distância - TOL, distância + TOL] para adicionar na lista de resultados.

Para adicionar a palavra na árvore, temos algumas etapas:
1. Se o nó root está vazio, a palavra atual (curr) que está sendo lida é colocada nesse nó.
2. Se já existe a palavra no root, é calculada a distância entre o root e a palavra (curr) que precisamos adicionar.
3. Se não possuir nó para essa distância na árvore no vetor next, cria-se um novo espaço para essa palavra (curr), atualizando o vetor next para apontar para ela e incrementando o contador ptr.
4. Se ja existir um nó para essa distância, não é criado um novo espaço, adiciona a palavra (curr) nesse nó existente. 



### FuzzyWuzzy


### Fórmula de Cálculo da Similaridade

A similaridade entre duas strings é calculada usando a seguinte fórmula:

```plaintext
Similaridade = (1 - (Distância de Levenshtein / Comprimento máximo das duas strings)) * 100
```
Esta fórmula fornece um valor percentual que reflete quão semelhantes são as duas strings baseado na distância de Levenshtein, onde 100% representa uma correspondência perfeita e 0% indica nenhuma similaridade.



### Instalação

### Exemplo 

(ordenacao do resultado, distancia e ordenacao) 

### Biblioteca no PyPI
https://pypi.org/project/bk-tree-modification/

### Referências
http://blog.notdot.net/2007/4/Damn-Cool-Algorithms-Part-1-BK-Trees \
https://www.youtube.com/watch?v=oIsPB2pqq_8 \
https://medium.com/datenworks/fuzzy-search-buscando-texto-por-aproxima%C3%A7%C3%A3o-6c7214e0ea01
