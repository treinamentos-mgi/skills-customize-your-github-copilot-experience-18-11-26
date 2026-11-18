
# 🎮 Tarefa: Jogo da Forca

## 🎯 Objetivo

Pratique manipulação de strings, listas, seleção aleatória, entrada de dados, loops e condicionais criando um jogo da Forca em Python.

## 📝 Tarefas

### 🛠️ Preparação da Palavra e do Jogo

#### Descrição
Prepare uma rodada selecionando uma palavra secreta da lista fornecida e inicializando as variáveis que serão usadas para acompanhar os palpites.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista `words` usando o módulo `random`.
- Inicializar uma coleção para registrar as letras já adivinhadas.
- Definir e inicializar o limite de tentativas incorretas.
- Exibir o progresso da palavra, mostrando as letras adivinhadas e espaços para as letras ainda não descobertas, como `_ _ _`.

### 🛠️ Rodada de Adivinhação

#### Descrição
Implemente o loop principal para receber palpites, atualizar o estado do jogo e informar o resultado da rodada.

#### Requisitos
O programa concluído deve:

- Solicitar ao jogador um palpite de letra e verificar se ela aparece na palavra secreta.
- Atualizar e exibir o progresso após cada palpite.
- Contabilizar e informar as tentativas incorretas restantes.
- Encerrar a rodada quando a palavra for descoberta ou o limite de tentativas incorretas for atingido.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra secreta.
