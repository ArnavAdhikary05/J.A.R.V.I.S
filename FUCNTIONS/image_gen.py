import requests
import os

def img_gen(prompt, output_file):
    
    #API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5" #very fast but not stable
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0" #Good and stable but slow
    #API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-2-1-finetuned" #most recent

    #set the authorization token in the headers
    headers ={f"Authorization": f"Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content
    
    image_bytes = query({
        "inputs": prompt,
    })

    with open(output_file, "wb") as f:
        f.write(image_bytes)

if __name__ == "__main__":
    img_gen("A playful and adorable cat sitting gracefully on a cozy cushion, wearing a vibrant red hat with a wide brim and a stylish ribbon. The cat has soft, fluffy fur and bright, curious eyes, looking directly at the viewer with a mischievous charm. The background is softly lit, featuring warm tones that emphasize the cat’s expressive personality. The scene feels cozy, whimsical, and full of character, highlighting the cat’s unique style and endearing presence.","output_image.png")