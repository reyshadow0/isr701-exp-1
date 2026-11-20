import socket
import threading
import time

HOST, PORT = "127.0.0.1", 5002

def servidor_udp():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        datos, addr = s.recvfrom(1024)  
        print(f"[UDP Servidor] Datagrama de {addr}: {datos.decode()}")
        s.sendto(b"Recibido por UDP (sin garantia de entrega)", addr)

def cliente_udp():
    time.sleep(0.3)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"Paquete rapido por UDP", (HOST, PORT))
        respuesta, _ = s.recvfrom(1024)
        print(f"[UDP Cliente] Respuesta: {respuesta.decode()}")

if __name__ == "__main__":
    t = threading.Thread(target=servidor_udp)
    t.start()
    cliente_udp()
    t.join()
