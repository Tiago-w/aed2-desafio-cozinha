# 👨‍🍳 Sistema de Gestão: Desafio na Cozinha

![C](https://img.shields.io/badge/Linguagem-C-blue.svg)
![Estruturas](https://img.shields.io/badge/Estruturas-Hash%20%7C%20Trie%20%7C%20Guloso-success.svg)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-warning.svg)

Sistema de gerenciamento de acervo culinário desenvolvido para otimizar operações de busca, organização de ingredientes e recomendação de menus sob restrições, garantindo a integridade dos dados contra adulterações.

---

## 👥 Desenvolvedores
* **Tiago Wolowski**
* **Gustavo Serratte**

---

## 🏛️ Arquitetura e Estruturas de Dados

### 1. Tabela Hash
* **Aplicação:** Armazenamento primário e integridade (Modo Investigação).
* **Complexidade:** $O(1)$ médio.

### 2. Árvore Trie
* **Aplicação:** Busca rápida por nomes e ingredientes (Modo Consulta Rápida).
* **Complexidade:** $O(m)$ sendo $m$ o comprimento da string.

### 3. Algoritmo Guloso (Problema da Mochila 0/1)
* **Aplicação:** Motor de recomendação do *Modo Chef*.
* **Descrição:** O sistema resolve a composição de menus utilizando a estratégia de densidade de valor (razão entre avaliação do cliente e custo). O problema 0/1 é tratado de forma gulosa, selecionando as receitas com maior "índice de atratividade" que se encaixem no orçamento total.

---

## [RECUPERAÇÃO P1]

* **Questão Escolhida:** Algoritmos Gulosos e Otimização Combinatória.
* **Explicação Arquitetural:** Durante a prova, a maior dificuldade encontrada foi a aplicação de restrições de capacidade em problemas de otimização. Para solucionar isso, implementamos o Problema da Mochila 0/1 no *Modo Chef*. A lógica baseia-se em ordenar as receitas pela razão $V_i / C_i$ (Valor da avaliação / Custo). A funcionalidade permite ao chef compor um menu que maximiza a nota dos clientes respeitando um teto orçamentário.
* **Instruções de Teste:**
    1. Inicie o sistema e selecione o `Modo Chef`.
    2. Insira o orçamento máximo disponível para o menu (ex: `100.00`).
    3. O sistema exibirá as receitas selecionadas que oferecem o maior benefício dentro do valor informado, demonstrando a decisão tomada pelo algoritmo.

---

## 📂 Estrutura do Projeto
* `data/`: `dataset.json` (Base de dados).
* `src/`: Código-fonte (`.c` e `.h`).
* `bin/`: Executáveis.
* `docs/`: Documentação extra.

---
