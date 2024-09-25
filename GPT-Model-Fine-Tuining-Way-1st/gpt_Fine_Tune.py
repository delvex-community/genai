import openai
import json

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Load your training dataset
with open('your_dataset.json', 'r') as file:
    training_data = json.load(file)

# Prepare the fine-tuning dataset
fine_tuning_data = []

for example in training_data:
    for message in example['messages']:
        role = message['role']
        content = message['content']
        fine_tuning_data.append({
            "role": role,
            "content": content
        })

