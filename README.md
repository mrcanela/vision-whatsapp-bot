# Vision WhatsApp Bot

Um bot moderno para WhatsApp usando WAHA (WhatsApp HTTP API) com Flask webhook handler e Docker.

## 🚀 Características

- ✅ API HTTP para WhatsApp usando WAHA
- ✅ Webhook personalizado em Flask para receber mensagens
- ✅ Containerizado com Docker Compose
- ✅ Multi-device support
- ✅ Logs detalhados de mensagens recebidas
- ✅ Auto-restart dos containers

## 📋 Pré-requisitos

- Docker e Docker Compose instalados
- Porta 3000 e 5678 disponíveis

## 🛠️ Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/vision-whatsapp-bot.git
cd vision-whatsapp-bot
```

### 2. Configure as variáveis de ambiente (opcional)
Edite o arquivo `docker-compose.yml` se necessário:
- `WAHA_API_KEY`: Chave da API (padrão: vision123)
- `WAHA_WEBHOOK_URL`: URL do webhook (padrão: http://webhook:5678/webhook/whatsapp)

### 3. Inicie os containers
```bash
docker-compose up -d
```

### 4. Verifique os logs
```bash
# Logs do WAHA
docker logs vision-waha

# Logs do Webhook
docker logs vision-webhook
```

## 📱 Como usar

### 1. Conectar WhatsApp
Acesse: http://localhost:3000 e siga as instruções para conectar sua conta WhatsApp.

### 2. Testar a API
```bash
# Verificar status
curl http://localhost:3000/api/health

# Listar sessões
curl http://localhost:3000/api/sessions
```

### 3. Verificar webhook
```bash
# Testar endpoint do webhook
curl http://localhost:5678/
```

## 🏗️ Estrutura do Projeto

```
vision-whatsapp-bot/
├── docker-compose.yml    # Configuração dos containers
├── app.py               # Script principal (legacy)
├── waha/               # Dados persistentes do WAHA
└── webhook/            # Aplicação webhook
    ├── Dockerfile      # Container do webhook
    ├── requirements.txt # Dependências Python
    └── app.py         # Código do webhook Flask
```

## 🔧 Desenvolvimento

### Executar localmente (sem Docker)

1. **Instalar dependências:**
```bash
cd webhook
pip install -r requirements.txt
```

2. **Executar webhook:**
```bash
python app.py
```

3. **Executar WAHA separadamente:**
```bash
docker run -p 3000:3000 devlikeapro/waha:latest
```

### Logs e Debug

- **Webhook logs**: As mensagens recebidas são exibidas no console com formatação JSON
- **WAHA logs**: Disponíveis através de `docker logs vision-waha`

## 📡 API Endpoints

### WAHA API (Porta 3000)
- `GET /api/health` - Status da API
- `GET /api/sessions` - Listar sessões
- `POST /api/sessions/start` - Iniciar sessão
- `POST /api/sendText` - Enviar mensagem de texto

### Webhook API (Porta 5678)
- `GET /` - Health check
- `POST /webhook/whatsapp` - Receber mensagens do WhatsApp

## 🐳 Comandos Docker Úteis

```bash
# Iniciar serviços
docker-compose up -d

# Parar serviços
docker-compose down

# Rebuild containers
docker-compose up --build -d

# Ver logs em tempo real
docker-compose logs -f

# Logs específicos
docker-compose logs webhook
docker-compose logs waha
```

## 🔐 Configurações de Segurança

- Altere a `WAHA_API_KEY` em produção
- Configure firewall para limitar acesso às portas
- Use HTTPS em produção

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📞 Suporte

Para suporte e dúvidas:
- Abra uma issue no GitHub
- Consulte a documentação do [WAHA](https://waha.devlike.pro/)

## 🙏 Agradecimentos

- [WAHA](https://waha.devlike.pro/) - WhatsApp HTTP API
- [Flask](https://flask.palletsprojects.com/) - Framework web Python
- [Docker](https://docker.com/) - Containerização