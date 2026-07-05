import socket
import requests

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

def run_ip_geolocation(t):
    target = input(t.get('ask_ip', '\n[?] Enter IP or Domain / Введите IP или домен: ')).strip()
    
    if not target:
        print(t.get('error', '[-] Error / Ошибка'))
        return

    print(f"\n[*] Fetching OSINT data for: {target}...")
    
    try:
        response = requests.get(f"http://ip-api.com/json/{target}?lang=en")
        data = response.json()

        if data.get("status") == "success":
            print("\n" + "="*40)
            print(f"[+] Target IP   : {data.get('query')}")
            print(f"[+] Country     : {data.get('country')} ({data.get('countryCode')})")
            print(f"[+] City/Region : {data.get('city')}, {data.get('regionName')}")
            print(f"[+] ISP         : {data.get('isp')}")
            print(f"[+] Organization: {data.get('org')}")
            print(f"[+] ASN         : {data.get('as')}")
            print(f"[+] Coordinates : {data.get('lat')}, {data.get('lon')}")
            print("="*40)
        else:
            error_msg = data.get("message", "Unknown error")
            print(f"\n[-] API Error: {error_msg}")

    except requests.exceptions.RequestException as e:
        print(f"\n[-] Connection Error: {e}")

def run_dns_recon(t):
    domain = input(t.get('ask_domain', '\n[?] Enter domain / Введите домен: ')).strip()
    
    if not domain:
        print(t.get('error', '[-] Error / Ошибка'))
        return

    # Поддерживаемые типы записей: A, MX, NS, TXT
    record_types = ['A', 'MX', 'NS', 'TXT']
    print(f"\n[*] Performing DNS Reconnaissance for: {domain}...")
    print("=" * 50)

    for record in record_types:
        try:
            # Делаем запрос к Google DNS JSON API
            url = f"https://dns.google/resolve?name={domain}&type={record}"
            response = requests.get(url)
            data = response.json()

            print(f"\n[+] Type: {record}")
            
            # Проверяем, есть ли ответы (поле 'Answer')
            if 'Answer' in data:
                for answer in data['Answer']:
                    # answer['data'] содержит сам результат записи
                    print(f"    -> {answer['data']}")
            else:
                print(f"    [-] No {record} records found.")

        except requests.exceptions.RequestException as e:
            print(f"    [-] Connection error for {record} record: {e}")
            
    print("\n" + "=" * 50)