# 🚚💰 Sistema de Cálculo de Frete para E‑commerce e Marketplaces

Um projeto **open source** desenvolvido em **Python + Flask**, com interface **Frontend (HTML, CSS e JavaScript)** para cálculo de frete baseado no **peso total dos produtos** e na **região de destino**.

Ideal para integração em plataformas como **e-commerces**, **ERPs**, **sistemas logísticos** e **marketplaces** que precisam automatizar a estimativa de frete.

---

## ✅ Funcionalidades:

* Cálculo automático de frete pelo **peso total** dos produtos;
* Adição de taxas extras conforme a **região de destino**;
* Acumuladores internos para armazenar totais de pedidos e valores gerais;
* Sistema organizado em camadas: **Backend (Flask)** + **Frontend (HTML/CSS/JS)**;
* Código simples e modular, com regras fáceis de adaptar.

---

## 💻⛏️ Tecnologias Utilizadas:

<p align="center"> 
<img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white"/> 
<img src="https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white"/> 
<img src="https://img.shields.io/badge/-JSON-000000?style=flat-square&logo=json&logoColor=white"/> 
<img src="https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/> 
<img src="https://img.shields.io/badge/-CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/> 
<img src="https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>

---

## 🧠🤔 Como o Sistema Funciona?

O projeto combina **backend em Python** com **frontend web**, permitindo que o usuário insira dados pelo navegador enquanto o processamento é feito no servidor.

### 💻🛠️ Backend (Flask + Python + Json(Gerenciador de Dados)):

* O arquivo `FreteEcommerce.py` contém toda a lógica do cálculo.
* O Flask recebe os dados enviados pelo frontend (peso e região).
* A função calcula:

  * Faixa de preço pelo peso;
  * Adicional por região;
  * Total acumulado (opcional);
* O resultado é retornado para o frontend via rota Flask.

### 🎨🖌️ Frontend (HTML + CSS + JavaScript):

* O usuário preenche um formulário com **peso** e **região**;
* JavaScript envia os dados para o backend usando **json()**;
* O resultado é exibido automaticamente na tela;
* CSS estiliza tudo em modo dark, com experiência amigável.

---

## 📁🗂️ Estrutura do Projeto:
<pre>
|main.py
|app.py
|.flaskenv
|LICENSE
|README.md
|templates/
    ├── base.html
    ├── index.html
    ├── peso.html
    ├── preco.html
    ├── regioes.html
    ├── exterior.html
    ├── resumo.html
    ├── carrinho.html
|static/
    |assets/ 
        ├──**(imagens usadas no site)**
    ├── styles.css
    ├── animacoes.js
|backending/
    ├── __init__.py
    ├── cores.py
    ├── FreteEcommerce.py
    ├── gerenciador_dados.py
    ├── mensagens.py
</pre>

## 🚀 Como o Projeto é executado (por ora):

1. Instalando o Flask (se ainda não tiver instalado):

```bash
pip install flask
```

2. Executando a aplicação Flask:

```bash
python main.py
```

3. Abra o navegador em:

```
http://localhost:5000 **porta mais comum quando não hospeado em uma url**
```

4.  Escolha seus produtos, insira peso e região de entrega, navegue mais 
e veja o cálculo e os métodos de pagamento instantaneamente.

---

## 👨‍💻 Autores:

<table align="center">
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/lucas-paguetti-pereira" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="95" />
        <br>
        <strong>Lucas Paguetti Pereira</strong>
      </a>
    </td>
    <td align="center">
      <a href="https://www.linkedin.com/in/helamã-procidio-428772367/" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="95" />
        <br>
        <strong>Helamã Leone de Lima Procidio</strong>
      </a>
    </td>
  </tr>
</table>


<br><br>

Cesar School - ADS Regular 💻🎓🧡
