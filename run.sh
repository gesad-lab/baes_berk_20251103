#!/bin/bash
set -e

# Check if setup was run
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Run ./setup.sh first!"
    exit 1
fi

if [ ! -f ".env" ]; then
    echo "❌ .env file not found. Run ./setup.sh first!"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Load environment variables
set -a
source .env
set +a

# Verify API keys are set
MISSING_KEYS=false
if [ -z "${OPENAI_API_KEY_BAES}" ]; then
    echo "⚠️  Missing: OPENAI_API_KEY_BAES"
    MISSING_KEYS=true
fi
if [ -z "${OPENAI_API_KEY_CHATDEV}" ]; then
    echo "⚠️  Missing: OPENAI_API_KEY_CHATDEV"
    MISSING_KEYS=true
fi
if [ -z "${OPENAI_API_KEY_GHSPEC}" ]; then
    echo "⚠️  Missing: OPENAI_API_KEY_GHSPEC"
    MISSING_KEYS=true
fi

if [ "$MISSING_KEYS" = true ]; then
    echo ""
    echo "❌ Please set all required API keys in .env file"
    echo "   Edit with: nano .env"
    exit 1
fi

echo "========================================="
echo "Running experiment: baes_benchmarking_20251028_0713"
echo "========================================="
echo ""
echo "Configuration:"
echo "  Model: gpt-4o-mini"
echo "  Frameworks: baes, chatdev, ghspec"
echo "  Max runs per framework: 100"
echo ""
echo "This may take a while..."
echo ""

# Run experiment
python -m src.main

EXIT_CODE=$?

echo ""
echo "========================================="
if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ Experiment completed successfully!"
else
    echo "❌ Experiment failed with exit code: $EXIT_CODE"
fi
echo "========================================="
echo ""
echo "Results saved to: ./runs/"
echo ""
echo "Next steps:"
echo "  - View run outputs: ls -la runs/"
echo "  - Generate analysis: python -m src.analysis.report_generator"
echo ""

exit $EXIT_CODE
