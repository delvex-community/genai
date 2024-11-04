import subprocess

def run_ollama_model(model_name, prompt):
    try:
        # Run the Ollama model with the given prompt
        result = subprocess.run(
            ["ollama", "run", model_name, "--prompt", prompt],
            capture_output=True,
            text=True,
            check=True
        )
        # Capture and return the output
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

# Example usage
model_name = "llama2"  # Replace with the model you have downloaded
prompt = "Hello, how are you?"
output = run_ollama_model(model_name, prompt)
print(output)
