#!/bin/bash
# Auto-generated server startup script

echo "🚀 Starting BAE Managed System servers..."

# Use the current Python environment (no virtual environment activation)
# This ensures we use the same dependencies as the main project

# Start FastAPI server in background
echo "Starting FastAPI server at http://127.0.0.1:8100"
python -m uvicorn app.main:app --host 127.0.0.1 --port 8100 --reload &
API_PID=$!

# Wait a moment for API to start
sleep 2

# Start Streamlit UI
echo "Starting Streamlit UI at http://127.0.0.1:8600"
python -m streamlit run ui/app.py --server.port 8600 &
UI_PID=$!

echo "✅ Both servers started!"
echo "API PID: $API_PID"
echo "UI PID: $UI_PID"

# Keep script running to maintain processes
wait
