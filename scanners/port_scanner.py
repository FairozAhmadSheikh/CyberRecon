import socket
import threading

def scan(target, ports=range(1, 100)):
    open_ports = []

    def scan_port(port):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            open_ports.append(port)
            s.close()
        except:
            pass

    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return open_ports
