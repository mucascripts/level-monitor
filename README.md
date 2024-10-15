## Como utilizar:

### 1 - Crie o bot do Telegram que irá te mandar as mensagens;

Instruções neste link: https://canaltech.com.br/apps/como-criar-um-bot-no-telegram-botfather/ \
Anote o API-Token gerado para o bot.

### 2 - Descubra o seu Chat-ID;

Inicie uma conversa com `@getidsbot`. \
O bot enviará algumas informações e, dentre elas, o seu ID.

### 3 - Crie o arquivo `.env`;

Faça uma cópia do arquivo já existente `.env.example` e renomeie para `.env`.
Preencha os valores com seus dados.

- `CHARS_NAMES`: Nomes dos personagens separados por vírgula. \
  Exemplo: `CHARS_NAMES=BK_Nome1,char2,char3_SM`

- `GUILD_NAME`: Nome da guild em que os personagens estão. \
  Exemplo: `GUILD_NAME=GuildDaora`

- `GUILD_PAGE`: Número da página da guild em que os personagens se encontram. Pode ser 1 ou 2. \
  Exemplo: `GUILD_PAGE=2`

- `RESET_TABLE`: Tipo de conta dos personagens. Pode ser `free` ou `premium`. \
  Exemplo: `RESET_TABLE=premium`

- `TELEGRAM_BOT_API_TOKEN`: API-Token gerado ao criar o bot no passo 1 das instruções. \
  Exemplo: `TELEGRAM_BOT_API_TOKEN=0123456789:abcdefgh1234aaaaaabbbbbbbbbcccccccc`

- `TELEGRAM_CHAT_ID`: Seu chat ID obtido no passo 2 das instruções. \
  Exemplo: `TELEGRAM_CHAT_ID=0123456789`

### 4 - Instale as dependências do programa;

No terminal: `pip install .`

### 5 - Execute o programa;

No terminal: `python ./bin/run.py`
