<<<<<<< HEAD
# Vision WhatsApp Bot

Um bot moderno para WhatsApp usando WAHA (WhatsApp HTTP API) com Flask webhook handler e Docker.

## 🚀 Características


## 📋 Pré-requisitos


## 🛠️ Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/vision-whatsapp-bot.git
cd vision-whatsapp-bot
```

### 2. Configure as variáveis de ambiente (opcional)
Edite o arquivo `docker-compose.yml` se necessário:

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


## 📡 API Endpoints

### WAHA API (Porta 3000)

### Webhook API (Porta 5678)

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

## 🙏 Agradecimentos

=======
# vision-whatsapp-bot
>>>>>>> 5708ff45fb4bd76a3f233bb111c7ebbb7681fb4c
