import colorama
from colorama import Fore, Style
from datetime import datetime

colorama.init()

def timestamp():
    return datetime.now().strftime('%H:%M:%S')

def log_info(message):
    print(f"{Fore.CYAN}[{timestamp()}] {message}{Style.RESET_ALL}")

def log_success(message):
    print(f"{Fore.GREEN}[{timestamp()}] ✅ {message}{Style.RESET_ALL}")

def log_warning(message):
    print(f"{Fore.YELLOW}[{timestamp()}] ⚠️  {message}{Style.RESET_ALL}")

def log_error(message):
    print(f"{Fore.RED}[{timestamp()}] ❌ {message}{Style.RESET_ALL}")

def log_debug(message):
    print(f"{Fore.MAGENTA}[{timestamp()}] 🐞 {message}{Style.RESET_ALL}")