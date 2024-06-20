# topicos-especiais-sd
## Correção Ortográfica Automática de Palavras Baseada em Dicionário

Foi feito um estudo dos possíveis algoritmos que poderiam ser implementados para este projeto. Por conseguinte, foi escolhido o melhor algoritmo para implementação.

### Distância de Levenshtein

A **distância de Levenshtein** é a parte principal desse projeto, pois todos os algoritmos usados derivam-se dele. É possível perceber que ela foi utilizada em quase todos os algoritmos pesquisados. Ela mede o número mínimo de edições necessárias para transformar uma string em outra. Estas edições incluem inserções, deleções e substituições de caracteres.

A fórmula da distância de Levenshtein entre duas strings `a`, `b` (de comprimentos |a| e |b| respectivamente) é dada por `lev(a, b)` onde:

```plaintext
lev(a, b) =   |a|                      se |b| = 0,
              |b|                      se |a| = 0,
              lev(tail(a), tail(b))    se head(a) = head(b),
              1 + min( lev(tail(a), b),
                       lev(a, tail(b)),
                       lev(tail(a), tail(b)) )  caso contrário.

```
O head de uma string x é seu primeiro caractere, enquanto o tail é o restante da string após o primeiro caractere. O primeiro elemento no "min" corresponde a deleção (de a para b), o segundo a inserção e o terceiro a substituição.


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
Para instalar o módulo `bk-tree-modification` (https://pypi.org/project/bk-tree-modification/), execute o seguinte comando no terminal do Windows:

```bash
pip install bk-tree-modification
```

Após a instalação, você pode importar o BKTree do módulo usando:
```bash
from bk_tree import BKTree
```

### Exemplo 

Para testar a biblioteca `bk_tree`, basta rodar o código `test_bktree.py` que está na pasta tests com o seguinte comando:

```bash
python test_bktree.py
```

Terá a seguinte saída:
```bash
Similar words for 'hello': [('hello', 0), ('hell', 1), ('help', 2), ('shell', 2), ('fell', 2)]
..Similar words for 'help': [('help', 0), ('hell', 1), ('shell', 2), ('fell', 2), ('felt', 2), ('halt', 2)]
.Similar words for 'helt': [('hell', 1), ('help', 1), ('felt', 1), ('halt', 1), ('shell', 2), ('fell', 2)]
.Similar words for 'xyz': []
.Similar words for 'ops': [('oops', 1), ('pop', 2)]
.
----------------------------------------------------------------------
Ran 6 tests in 0.004s

OK
```

### Referências
http://blog.notdot.net/2007/4/Damn-Cool-Algorithms-Part-1-BK-Trees \
https://www.youtube.com/watch?v=oIsPB2pqq_8 \
https://medium.com/datenworks/fuzzy-search-buscando-texto-por-aproxima%C3%A7%C3%A3o-6c7214e0ea01
https://en.wikipedia.org/wiki/Levenshtein_distance#:~:text=Informally%2C%20the%20Levenshtein%20distance%20between,considered%20this%20distance%20in%201965.
