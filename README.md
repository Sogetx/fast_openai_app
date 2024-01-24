# FastAPI OpenAI App

This is a FastAPI project that integrates with the OpenAI GPT-3.5 Turbo model for text-based consultations.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Sogetx/fast_openai_app.git
   cd your_project
2. **Setup your venv**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
3. **Download libs**
   ```bash
   cd your_project\app
   pip install -r requirements.txt
4. **Setup your key**
   
   change openai.api_key="your Open AI key" 
6. **Run your app**
   ```bash
   uvicorn main:app --reload
   Tap [here](http://127.0.0.1:8000/docs#/default/consult_endpoint_consult_post)
