from flask import Flask, request, jsonify, render_template
from llm_loader import load_model_and_tokenizer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 

fine_tuned_model, tokenizer = load_model_and_tokenizer()

def data_transformation(user_query,tokenizer):
    system_prompt = """You are a specialized assistant for Upflairs,
    dedicated to answering queries related strictly to Python programming.
    Upflairs offers courses in Data Science, Machine Learning, DevOps,
    Full Stack Development, IoT, and System Embedding,
    all focused on Python.\n\nFor any Python-related question, respond with clear,
    accurate explanations, code snippets, or examples as needed.\n\nHowever,
    if a question involves any programming language other than Python (like Java, C++, or others),
    reply with this message:'I am here to assist with Python-related programming questions only.
    For inquiries about other programming languages, please consult other resources.
    Your response should always focus on Python and topics covered by Upflairs."""
    messages = [
    {"role":"system","content":system_prompt},
    {"role": "user", "content": user_query}]

    inputs = tokenizer.apply_chat_template(messages,
                                            tokenize = True,
                                            add_generation_prompt = True,
                                            return_tensors = "pt").to("cuda")
    return  inputs
def llama_response(inputs,LLM):
    outputs = model.generate(input_ids = inputs, max_new_tokens = 64, use_cache = True,
                         temperature = 1, min_p = 0.1) 
    response = tokenizer.batch_decode(outputs)
    response = response[0].split('\n')[-1] # filterig the response
    return response

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form.get('user_message', '')

    if not user_message.strip():
        return "I didn't catch that. Could you rephrase it?"

    if "hello" in user_message.lower():
        bot_response = "Hello! How can I assist you today?"
    elif "how are you" in user_message.lower():
        bot_response = "I'm just a bot, but I'm functioning perfectly! How about you?"
    elif "bye" in user_message.lower():
        bot_response = "Goodbye! Have a great day!"
    else:
        input_query  = data_transformation(user_query=user_message.lower(),tokenizer=tokenizer)
        bot_response = llama_response(inputs=input_query,LLM=fine_tuned_model) # passing message to the llama

    return bot_response

if __name__ == '__main__':
    app.run(debug=True)
