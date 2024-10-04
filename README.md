# Banco LHRBF

Este é um simples sistema bancário em Python, que permite ao usuário realizar operações de depósito, saque, verificar o saldo e sair do sistema.

## Funcionalidades

O programa oferece as seguintes funcionalidades:

1. **Depósito**: Permite ao usuário depositar dinheiro em sua conta.
2. **Saque**: Permite ao usuário sacar dinheiro, desde que tenha saldo suficiente.
3. **Extrato**: Exibe o saldo atual da conta.
4. **Sair**: Encerra o programa.

## Como usar

1. Ao iniciar o programa, o saldo inicial será de R$2500.
2. O menu oferece quatro opções:
   - `1`: Para depositar um valor.
   - `2`: Para sacar um valor.
   - `3`: Para verificar o saldo.
   - `0`: Para sair do programa.
3. Após selecionar uma opção, o programa solicitará o valor (para depósito ou saque) ou exibirá o saldo atual.
4. Caso o valor de saque seja maior que o saldo disponível, o programa exibirá uma mensagem de saldo insuficiente.

## Exemplo de uso

```bash
Bem-vindo ao Banco LHRBF!

1 - Depósito
2 - Saque
3 - Extrato
0 - Sair
Escolha uma opção: 1
Digite o valor do depósito: 500
Depósito de R$500.00 realizado com sucesso!

Bem-vindo ao Banco LHRBF!

1 - Depósito
2 - Saque
3 - Extrato
0 - Sair
Escolha uma opção: 3
Seu saldo é: R$3000.00
