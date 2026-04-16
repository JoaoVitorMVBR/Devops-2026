# Request Weather API

Projeto que faz requisições à API **Open-Meteo** para obter dados de previsão de tempo (temperatura horária) para Belo Horizonte, MG.

## 🌍 O que faz

- Conecta-se à API Open-Meteo sem autenticação
- Obtém dados de temperatura horária para coordenadas específicas (Belo Horizonte)
- Exibe as coordenadas, fuso horário e previsão de temperatura para as próximas 24 horas
- Implementa cache e retry automático para maior confiabilidade

## 📋 Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes)

## 🚀 Instalação

### 1. Clone ou navegue até o diretório do projeto

```bash
cd /home/joaovilas/pessoal/devops-2026/requestWeatherApi
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python3 -m venv venv
```

### 3. Ative o ambiente virtual

**Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

## ▶️ Como executar

Com o ambiente virtual ativado, execute:

```bash
python3 main.py
```

### Saída esperada

```
Coordinates: -19.92°N, -43.94°E
Timezone: America/Sao_Paulo

Hourly temperature forecast:
Hour 0: 28.5°C
Hour 1: 27.8°C
Hour 2: 27.2°C
...
```

## 📦 Dependências

Veja o arquivo `requirements.txt` para lista completa. As principais são:

- `openmeteo-requests` - Cliente para API Open-Meteo
- `requests-cache` - Cache para requisições HTTP
- `retry-requests` - Retry automático com backoff
- `numpy` - Manipulação de dados numéricos

## 📝 Configuração

No arquivo `main.py`, você pode modificar:

- **Latitude/Longitude**: Altere as coordenadas para outra localidade
- **Variáveis horárias**: Adicione mais variáveis em `"hourly"` (ex: `"temperature_2m,precipitation,windspeed_10m"`)
- **Timezone**: Ajuste o fuso horário conforme necessário

## 🔗 Referências

- [Open-Meteo API Documentation](https://open-meteo.com/en/docs)
- [Python Requests](https://requests.readthedocs.io/)
