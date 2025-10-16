import time
from datetime import datetime

class Logger:
    COLORS = {'red':'\033[91m','green':'\033[92m','yellow':'\033[93m','blue':'\033[94m','magenta':'\033[95m','cyan':'\033[96m','white':'\033[97m','reset':'\033[0m'}
    @staticmethod
    def _timestamp(): return datetime.now().strftime('%H:%M:%S')
    @staticmethod
    def log_info(msg): print(f"{Logger.COLORS['cyan']}[{Logger._timestamp()}] ℹ️ {msg}{Logger.COLORS['reset']}")
    @staticmethod
    def log_success(msg): print(f"{Logger.COLORS['green']}[{Logger._timestamp()}] ✅ {msg}{Logger.COLORS['reset']}")
    @staticmethod
    def log_warning(msg): print(f"{Logger.COLORS['yellow']}[{Logger._timestamp()}] ⚠️ {msg}{Logger.COLORS['reset']}")
    @staticmethod
    def log_error(msg): print(f"{Logger.COLORS['red']}[{Logger._timestamp()}] ❌ {msg}{Logger.COLORS['reset']}")

def log_info(msg): Logger.log_info(msg)
def log_success(msg): Logger.log_success(msg)
def log_warning(msg): Logger.log_warning(msg)
def log_error(msg): Logger.log_error(msg)
