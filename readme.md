# 👨‍🍳 Sistema de Gestão: Desafio na Cozinha

Sistema de gerenciamento de acervo culinário desenvolvido para otimizar operações de busca, organização de ingredientes e recomendação de menus sob restrições, garantindo a integridade dos dados contra adulterações.

---

## 👥 Desenvolvedores
* **Tiago Wolowski**
* **Gustavo Serratte**

---

## 🏛️ Arquitetura e Estruturas de Dados

O núcleo do sistema foi implementado do zero em **C**, focado no controle manual de alocação de memória e performance de acesso. 

### 1. Tabela Hash (Dicionário Principal)
Responsável pelo armazenamento primário das receitas.
* **Complexidade:** Busca em $O(1)$ no melhor caso.
* **Aplicação:** *Modo Consulta Rápida* e *Modo Investigação*. Cada receita recebe um identificador único baseado no seu conteúdo (hash de integridade). Se o conteúdo muda, a verificação acusa a sabotagem.

### 2. Árvore Trie (Autocompletar e Filtros)
Implementada para a indexação de strings (nomes de receitas e ingredientes).
* **Complexidade:** Busca em $O(m)$, onde $m$ é o tamanho do prefixo/palavra.
* **Aplicação:** Permite buscas instantâneas por prefixo. A busca na árvore foi otimizada utilizando lógica iterativa em vez de recursiva profunda, garantindo segurança contra estouro de pilha (*stack overflow*).

### 3. Algoritmo Guloso (Otimização Combinatória)
Atua como o motor de recomendação do *Modo Chef*.
* **Aplicação:** Sugere combinações de pratos que maximizam a avaliação dos clientes sem ultrapassar restrições de custo ou tempo máximo de preparo, ordenando os itens pela melhor relação custo-benefício.

---

## 📂 Estrutura do Projeto

A organização do repositório segue os padrões de projetos em C para garantir modularidade e clareza:

* **`data/`**: Contém o ficheiro `dataset.json`, que serve como a base de dados estática do sistema.
* **`src/`**: Pasta que aloja todo o código-fonte. Inclui os ficheiros `.h` (headers) com as definições das estruturas e as assinaturas das funções, e os ficheiros `.c` com as implementações das Tabelas Hash, Árvores Trie e lógica do sistema.
* **`bin/`**: Diretório destinado aos ficheiros binários e ao executável final após a compilação.
* **`docs/`**: Contém documentação auxiliar, como o manual de utilizador ou diagramas de fluxo das estruturas de dados.

---

## 🗄️ Modelagem dos Dados (JSON Estático)

Os dados são ingeridos a partir de um arquivo `dataset.json`. O parser converte as strings do JSON diretamente para *structs* em C na memória. 

**Exemplo do modelo de dados ingerido:**
```json
{
  "id": "104",
  "nome": "Tainha Assada na Brasa",
  "categoria": "Pescados",
  "tempo_preparo_min": 45,
  "custo_estimado": 35.50,
  "ingredientes": ["Tainha", "Sal grosso", "Limão", "Azeite"]
}