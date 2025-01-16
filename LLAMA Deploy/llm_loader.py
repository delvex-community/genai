from unsloth import FastLanguageModel

# Function to load the locally saved LLaMA model and tokenizer
def load_model_and_tokenizer(model_name, max_seq_length, dtype, load_in_4bit):
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=model_name,  
        max_seq_length=max_seq_length,
        dtype=dtype,
        load_in_4bit=load_in_4bit,
    )
    FastLanguageModel.for_inference(model)  # Enable faster inference
    return model, tokenizer

# Load the model and tokenizer at the start of the Flask app
model_name = "LLAMA_Fine-Tuned-Model"  
max_seq_length = 2048  
dtype = None 
load_in_4bit = True  

model, tokenizer = load_model_and_tokenizer(model_name, max_seq_length, dtype, load_in_4bit)


