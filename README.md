# curso-hacking-etico-m5-leccion-6-actividad-1
Entrega módulo 5 lección 6: actividad 1 portafolio.

## Descripción
1. Asegúrate de tener instalado:
   - nmap
   - La librería python-nmap
2. Crea un script en Python que:
  - Realice un escaneo con -sV sobre la subred 192.168.1.0/24 (puedes
ajustar a la IP de tu entorno).​
  - Detecte y liste:​
      - IP del host
      - ​Puerto abierto​
      - Nombre del servicio​
      - Versión del software si está disponible​
3. Imprima un resumen ordenado por host, como si se preparara para un informe de
pentesting.​
4. Asegúrate de ejecutar este ejercicio únicamente en redes de laboratorio o con
autorización expresa.​

### Instalación de nmap
- Ubuntu: sudo apt-get update && sudo apt-get install -y nmap
- Arch: sudo pacman -Sy nmap
- Windows: [descarga](https://nmap.org/download#windows)
- Mac OSX: [instalación](https://nmap.org/book/inst-macosx.html)

### Creación del ambiente
- Creación: `python3 -m venv .venv`
- Activación: `source .venv/bin/activate`
- Desactivación: `deactivate`

### Instalación de dependencias
`pip install -r requirements.txt`

### Ejecución
`python scanner.py -n XXX.XXX.XXX.XXX\YY -p [PORT|START-END|A,B,C]`

#### Ayuda
```bash
python scanner.py -h

usage: scanner.py [-h] [-n NETWORK] [-p PORTS]

Modulo 5 - Lección 6 - Actividad 1: escaneo automatizado con nmap.

options:
  -h, --help            show this help message and exit
  -n, --network NETWORK
                        Red IPV4 a analizar en formato XXX.XXX.XXX.XXX/YY
  -p, --ports PORTS     Puerto/s a analizar en formato [PORT|START-END|A,B,C]
```

#### Salida
```bash
python scanner.py -n "192.168.1.0/24" -p 3000,5000
[Info] Scanning...
Command executed: nmap -oX - -p 3000,5000 -sV 192.168.1.0/24

Host: 192.168.1.1
- Port: 3000 -> closed
- Port: 5000 -> closed
Host: 192.168.1.84
- Port: 3000 -> open
   Node.js Express framework  
- Port: 5000 -> open
   PHP cli server 5.5 or later PHP 8.4.8
Host: 192.168.1.87
- Port: 3000 -> closed
- Port: 5000 -> closed
Host: 192.168.1.91
- Port: 3000 -> closed
- Port: 5000 -> closed


Date: 08-07-Y
Time: 22:47:38

Active Hosts: 4
```
