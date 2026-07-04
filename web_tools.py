import socket
import requests

def run_subdomain_bruteforce(t):
    target_domain = input(t['ask_domain']).strip()
    print(t['sub_start'])
    
    try:
        with open("subdomains.txt", "r", encoding="utf-8") as file:
            subdomains = [line.strip() for line in file if line.strip()]
            
        total = len(subdomains)
        
        for index, sub in enumerate(subdomains, 1):
            full_url = f"{sub}.{target_domain}"
            percent = (index / total) * 100
            bar = "█" * int(percent // 10) + "░" * (10 - int(percent // 10))
            print(f"\r[{bar}] {percent:.1f}% ({index}/{total})", end="", flush=True)
            
            try:
                ip = socket.gethostbyname(full_url)
                print("\r" + " " * 70 + "\r", end="")
                print(t['sub_found'].format(url=full_url, ip=ip))
            except socket.gaierror:
                pass
                
    except FileNotFoundError:
        print("\n[!] Error: 'subdomains.txt' not found!")
    except KeyboardInterrupt:
        print("\n[!] Error / Прервано пользователем.")
        
    print("\n" + t['sub_done'])

def run_directory_bruteforce(t):
    target_url = input(t['ask_url']).strip()
    
    clean_name = target_url.replace("https://", "").replace("http://", "").replace("/", "_")
    report_file = f"report_dir_{clean_name}.txt"
    
    print(t['dir_start'])
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
    }
    
    garbage_detector = {}
    
    try:
        with open("directories.txt", "r", encoding="utf-8") as file:
            dirs = [line.strip() for line in file if line.strip()]
            
        total = len(dirs)
        
        for index, d in enumerate(dirs, 1):
            if target_url.endswith('/'):
                full_url = f"{target_url}{d}"
            else:
                full_url = f"{target_url}/{d}"
                
            percent = (index / total) * 100
            bar = "█" * int(percent // 10) + "░" * (10 - int(percent // 10))
            print(f"\r[{bar}] {percent:.1f}% ({index}/{total})", end="", flush=True)
            
            try:
                response = requests.get(full_url, headers=headers, timeout=2.5, allow_redirects=False)
                
                size = len(response.content)
                response_key = (response.status_code, size)
                
                garbage_detector[response_key] = garbage_detector.get(response_key, 0) + 1
                
                if response.status_code in [200, 301, 302, 403]:
                    
                    if garbage_detector[response_key] > 3:
                        if garbage_detector[response_key] == 4:
                            print("\r" + " " * 80 + "\r", end="")
                            print(f"[!] Filter (404) {full_url} -> [Status: {response.status_code}]")
                        continue
                        
                    result_str = t['dir_found'].format(url=full_url, code=response.status_code, size=size)
                    
                    print("\r" + " " * 80 + "\r", end="")
                    print(result_str)
                    
                    file_log_str = f"[+] Found: {full_url} -> [Status: {response.status_code}]"
                    with open(report_file, "a", encoding="utf-8") as report:
                        report.write(file_log_str + "\n")
                        
            except requests.exceptions.RequestException:
                pass
                
    except FileNotFoundError:
        print("\n[!] Error: 'directories.txt' not found!")
    except KeyboardInterrupt:
        print("\n[!] Error / Прервано пользователем.")
        
    print("\n" + t['dir_done'].format(file=report_file))

def run_header_analyzer(t):
    target_url = input(t['ask_url']).strip()
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'https://' + target_url
        
    print(t['ha_requesting'].format(url=target_url))
    
    headers_to_check = {
        'Content-Security-Policy': 'desc_csp',
        'X-Frame-Options': 'desc_xfo',
        'X-Content-Type-Options': 'desc_xcto',
        'Strict-Transport-Security': 'desc_hsts'
    }
    
    try:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        response = requests.get(target_url, headers={'User-Agent': user_agent}, timeout=5, allow_redirects=True)
        
        print("=" * 50)
        print(t['ha_tech_title'])
        print("=" * 50)
        
        server = response.headers.get('Server', 'Hidden / Unknown')
        powered_by = response.headers.get('X-Powered-By', 'Hidden / Unknown')
        
        print(t['ha_server'].format(server=server))
        print(t['ha_powered'].format(powered=powered_by))
        
        print("\n" + "=" * 50)
        print(t['ha_sec_title'])
        print("=" * 50)
        
        missing_count = 0
        for header, desc_key in headers_to_check.items():
            if header in response.headers:
                print(t['ha_present'].format(header=header))
            else:
                print(t['ha_missing'].format(header=header))
                print(t['ha_bug_hint'].format(desc=t[desc_key]))
                missing_count += 1
                
        if missing_count == 0:
            print(t['ha_all_good'])
        else:
            print(t['ha_summary'].format(count=missing_count))
            
    except requests.exceptions.RequestException as e:
        print(t['ha_conn_error'].format(error=e))