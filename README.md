# 📂 RPA - Automatizador de Boletos PDF

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-green)

![Demonstração do projeto](echo '# 📂 RPA - Automatizador de Boletos PDF

![Python](https://img.shields.io/badge/Python-3.12-blue)
'/home/jonas/Downloads/AdobeExpress-ghostmachineExecutando-OracleVirtualBox2025-08-0320-55-17-ezgif.com-video-to-gif-converter.mp4' ![Docker](https://img.shields.io/badge/Docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-green)

![Demonstração do projeto](echo '# 📂 RPA - Automatizador de Boletos PDF

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-green)

![Demonstração do projeto](./screenshots/montana-resort.gif)


Automatizador de boletos em PDF com RPA desenvolvido em Python.  
Esse projeto extrai automaticamente dados como **CNPJ**, **valor** e **data de vencimento** de boletos em formato PDF, exportando para um arquivo CSV pronto para uso em sistemas financeiros.

## 🚀 Tecnologias usadas

- Python 3.12  
- pypdf  
- pandas  
- Docker  
- GitHub Actions (CI/CD)  

## 💻 Como usar localmente

1. Clone o projeto  
2. Crie e ative o ambiente virtual:

   python3 -m venv .venv  
   source .venv/bin/activate.fish  # ou source .venv/bin/activate no bash

3. Instale as dependências com:  

   pip install -r requirements.txt

4. Coloque seus PDFs na pasta \`pdfs/\`  
5. Execute o script:  

   python main.py pdfs

6. O arquivo \`boletos_extraidos.csv\` será criado na raiz.

---

### 🧾 Exemplo de saída:

| CNPJ               | Valor      | Vencimento  |
|--------------------|------------|-------------|
| 12.345.678/0001-90 | R$ 321,45  | 10/08/2025  |

## 🐳 Usando Docker

Execute:

docker build -t rpa-boletos .  
docker run --rm -v $(pwd)/pdfs:/app/pdfs rpa-boletos python main.py pdfs

## ⚙️ CI/CD

Usamos GitHub Actions para rodar testes e automatizar processos a cada push.

## 🧪 Testes

Os testes ficam na pasta \`Tests/\`. Para rodar, use:

pytest

---

## 👤 Autor

Ifeson Jonas
' > README.md
)

📽️ [Clique aqui para ver a demonstração em vídeo](https://www.youtube.com/SEU-LINK-AQUI)

Automatizador de boletos em PDF com RPA desenvolvido em Python.  
Esse projeto extrai automaticamente dados como **CNPJ**, **valor** e **data de vencimento** de boletos em formato PDF, exportando para um arquivo CSV pronto para uso em sistemas financeiros.

## 🚀 Tecnologias usadas

- Python 3.12  
- pypdf  
- pandas  
- Docker  
- GitHub Actions (CI/CD)  

## 💻 Como usar localmente

1. Clone o projeto  
2. Crie e ative o ambiente virtual:

   python3 -m venv .venv  
   source .venv/bin/activate.fish  # ou source .venv/bin/activate no bash

3. Instale as dependências com:  

   pip install -r requirements.txt

4. Coloque seus PDFs na pasta \`pdfs/\`  
5. Execute o script:  

   python main.py pdfs

6. O arquivo \`boletos_extraidos.csv\` será criado na raiz.

---

### 🧾 Exemplo de saída:

| CNPJ               | Valor      | Vencimento  |
|--------------------|------------|-------------|
| 12.345.678/0001-90 | R$ 321,45  | 10/08/2025  |

## 🐳 Usando Docker

Execute:

docker build -t rpa-boletos .  
docker run --rm -v $(pwd)/pdfs:/app/pdfs rpa-boletos python main.py pdfs

## ⚙️ CI/CD

Usamos GitHub Actions para rodar testes e automatizar processos a cada push.

## 🧪 Testes

Os testes ficam na pasta \`Tests/\`. Para rodar, use:

pytest

---

## 👤 Autor

Ifeson Jonas
' > README.md
)

📽️ [Clique aqui para ver a demonstração em vídeo](https://www.youtube.com/SEU-LINK-AQUI)

Automatizador de boletos em PDF com RPA desenvolvido em Python.  
Esse projeto extrai automaticamente dados como **CNPJ**, **valor** e **data de vencimento** de boletos em formato PDF, exportando para um arquivo CSV pronto para uso em sistemas financeiros.

## 🚀 Tecnologias usadas

- Python 3.12  
- pypdf  
- pandas  
- Docker  
- GitHub Actions (CI/CD)  

## 💻 Como usar localmente

1. Clone o projeto  
2. Crie e ative o ambiente virtual:

   python3 -m venv .venv  
   source .venv/bin/activate.fish  # ou source .venv/bin/activate no bash

3. Instale as dependências com:  

   pip install -r requirements.txt

4. Coloque seus PDFs na pasta \`pdfs/\`  
5. Execute o script:  

   python main.py pdfs

6. O arquivo \`boletos_extraidos.csv\` será criado na raiz.

---

### 🧾 Exemplo de saída:

| CNPJ               | Valor      | Vencimento  |
|--------------------|------------|-------------|
| 12.345.678/0001-90 | R$ 321,45  | 10/08/2025  |

## 🐳 Usando Docker

Execute:

docker build -t rpa-boletos .  
docker run --rm -v $(pwd)/pdfs:/app/pdfs rpa-boletos python main.py pdfs

## ⚙️ CI/CD

Usamos GitHub Actions para rodar testes e automatizar processos a cada push.

## 🧪 Testes

Os testes ficam na pasta \`Tests/\`. Para rodar, use:

pytest

---

## 👤 Autor

Ifeson Jonas

