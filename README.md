# FastAPI OpenAI App

This is a FastAPI project that integrates with the OpenAI GPT-3.5 Turbo model for text-based consultations.

## Setup Short
1. **Download project**
   
   You may download only setup.sh or all project and then click on setup.sh, or enter in cmd:
   ```bash
    ./setup.sh
   ```
2. **Setup your OpenAI API key:**

   Open the `app/utils.py` file and find the line:

   ```python
   openai.api_key = "your Open AI key" ,
   ```
   
   After tap enter in console to launch application.
   If all is OK you will see this:
   ![image](https://github.com/Sogetx/fast_openai_app/assets/78159992/7a7337e4-e11f-49a4-9234-8a3bec06c454)
4. **Enter your prompt**
   
   Tap [here](http://127.0.0.1:8000/docs#/default/consult_endpoint_consult_post) and then enter in consult Request body something like this:
   ![image](https://github.com/Sogetx/fast_openai_app/assets/78159992/53d58fcc-41da-4bb8-b179-047f54b7f357)
5. **Check Respons**

   Wait a minute after previous step and then recive you will recive answer like here:
   ![image](https://github.com/Sogetx/fast_openai_app/assets/78159992/790aade4-2952-4c4d-976b-a9a4dc394ab1)
   ![image](https://github.com/Sogetx/fast_openai_app/assets/78159992/750c003b-54dd-43cf-bfe2-a44aa54aaa44)
## Alternative
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
4. **Setup your OpenAI API key:**
   Open the `app/utils.py` file and find the line:

   ```python
   openai.api_key = "your Open AI key"
5. **Run your app**
   ```bash
   uvicorn main:app --reload
6. **Enter your prompt**
Tap [here](http://127.0.0.1:8000/docs#/default/consult_endpoint_consult_post) and then enter in consult Request body something like this:
![image](https://github.com/Sogetx/fast_openai_app/assets/78159992/53d58fcc-41da-4bb8-b179-047f54b7f357)
7. **Check Respons**
Wait a minute after previous step and then recive you will recive answer like here:
![image](https://github.com/Sogetx/fast_openai_app/assets/78159992/790aade4-2952-4c4d-976b-a9a4dc394ab1)
![image](https://github.com/Sogetx/fast_openai_app/assets/78159992/750c003b-54dd-43cf-bfe2-a44aa54aaa44)

