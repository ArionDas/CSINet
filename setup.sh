#!/bin/sh

# Function to create virtual environment
create_venv() {
    if command -v python3 &> /dev/null; then
        python3 -m venv .venv
    elif command -v python &> /dev/null; then
        python -m venv .venv
    else
        echo "Python is not installed. Please install Python and try again."
        exit 1
    fi
}

# Create virtual environment
create_venv

# Function to activate virtual environment
activate_venv() {
    if [ -f ".venv/bin/activate" ]; then
        . .venv/bin/activate
    else
        echo "Virtual environment not found. Please check the previous steps."
        exit 1
    fi
}

# Activate virtual environment
activate_venv

# Install dependencies
if ! pip install -r requirements.txt; then
    echo "Failed to install dependencies."
    exit 1
fi

# Check GPU
if ! pytest -m gpu; then
    echo "Failed to run GPU tests."
    exit 1
fi

echo "Setup completed successfully."
