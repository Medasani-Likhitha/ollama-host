import traceback
import ollama
from app.Logger import log_message

model_list = [models["name"].split(":")[0] for models in ollama.list().get("models")]


def chat_completion(model: str, messages: list[dict]):
    try:
        if model not in model_list:
            ollama.pull(model)
        response = ollama.chat(
            model=model,
            messages=messages)

        answer = response['message']['content']
        log_message("Ollama model response", model=model, question=messages[0].get('content', ''), response=answer)
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
    print(chat_completion(model, messages))
