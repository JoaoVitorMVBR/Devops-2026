#!/usr/bin/env python3
"""
Script de monitoramento de sistema: CPU, Disco e Memória
Usa a biblioteca psutil para coletar métricas.
Instale com: pip install psutil
"""

import psutil
import time

def monitorar_sistema(intervalo=5):
    """
    Monitora CPU, disco e memória a cada 'intervalo' segundos.
    Pressione Ctrl+C para parar.
    """
    try:
        while True:
            # CPU
            cpu_percent = psutil.cpu_percent(interval=1)
            print(f"CPU: {cpu_percent}%")

            # Memória
            memoria = psutil.virtual_memory()
            memoria_percent = memoria.percent
            memoria_usada_gb = memoria.used / (1024 ** 3)
            memoria_total_gb = memoria.total / (1024 ** 3)
            print(f"Memória: {memoria_percent:.1f}% ({memoria_usada_gb:.1f} GB / {memoria_total_gb:.1f} GB)")

            # Disco
            disco = psutil.disk_usage('/')
            disco_percent = disco.percent
            disco_usado_gb = disco.used / (1024 ** 3)
            disco_total_gb = disco.total / (1024 ** 3)
            print(f"Disco (/): {disco_percent:.1f}% ({disco_usado_gb:.1f} GB / {disco_total_gb:.1f} GB)")

            print("-" * 50)
            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("\nMonitoramento interrompido.")

if __name__ == "__main__":
    monitorar_sistema()