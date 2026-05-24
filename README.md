# 👨‍🍳 Sistema de Gestão: Desafio na Cozinha

![Python](https://img.shields.io/badge/Linguagem-Python-blue.svg)
![Estruturas](https://img.shields.io/badge/Estruturas-Hash%20%7C%20Trie%20%7C%20Guloso-success.svg)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-warning.svg)

Sistema de gerenciamento de acervo culinário desenvolvido para otimizar operações de busca, organização de ingredientes e recomendação de menus sob restrições. O sistema utiliza um **banco de dados em formato JSON (dataset estático)**, permitindo portabilidade e fácil manipulação dos dados de receitas.

---

## 👥 Desenvolvedores
* **Tiago Wolowski**
* **Gustavo Serratte**

---

## 🏛️ Arquitetura e Estruturas de Dados

* **Banco de Dados:** Utiliza o formato **JSON** para armazenamento persistente e leitura dinâmica dos dados, garantindo uma estrutura hierárquica eficiente para ingredientes e passos de preparo.
* **Tabela Hash:** Implementada manualmente para armazenamento primário e verificação de integridade.
* **Árvore Trie:** Implementada manualmente para busca rápida de prefixos (nomes e ingredientes).
* **Algoritmo Guloso:** Motor de recomendação baseado no Problema da Mochila 0/1, otimizando cardápios via densidade de valor ($V_i/C_i$).

---

## [RECUPERAÇÃO P1]

* **Questão Escolhida:** Algoritmos Gulosos e Otimização Combinatória.
* **Explicação Arquitetural:** Implementamos o Problema da Mochila 0/1 no *Modo Chef*. A lógica ordena as receitas pela razão $V_i / C_i$ (Avaliação / Custo) para maximizar a satisfação do cliente dentro de um teto orçamentário.
* **Instruções de Teste:**
    1. Certifique-se de que o ficheiro `dataset.json` está na pasta `data/`.
    2. Execute `py src/main.py` e selecione o *Modo Chef*.
    3. Insira o orçamento disponível e o sistema retornará a combinação otimizada.

---

## 📂 Estrutura do Projeto
* `data/`: `dataset.json` (Banco de dados de receitas).
* `src/`: Código-fonte (Implementação das estruturas e lógica principal).
* `docs/`: Documentação extra.

---

## 🚀 Guia de Execução

### Pré-requisitos
* Python 3.x

### Inicialização
```bash
py src/main.py
```
