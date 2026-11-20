# Ejemplo UDP

Este ejemplo demuestra el envío y la recepción de datagramas UDP entre un servidor y un cliente locales.

## Requisitos

- Python 3
- Librerías estándar `socket` y `threading`

No es necesario instalar paquetes adicionales.

## Ejecución

Desde la raíz del repositorio, ejecuta:

```powershell
python ejemplo\udp_demo.py
```

El programa inicia el servidor UDP en `127.0.0.1:5002`, envía un datagrama desde el cliente y muestra la respuesta recibida.
