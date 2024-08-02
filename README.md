# Sistema Bancário Orientado a Objetos

> [!NOTE]
> Este projeto é um sistema bancário desenvolvido com princípios de Programação Orientada a Objetos (POO). Ele permite a criação e gerenciamento de contas bancárias, incluindo contas correntes e contas poupança.<br>

#### Estrutura do Sistema

O sistema é composto pelas seguintes classes:

-Pessoa: Representa uma pessoa com nome e idade.<br>
-Cliente: Herda de Pessoa e representa um cliente do banco, agregando uma conta bancária (pode ser conta corrente ou conta poupança).<br>
-Conta (ABC): Classe abstrata que define os atributos e métodos básicos de uma conta bancária.<br>
-ContaCorrente: Herda de Conta e inclui um limite extra para a conta corrente.<br>
-ContaPoupanca: Herda de Conta e representa uma conta poupança.<br>
-Banco: Agrega clientes e contas, sendo responsável por autenticar clientes e contas, além de gerenciar operações bancárias.<br>

#### Funcionalidades

-Criação de Clientes e Contas: Permite a criação de clientes, cada um com uma conta associada (corrente ou poupança).<br>
-Depósitos e Saques: Implementa métodos para realizar depósitos e saques em contas. Contas correntes possuem um limite extra para saques.<br>
-Autenticação de Clientes e Contas: O banco autentica clientes e suas respectivas contas, verificando se a agência, o cliente e a conta são válidos.<br>
-Verificação de Agências: Confirma se uma conta pertence a uma agência específica do banco.<br>

Contribuições: <br>
`Contribuições são bem-vindas! Se você encontrar algum problema, bug ou tiver alguma sugestão de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.`<br>

LICENSE: <br>
`MIT License
Copyright (c) 2024 Bernardo Cezar Alves de Oliveira`
