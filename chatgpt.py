import openai


openai.api_key = "Api key is given in #readme.md"


while True:
    
    model_engine = "text-davinci-003"
    
    command = input('Enter your question: ')

    if 'exit' in command or 'quit' in command:
        break

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=command,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    
    coders = completion.choices[0].text
    
    
    print(coders)
