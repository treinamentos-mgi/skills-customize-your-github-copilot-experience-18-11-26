
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Pratique manipulação de strings, listas, seleção aleatória, entrada de dados, loops e condicionais criando um jogo da Forca em Python.

## 📝 Tarefas

### 🛠️ Preparar a Palavra e o Estado do Jogo

#### Descrição

Prepare uma rodada selecionando uma palavra secreta da lista fornecida e inicializando as variáveis usadas para acompanhar os palpites e as tentativas.

#### Requisitos

O programa concluído deve:

- Selecionar uma palavra aleatória da lista `words` usando `random.choice` e armazená-la em `secret_word`.
- Inicializar `guessed_letters` para acompanhar as letras adivinhadas, `incorrect_guesses` para contar os erros e `max_incorrect` para definir o limite de erros.
- Exibir cada letra já adivinhada e usar `_` para representar cada letra ainda não descoberta, como `_ _ _`.

### 🛠️ Implementar as Rodadas de Adivinhação

#### Descrição

Implemente o loop principal para receber palpites, atualizar o estado do jogo e informar o resultado de cada rodada.

#### Requisitos

O programa concluído deve:

- Solicitar um palpite de letra a cada rodada e verificar se a letra aparece em `secret_word`.
- Registrar as letras corretas em `guessed_letters` e incrementar `incorrect_guesses` quando o palpite estiver errado.
- Exibir o progresso da palavra e quantas tentativas incorretas ainda restam após cada palpite.
- Encerrar a partida quando todas as letras forem descobertas ou `incorrect_guesses` atingir `max_incorrect`.
- Exibir uma mensagem de vitória ou derrota e revelar `secret_word` em caso de derrota.