# 🚢 Batalha Naval

## 📚 Sobre o Projeto

Este projeto foi desenvolvido como trabalho acadêmico para a disciplina de **Raciocínio Algorítmico** da **PUCPR (Pontifícia Universidade Católica do Paraná)**.

O sistema consiste em uma implementação do clássico jogo **Batalha Naval** utilizando a linguagem Python, executado diretamente no terminal. O projeto aplica conceitos fundamentais de lógica de programação, estruturas de repetição, condicionais, funções, matrizes e validação de entradas.

---

## 👨‍💻 Integrantes

* João Pedro Lima
* Gabriel Sandrini
* Mateus Picinin

---

## 🎯 Objetivo

O objetivo do jogo é localizar e destruir todas as embarcações inimigas antes que o computador destrua as suas.

Cada jogador possui 5 embarcações distribuídas em um tabuleiro 10x10.

---

## ⚙️ Funcionalidades

* Criação de tabuleiros 10x10.
* Posicionamento manual das embarcações do jogador.
* Posicionamento aleatório das embarcações do computador.
* Validação das entradas do usuário.
* Controle de posições já utilizadas.
* Ataques alternados entre jogador e computador.
* Exibição da quantidade de embarcações restantes.
* Sistema de vitória e derrota.

---

## 🎮 Legenda do Jogo

| Símbolo | Significado          |
| ------- | -------------------- |
| 🌊      | Posição não revelada |
| 💥      | Embarcação atingida  |
| 👎      | Ataque sem sucesso   |

---

## 📂 Estrutura do Projeto

```text
Batalha-Naval/
│
├── main.py
└── README.md
```

### Principais Funções

| Função               | Descrição                                                            |
| -------------------- | -------------------------------------------------------------------- |
| `maquina()`          | Cria o tabuleiro do computador e posiciona os navios aleatoriamente. |
| `humano()`           | Cria o tabuleiro do jogador com as posições escolhidas.              |
| `escolha_humano()`   | Recebe as posições das embarcações do jogador.                       |
| `ataque_humano()`    | Processa os ataques realizados pelo jogador.                         |
| `ataque_maquina()`   | Processa os ataques realizados pelo computador.                      |
| `feedback_humano()`  | Exibe o resultado do ataque do jogador.                              |
| `feedback_maquina()` | Exibe o resultado do ataque do computador.                           |
| `mostrador()`        | Atualiza e exibe os tabuleiros.                                      |
| `incial()`           | Inicializa os tabuleiros do jogo.                                    |
| `main()`             | Controla toda a execução do programa.                                |

---

## ▶️ Como Executar

### Pré-requisitos

* Python 3.x instalado

### Execução

No terminal, execute:

```bash
python main.py
```

---

## 🧠 Conceitos Utilizados

Durante o desenvolvimento foram aplicados os seguintes conceitos:

* Algoritmos
* Lógica de Programação
* Estruturas Condicionais (`if`, `elif`, `else`)
* Estruturas de Repetição (`for` e `while`)
* Funções
* Matrizes
* Listas
* Geração de números aleatórios com a biblioteca `random`
* Validação de dados de entrada
* Modularização de código

---

## 🏫 Informações Acadêmicas

**Instituição:** Pontifícia Universidade Católica do Paraná (PUCPR)

**Disciplina:** Raciocínio Algorítmico

**Ano:** 2026

---

## 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos como atividade da disciplina de Raciocínio Algorítmico da PUCPR.
