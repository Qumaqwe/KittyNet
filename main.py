import network_tools
import web_tools
LOCALIZATION = {
    'ru': {
        'welcome': "\033[92m" + r"""
██╗  ██╗██╗████████╗████████╗██╗   ██╗███╗   ██╗███████╗████████╗
██║ ██╔╝██║╚══██╔══╝╚══██╔══╝╚██╗ ██╔╝████╗  ██║██╔════╝╚══██╔══╝
█████╔╝ ██║   ██║      ██║    ╚████╔╝ ██╔██╗ ██║█████╗     ██║   
██╔═██╗ ██║   ██║      ██║     ╚██╔╝  ██║╚██╗██║██╔══╝     ██║   
██║  ██╗██║   ██║      ██║      ██║   ██║ ╚████║███████╗   ██║   
╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝      ╚═╝   ╚═╝  ╚═══╝╚══════╝   ╚═╝
        """ + "\033[0m",
        'ask_choice': "\n[>] Выберите пункт меню: ",
        'scanning': "\n[*] Запуск сканирования портов...",
        'goodbye': "\n[!] Выход из программы. Пока!",
        'error': "\n[!] Ошибка: Неверный пункт меню!",
        'ask_domain': "[?] Введите целевой домен (например, example.com): ",
        'ask_url': "[?] Введите полный URL цели (например, https://example.com): ",

        'ask_target': "[?] Введите целевой IP или домен для сканирования: ",
        'scan_start': "\n[*] Сканирование цели: ",
        'scan_wait': "[*] Пожалуйста, подождите, идет проверка портов...",
        'port_open': "[+] Порт {port} ОТКРЫТ",
        'scan_done': "\n[*] Сканирование портов завершено.",

        'warning': "\033[96m▲ Use only for security testing\033[0m",
        
        'menu_header': "\n\033[95m================================================================================\nSelect a Category\033[0m",

        'menu_1': "\033[96m[1]\033[0m Port Scanner",
        'menu_2': "\033[96m[2]\033[0m Subdomain Bruteforce",
        'menu_3': "\033[96m[3]\033[0m Directory Bruteforce [Auto-logger]",
        'menu_4': "\033[96m[4]\033[0m Web Header & Security Analyzer",
        'menu_5': "\033[96m[5]\033[0m Exit",
        
        'menu_footer': "\033[95m================================================================================\033[0m",

        'sub_start': "\n[*] Начинаем поиск поддоменов...\n",
        'sub_found': "[+] Найдено: {url} -> IP: {ip}",
        'sub_done': "[*] Поиск поддоменов завершен.",
        
        'dir_start': "\n[*] Начинаем сканирование путей. Пожалуйста, подождите...\n",
        'dir_found': "[+] Найдено: {url} -> [{code}]",
        'dir_done': "\n[*] Сканирование завершено. Результаты сохранены в файл: {file}",
        
        'ha_requesting': "\n[*] Запрашиваем заголовки для {url}...\n",
        'ha_tech_title': "ТЕХНОЛОГИИ И СЕРВЕР:",
        'ha_sec_title': "АНАЛИЗ БЕЗОПАСНОСТИ ЗАГОЛОВКОВ:",
        'ha_server': "[i] Веб-сервер: {server}",
        'ha_powered': "[i] Движок/Платформа: {powered}",
        'ha_present': "[+] [СТОИТ] {header}",
        'ha_missing': "[-] [ОТСУТСТВУЕТ] {header}",
        'ha_bug_hint': "    💡 ПОТЕНЦИАЛЬНЫЙ БАГ: {desc}",
        'ha_all_good': "\n[🎉] Отлично! Сайт использует все базовые заголовки безопасности.",
        'ha_summary': "\n[!] Анализ завершен. Найдено отсутствующих заголовков: {count}\n    Новички могут оформить это как Missing Security Headers в Bug Bounty!",
        'ha_conn_error': "[!] Ошибка подключения: {error}",
        'ha_press_enter': "\nНажмите Enter, чтобы выйти...",
        
        'desc_csp': "Защищает от XSS (внедрения вредоносного скрипта).",
        'desc_xfo': "Защищает от Clickjacking (кражи кликов через невидимые фреймы).",
        'desc_xcto': "Запрещает браузеру угадывать MIME-тип файла (защита от Sniffing).",
        'desc_hsts': "HSTS — принудительно включает безопасное HTTPS соединение."
    },
    'en': {
        'welcome': "\033[92m" + r"""
██╗  ██╗██╗████████╗████████╗██╗   ██╗███╗   ██╗███████╗████████╗
██║ ██╔╝██║╚══██╔══╝╚══██╔══╝╚██╗ ██╔╝████╗  ██║██╔════╝╚══██╔══╝
█████╔╝ ██║   ██║      ██║    ╚████╔╝ ██╔██╗ ██║█████╗     ██║   
██╔═██╗ ██║   ██║      ██║     ╚██╔╝  ██║╚██╗██║██╔══╝     ██║   
██║  ██╗██║   ██║      ██║      ██║   ██║ ╚████║███████╗   ██║   
╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝      ╚═╝   ╚═╝  ╚═══╝╚══════╝   ╚═╝
        """ + "\033[0m",
        'ask_choice': "\n[>] Choose an option: ",
        'scanning': "\n[*] Launching port scanner...",
        'goodbye': "\n[!] Exiting program. Goodbye!",
        'error': "\n[!] Error: Invalid option!",
        'ask_domain': "[?] Enter target domain (e.g., example.com): ",
        'ask_url': "[?] Enter target full URL (e.g., https://example.com): ",

        'ask_target': "[?] Enter target IP or domain for scanning: ",
        'scan_start': "\n[*] Scanning target: ",
        'scan_wait': "[*] Please wait, checking ports...",
        'port_open': "[+] Port {port} is OPEN",
        'scan_done': "\n[*] Port scanning done.",
        
        'warning': "\033[96m▲ Use only for security testing\033[0m",

        'menu_header': "\n\033[95m================================================================================\nSelect a Category\033[0m",

        'menu_1': "\033[96m[1]\033[0m Port Scanner",
        'menu_2': "\033[96m[2]\033[0m Subdomain Bruteforce",
        'menu_3': "\033[96m[3]\033[0m Directory Bruteforce [Auto-logger]",
        'menu_4': "\033[96m[4]\033[0m Web Header & Security Analyzer",
        'menu_5': "\033[96m[5]\033[0m Exit",
        
        'menu_footer': "\033[95m================================================================================\033[0m",

        'sub_start': "\n[*] Starting subdomain bruteforce...\n",
        'sub_found': "[+] Found: {url} -> IP: {ip}",
        'sub_done': "[*] Subdomain bruteforce finished.",
        
        'dir_start': "\n[*] Starting directory scanning. Please wait...\n",
        'dir_found': "[+] Found: {url} -> [{code}]",
        'dir_done': "\n[*] Scanning finished. Results saved to: {file}",
        
        'ha_requesting': "\n[*] Requesting headers for {url}...\n",
        'ha_tech_title': "TECHNOLOGIES & SERVER:",
        'ha_sec_title': "SECURITY HEADERS ANALYSIS:",
        'ha_server': "[i] Web Server: {server}",
        'ha_powered': "[i] Engine/Platform: {powered}",
        'ha_present': "[+] [PRESENT] {header}",
        'ha_missing': "[-] [MISSING] {header}",
        'ha_bug_hint': "    💡 POTENTIAL BUG: {desc}",
        'ha_all_good': "\n[🎉] Excellent! The site uses all basic security headers.",
        'ha_summary': "\n[!] Analysis complete. Missing headers found: {count}\n    Beginners can report this as Missing Security aders in Bug Bounty!",
        'ha_conn_error': "[!] Connection error: {error}",
        'ha_press_enter': "\nPress Enter to exit...",
        
        'desc_csp': "Protects against XSS (malicious script injection).",
        'desc_xfo': "Protects against Clickjacking (stealing clicks via invisible frames).",
        'desc_xcto': "Prevents browser from guessing MIME types (Sniffing protection).",
        'desc_hsts': "HSTS — forces secure HTTPS connection."
    }
}

def main():
    print("Select language / Выберите язык:")
    print("[1] English")
    print("[2] Русский")
    
    lang_choice = input(">> ")
    
    if lang_choice == "1":
        current_lang = "en"
    else:
        current_lang = "ru"
        
    t = LOCALIZATION[current_lang]

    print(t['welcome'])
    print(t['warning'])
    print(t['menu_header'])
    print(t['menu_1'])
    print(t['menu_2'])
    print(t['menu_3'])
    print(t['menu_4'])
    print(t['menu_5'])
    print(t['menu_footer'])

    choice = input(t['ask_choice'])

    if choice == "1":
        print(t['scanning'])
        network_tools.run_port_scanner(t)
    elif choice == "2":
        web_tools.run_subdomain_bruteforce(t)
    elif choice == "3":
        web_tools.run_directory_bruteforce(t)
    elif choice == "4":
        web_tools.run_header_analyzer(t)
    elif choice == "5":
        print(t['goodbye'])
        return
    else:
        print(t['error'])

if __name__ == "__main__":
    main()