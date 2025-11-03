#!/bin/bash
set -e

echo "========================================="
echo "Setting up experiment: baes_benchmarking_20251028_0713"
echo "========================================="
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 not found"
    echo "Please install Python 3.9 or higher"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo "✓ Python version: $PYTHON_VERSION"

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt --quiet

echo "✓ Dependencies installed"

# Setup environment file
echo ""
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✅ Created .env file"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your OpenAI API keys!"
    echo ""
    echo "   Required keys for enabled frameworks:"
    echo "   - OPENAI_API_KEY_BAES"
    echo "   - OPENAI_API_KEY_CHATDEV"
    echo "   - OPENAI_API_KEY_GHSPEC"
    echo ""
    echo "   Edit with: nano .env  (or your preferred editor)"
else
    echo "✅ .env file already exists"
fi

# Clone framework repositories
echo ""
python -m src.setup_frameworks

echo ""
echo "========================================="
echo "✅ Setup complete!"
echo "========================================="
echo ""
echo "Next steps:"
echo "  1. Edit .env and add your API keys: nano .env"
echo "  2. Run experiment: ./run.sh"
echo ""
