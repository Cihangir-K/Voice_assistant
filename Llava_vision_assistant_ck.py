import ollama
import tkinter as tk
from tkinter import filedialog
from PIL import Image as img


def generate(model, image, prompt):
    stream = ollama.generate(
        model=model,
        prompt=prompt,
        images=[image],
        stream=True
        # stream=False
    )
    response = ""
    # print(stream)
    for chunk in stream:
        response += chunk['response']
        print(chunk['response'], end='', flush=True)
    print("")

    # full_response=response
    # print("full_response: ",full_response)
    return response
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

image = file_path
# prompt = "Create a caption for this image"
# prompt = "What is in this picture?"
# prompt = "Describe this picture"
# prompt = "What is the text in this image?"
prompt=input("Please ask: ")

# Open an image file
image_to_open = img.open(file_path)



for model in ['llava']:
  print(f"Model: {model}")
  generate(model, image, prompt)


# Display the image
image_to_open.show()