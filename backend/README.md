backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Inicialização do FastAPI
│   │
│   ├── routers/                # Rotas e endpoints da API e schemas
│   │   ├── __init__.py
│   │   ├── users.py
│   │   └── products.py
│   │
│   ├── models/                 # Modelos do banco de dados
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── product.py
│   │
│   ├── db/               # Conexão e operações do banco
│   │   ├── __init__.py
│   │   └── connection.py
│   │
│   └── core/                   # Configurações compartilhadas
│       ├── __init__.py
│       └── config.py
│
├── .env                        # Variáveis de ambiente
├── .gitignore
├── requirements.txt            # Dependências Python
└── README.md