🃏 Deck Generator & Dealer (Python)
Este é um projeto em Python para geração, manipulação e distribuição de cartas de baralhos. O sistema permite configurar múltiplos baralhos, adicionar coringas e distribuir cartas para um número variável de jogadores.

🚀 Funcionalidades
Customização de Baralho: Escolha quantas cópias de baralhos de 52 cartas deseja utilizar.

Coringas Opcionais: Opção para incluir dois coringas (JK1 e JK2) por baralho.

Embaralhamento Inteligente: Sistema que utiliza a biblioteca random para garantir a aleatoriedade das cartas.

Distribuição Dinâmica: Lógica para entregar um número específico de cartas para uma quantidade definida de jogadores.

🛠️ Como Funciona
O projeto está dividido em dois núcleos principais:

1. Geração (gerar_baralho)
Localizada no módulo de lógica, esta função constrói o baralho combinando:

Naipes: ♠, ♣, ♥, ♦

Valores: A, 2-10, J, Q, K

Coringas: Adicionados conforme a escolha do usuário.

2. Distribuição (distribuir)
A função de distribuição gerencia a lógica de retirada de cartas:

Remove as cartas do baralho principal (usando pop()).

Organiza as "mãos" individuais em uma lista de jogadores.
