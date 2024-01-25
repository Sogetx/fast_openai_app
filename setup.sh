#!/bin/bash

# Step 1: Clone the repository
REPO_DIR="fast_openai_app"

# сheck the repo exists
if [ -d "$REPO_DIR" ]; then
    echo "The repo was cloned..."
    cd "$REPO_DIR"
else
    # cloning
    echo "Cloning repo...."
    git clone https://github.com/Sogetx/fast_openai_app.git
    cd "$REPO_DIR"
fi


# Step 2: Setup your venv
python -m venv venv
source "$(pwd)/venv/Scripts/activate"  

# Step 3: Download libs
cd app
pip install -r requirements.txt
read -p "Change the openai_key and then press enter...."

uvicorn main:app --reload    
read -p "When finish press Enter...."