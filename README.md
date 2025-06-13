### ✅ **1. Organização em Funções**

**Alteração:** O código foi dividido em funções (`exibir_menu`, `realizar_deposito`, `realizar_saque`, `exibir_extrato` e `main`).

**Vantagens:**

* Melhora a legibilidade e a estrutura do código.
* Facilita a manutenção, testes e reuso do código.
* Isola responsabilidades: cada função executa uma tarefa específica.

### ✅ **2. Função `main()`**

**Alteração:** Toda a lógica principal do programa foi encapsulada na função `main()`.

**Vantagens:**

* Permite que o código seja reutilizado ou testado em outros contextos.
* Segue boas práticas de programação em Python (estrutura de script).


### ✅ **3. Parâmetros e Retornos nas Funções**

**Alteração:** As funções `realizar_deposito` e `realizar_saque` recebem e retornam os dados necessários (`saldo`, `extrato`, etc.).

**Vantagens:**

* Torna o código mais claro e evita o uso excessivo de variáveis globais.
* Ajuda no controle do estado do programa.


### ✅ **4. Melhor apresentação visual**

**Alteração:** Foram adicionadas linhas visuais como:

========== MENU ==========
==========================
========== EXTRATO ==========
==============================

**Vantagens:**

* Melhora a experiência do usuário.
* Facilita a leitura do terminal.


### ✅ **5. Mensagens de erro mais claras**

**Alteração:** As mensagens foram reescritas para maior clareza, como:

* `"Operação falhou! Saldo insuficiente."`
* `"Operação falhou! O valor excede o limite por saque."`

**Vantagens:**

* Comunicação mais clara com o usuário.
* Evita ambiguidades durante a execução.


### ✅ **6. Proteção do ponto de entrada (`if __name__ == "__main__":`)**

**Alteração:** O programa só executa `main()` se for executado diretamente.

**Vantagens:**

* Permite importar esse arquivo em outro módulo sem executar o código principal automaticamente.
* Segue a convenção recomendada para scripts em Python.

