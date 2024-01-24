import openai


openai.api_key = "your key" #!!!!! Input your OpenAI API key here
def generate_response(input):
    messages = [
        {"role": "user",
         "content": """As a consultant answer my questions in very deep details' \n"""},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    ) 
    # reply = completion.choices[0].message.content
    reply = completion.choices[0].message.content
    return reply