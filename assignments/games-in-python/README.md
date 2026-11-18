
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Pratique manipulação de strings, listas, seleção aleatória, entrada de dados, loops e condicionais criando um jogo da Forca em Python.

## 📝 Tarefas

### 🛠️ Preparar a Palavra e o Estado do Jogo

#### Descrição

Prepare uma rodada selecionando uma palavra secreta da lista fornecida e inicializando as variáveis usadas para acompanhar os palpites e as tentativas.

#### Requisitos

O programa concluído deve:

- Selecionar aleatoriamente uma palavra de uma lista predefinida usando o módulo `random`.
- Inicializar uma coleção para registrar as letras já adivinhadas.
- Definir o limite de tentativas incorretas.
- Exibir o progresso da palavra, mostrando as letras descobertas e espaços para as letras restantes, como `_ _ _`.

### 🛠️ Implementar as Rodadas de Adivinhação

#### Descrição

Implemente o loop principal para receber palpites, atualizar o estado do jogo e informar o resultado de cada rodada.

#### Requisitos

O programa concluído deve:

- Solicitar ao jogador um palpite de letra e verificar se ela aparece na palavra secreta.
- Atualizar e exibir o progresso após cada palpite.
- Contabilizar e informar as tentativas incorretas restantes.
- Encerrar quando a palavra for descoberta ou o limite de tentativas incorretas for atingido.
- Exibir uma mensagem de vitória ou derrota e revelar a palavra secreta em caso de derrota.