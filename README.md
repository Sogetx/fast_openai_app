# FastAPI OpenAI App

This is a FastAPI project that integrates with the OpenAI GPT-3.5 Turbo model for text-based consultations.

## Setup
1. **Shortcut** (you can skip 2-4 steps)
   
   Download setup.sh and then enter in cmd:
   ```bash
    ./setup.sh
2. **Clone the repository:**

   ```bash
   git clone https://github.com/Sogetx/fast_openai_app.git
   cd your_project
3. **Setup your venv**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
4. **Download libs**
   ```bash
   cd your_project\app
   pip install -r requirements.txt
5. **Setup your OpenAI API key:**
   Open the `app/utils.py` file and find the line:

   ```python
   openai.api_key = "your Open AI key"
6. **Run your app**
   ```bash
   uvicorn main:app --reload
7. **Enter your prompt**
Tap [here](http://127.0.0.1:8000/docs#/default/consult_endpoint_consult_post) and then enter in consult Request body something like this:
![image](https://github.com/Sogetx/fast_openai_app/assets/78159992/53d58fcc-41da-4bb8-b179-047f54b7f357)
8. **Check Respons**
Wait a minute after previous step and then recive you will recive answer like here:
![image](https://github.com/Sogetx/fast_openai_app/assets/78159992/790aade4-2952-4c4d-976b-a9a4dc394ab1)
![image](https://github.com/Sogetx/fast_openai_app/assets/78159992/750c003b-54dd-43cf-bfe2-a44aa54aaa44)

