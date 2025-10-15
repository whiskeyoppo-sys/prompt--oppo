import random, time
from utils.logger import log_info, log_success, log_warning
from config import PROJECT_CONFIG

FAST = PROJECT_CONFIG.get("fast_mode", False)

def safe_sleep(sec):
    if not FAST:
        time.sleep(sec)

def automate_tasks():
    log_info("📅 Starting automated scheduling...")
    safe_sleep(random.uniform(0.5, 1.5))

    tasks = [
        "Inventory sync with suppliers",
        "Price adjustments",
        "Customer notifications",
        "Analytics report generation",
        "Order processing",
        "Product moderation",
        "Marketing campaign launch"
    ]

    for i, task in enumerate(tasks, 1):
        progress = random.randint(1, 100)
        log_info(f"   Task {i}: {task} ({progress}%)")
        safe_sleep(random.uniform(0.1, 0.5))

    log_success("✅ Scheduled tasks completed successfully!")
    return len(tasks)
