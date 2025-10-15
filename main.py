import os
import json
import time
from datetime import datetime
from config import PROJECT_CONFIG

# Import modules
try:
    from modules.scheduler import automate_tasks
    from modules.commerce import manage_inventory, dynamic_pricing
    from modules.customer import personalize_messages, track_loyalty
    from modules.analytics import generate_dashboard
    from utils.logger import log_info, log_success, log_warning, log_error
except ImportError as e:
    print(f"❌ Critical import error: {e}")
    exit(1)

def print_banner():
    banner = """
    ╔════════════════════════════════════════════════════════════════════╗
    ║                🚀 O P P O C O D E - B O O M !                    ║
    ║           B U S I N E S S   A U T O M A T I O N                   ║
    ║                Platform for Android Termux                       ║
    ╚════════════════════════════════════════════════════════════════════╝
    
    ███╗   ███╗██╗    ██╗██╗  ██╗███████╗███╗   ███╗██╗███████╗███████╗
    ████╗ ████║██║    ██║██║  ██║██╔════╝████╗ ████║██║██╔════╝██╔════╝
    ██╔████╔██║██║ █╗ ██║███████║█████╗  ██╔████╔██║██║█████╗  █████╗  
    ██║╚██╔╝██║██║███╗██║██╔══██║██╔══╝  ██║╚██╔╝██║██║██╔══╝  ██╔══╝  
    ██║ ╚═╝ ██║╚███╔███╔╝██║  ██║███████╗██║ ╚═╝ ██║██║███████╗██║     
    ╚═╝     ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝╚══════╝╚═╝     
    """
    print(banner)

def print_menu():
    print("\n📋 Menu Options:")
    print("   1. 🏭 Automate Tasks")
    print("   2. 🛒 E-commerce Growth")
    print("   3. 👥 Customer Experience")
    print("   4. 📊 Analytics Dashboard")
    print("   5. 🚀 Full Automation Suite")
    print("   6. 🔍 Configuration Status")
    print("   q. 🚪 Quit")

def run_task_scheduler():
    log_info("🔁 Starting Task Scheduler...")
    try:
        automate_tasks()
        log_success("✅ Task Scheduler completed successfully!")
    except Exception as e:
        log_error(f"❌ Task Scheduler failed: {str(e)}")

def run_commerce_engine():
    log_info("🛒 Running E-commerce Growth Engine...")
    try:
        log_info("📦 Managing Inventory...")
        inventory_data = manage_inventory()
        
        log_info("💵 Dynamic Pricing Implementation...")
        pricing_data = dynamic_pricing()
        
        log_success("✅ E-commerce Growth Module completed!")
        print(f"   Inventory Analysis: {inventory_data} | Price Adjustments: {pricing_data}")
    except Exception as e:
        log_error(f"❌ E-commerce module failed: {str(e)}")

def run_customer_module():
    log_info("👥 Running Customer Experience Engine...")
    try:
        log_info("💬 Personalizing Messages...")
        message_data = personalize_messages()
        
        log_info("🎖️ Tracking Loyalty...")
        loyalty_data = track_loyalty()
        
        log_success("✅ Customer Experience Module completed!")
        print(f"   Messages Generated: {message_data} | Loyalty Points: {loyalty_data}")
    except Exception as e:
        log_error(f"❌ Customer module failed: {str(e)}")

def run_analytics_dashboard():
    log_info("📊 Generating Analytics Dashboard...")
    try:
        dashboard_data = generate_dashboard()
        log_success("✅ Analytics Dashboard generated!")
        print(f"   Data Sources: {dashboard_data}")
    except Exception as e:
        log_error(f"❌ Analytics module failed: {str(e)}")

def run_full_suite():
    log_info("🚀 Launching Full Automation Suite...")
    
    # Run all modules
    run_task_scheduler()
    run_commerce_engine()
    run_customer_module()
    run_analytics_dashboard()
    
    log_success("🎉 Full Automation Suite completed successfully!")
    print("\n✨ Ready to BOOM your business metrics!")

def check_config():
    log_info("📋 Checking Configuration Status...")
    log_success(f"✓ Project Name: {PROJECT_CONFIG['project_name']}")
    log_success(f"✓ Version: {PROJECT_CONFIG['version']}")
    log_success(f"✓ Analytics Enabled: {PROJECT_CONFIG['analytics_enabled']}")
    log_success("✅ Configuration is properly set!")

def main():
    # Welcome message
    print_banner()
    log_info("🎈 Booting up OppoCode Automation Engine...")
    log_success("🚀 BOOM! Business Automation is ready!")
    
    # Main loop
    while True:
        print_menu()
        choice = input("\n🧠 Enter your choice (1-6 or q): ").strip().lower()
        
        if choice == 'q':
            log_info("👋 Thank you for using OppoCode Automation!")
            log_success("🎉 Your business is now more automated than ever!")
            break
        elif choice == '1':
            run_task_scheduler()
        elif choice == '2':
            run_commerce_engine()
        elif choice == '3':
            run_customer_module()
        elif choice == '4':
            run_analytics_dashboard()
        elif choice == '5':
            run_full_suite()
        elif choice == '6':
            check_config()
        else:
            log_warning("⚠️  Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🛑 Graceful shutdown initiated...")
        log_info("👋 Hope you achieved BOOM business results!")
    except Exception as e:
        log_error(f"💥 Unhandled exception: {str(e)}")
        print("\n🔧 Please check install scripts or contact OppoCode support.")