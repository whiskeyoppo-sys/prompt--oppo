#!/bin/bash

# OppoCode Setup Script for Termux
# Copyright (c) OppoCode 2024

clear
echo "
╔════════════════════════════════════════════════════════════════════════╗
║                    O P P O C O D E   S E T U P                         ║
║                        Business Automation Platform                    ║
╚════════════════════════════════════════════════════════════════════════╝
"

# Check Termux environment
if [[ ! "$TERMUX_VERSION" ]]; then
    echo "❌ This script is designed for Termux only (Android) environment!"
    echo "   Please install Termux from F-Droid or Google Play first."
    exit 1
fi

# Create project directory
echo "📁 Creating project structure..."
mkdir -p oppocode_automation_platform/{modules,utils,data}

# Create requirements file
EDFcat > oppocode_automation_platform/requirements.txt << 'EOF'
# Python requirements for OppoCode Automation Platform
# All packages already built-in to Termux Python
# Only packages that need explicit installation:
# (None required for basic functionality)
