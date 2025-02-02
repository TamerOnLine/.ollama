import ollama

def generate_text(prompt):
    response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

if __name__ == "__main__":
    print("Ollama Chatbot is running. Type 'exit' to quit.")
    
    while True:
        user_input = input("\nEnter a prompt: ")
        
        if user_input.lower() == "exit":
            print("Exiting Ollama Chatbot. Goodbye!")
            break
        
        output = generate_text(user_input)
        print("\nGenerated Text:\n", output)
