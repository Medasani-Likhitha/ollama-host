import traceback



import ollama


def chat_completion(model: str, messages: list[dict]):
    try:
        response = ollama.chat(
            model=model,
            messages=messages)

        answer = response['message']['content']
    except ollama.ResponseError as e:
        print('Error:', e.error)
        if e.status_code == 404:
            print("pulling the model")
            ollama.pull(model)
    except Exception as e:
        traceback.print_exc()
        return None
    else:
        return {"answer": answer}


if __name__ == "__main__":
    model = 'llama3'
    messages = [
        {
            'role': 'user',
            'content': 'Why is the sky blue?',
        },
    ]
    print(chat_completion(model,messages))
