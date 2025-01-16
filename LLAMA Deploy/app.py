from flask import Flask, request, jsonify, render_template
from llm_loader import load_model_and_tokenizer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 

model, tokenizer = load_model_and_tokenizer()

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
    pass 

@app.route('/get_response', methods=['POST'])
def get_response():
    # Get the user message from the request
    user_message = request.form.get('user_message', '')

    # Basic logic to generate a chatbot response
    if not user_message.strip():
        return "I didn't catch that. Could you rephrase it?"

    # Example: simple keyword-based responses
    if "hello" in user_message.lower():
        bot_response = "Hello! How can I assist you today?"
    elif "how are you" in user_message.lower():
        bot_response = "I'm just a bot, but I'm functioning perfectly! How about you?"
    elif "bye" in user_message.lower():
        bot_response = "Goodbye! Have a great day!"
    else:
        input_query  = data_transformation(user_query=user_message.lower(),tokenizer=tokenizer)
        bot_response = llama_response(inputs=input_query,LLM=None) # passing message to the llama

    return bot_response

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
