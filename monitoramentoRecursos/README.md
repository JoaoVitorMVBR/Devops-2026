# Monitor de Sistema

Este script em Python monitora o uso de CPU, memória e disco do sistema em tempo real.

## Funcionalidades

- **CPU**: Exibe a porcentagem de uso da CPU.
- **Memória**: Mostra a porcentagem de uso da memória RAM, além dos valores em GB usados e total.
- **Disco**: Monitora o uso do disco raiz (/), exibindo porcentagem, espaço usado e total em GB.
- Atualização automática a cada 5 segundos.
- Interrupção manual com Ctrl+C.

## Pré-requisitos

- Python 3.6 ou superior.
- Biblioteca `psutil` instalada.

## Instalação

1. Clone ou baixe o repositório.
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```
   python -m venv .venv
   source .venv/bin/activate  # No Linux/Mac
   ```
3. Instale as dependências:
   ```
   pip install psutil
   ```

## Uso

Execute o script no terminal:

```
python monitor_sistema.py
```

O monitoramento começará imediatamente e exibirá as métricas no console.

### Exemplo de Saída

```
CPU: 5.7%
Memória: 35.1% (2.7 GB / 7.6 GB)
Disco (/): 1.7% (16.4 GB / 1006.9 GB)
--------------------------------------------------
CPU: 0.9%
Memória: 35.1% (2.7 GB / 7.6 GB)
Disco (/): 1.7% (16.4 GB / 1006.9 GB)
--------------------------------------------------
```

## Como Parar

Pressione `Ctrl+C` no terminal para interromper o monitoramento.

## Personalização

- Para alterar o intervalo de atualização, modifique o parâmetro `intervalo` na função `monitorar_sistema()` (padrão: 5 segundos).
- Para monitorar outros discos, altere o caminho em `psutil.disk_usage('/')` para o desejado (ex.: '/home').
- Adicione alertas ou logs editando o código para verificar limites e enviar notificações.

## Licença

Este projeto é de uso livre. Modifique conforme necessário.