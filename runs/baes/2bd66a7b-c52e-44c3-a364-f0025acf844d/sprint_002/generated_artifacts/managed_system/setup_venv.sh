#!/bin/bash
# Auto-generated virtual environment setup script

echo "🔧 Setting up virtual environment for Managed System..."

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

echo "✅ Virtual environment setup complete!"
echo "To activate: source venv/bin/activate"
