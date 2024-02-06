import random

def generate_text(prompt):
    responses = ["This is a simple response.", "Another generated text.", "A different response here."]
    return f"{prompt} {random.choice(responses)}"

while True:
    user_input = input("Enter a prompt (or 'exit' to end): ")
    
    if user_input.lower() == 'exit':
        print("Exiting.")
        break
    
    generated_text = generate_text(user_input)
    print("Generated Text:", generated_text)
