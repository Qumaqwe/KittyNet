import socket

def run_port_scanner(t):
    raw_target = input(t['ask_target']).strip()
    target = raw_target.replace('http://', '').replace('https://', '').split('/')[0]

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n[!] Ошибка: Не удалось определить IP-адрес. Проверьте домен (вводите без http://).")
        return

    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 1433, 1521, 3306, 3389, 5432, 5900, 6379, 8000, 8080, 8443, 9200, 27017]
    
    print(t['scan_start'] + f"{target} ({target_ip})")
    print(t['scan_wait'])
    
    try:
        for port in ports_to_scan:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target_ip, port))
            
            if result == 0:
                print(t['port_open'].format(port=port))
                
            s.close()
            
    except KeyboardInterrupt:
        print("\n[!] Error / Прервано пользователем")
        
    print(t['scan_done'])