import gradio as gr
import google.generativeai as genai
import PIL.Image

# Predefined prompt text
predefined_prompt = """
A Prompt is a short text phrase that the Midjourney Bot interprets to produce an image. The Midjourney Bot breaks down the words and phrases in a prompt into smaller pieces, called tokens, that can be compared to its training data and then used to generate an image. A well-crafted prompt can help make unique and exciting images.

Prompts can be very simple. Single words (or even an emoji!) will produce an image. Very short prompts will rely heavily on Midjourney’s default style, so a more descriptive prompt is better for a unique look. However, super-long prompts aren’t always better. Concentrate on the main concepts you want to create.

The Midjourney Bot does not understand grammar, sentence structure, or words like humans. Word choice also matters. More specific synonyms work better in many circumstances. Instead of big, try gigantic, enormous, or immense. Remove words when possible. Fewer words mean each word has a more powerful influence. Use commas, brackets, and hyphens to help organize your thoughts, but know the Midjourney Bot will not reliably interpret them. The Midjourney Bot does not consider capitalization.

Midjourney Model Version 4 is slightly better than other models at interpreting traditional sentence structure.

It is better to describe what you want instead of what you don’t want. If you ask for a party with “no cake,” your image will probably include a cake. If you want to ensure an object is not in the final image, try advance prompting using the --no parameter.

Anything left unsaid may surprise you. Be as specific or vague as you want, but anything you leave out will be randomized. Being vague is a great way to get variety, but you may not get the specific details you want.

Subject: person, animal, character, location, object, etc.
Medium: photo, painting, illustration, sculpture, doodle, tapestry, etc.
Environment: indoors, outdoors, on the moon, in Narnia, underwater, the Emerald City, etc.
Lighting: soft, ambient, overcast, neon, studio lights, etc
Color: vibrant, muted, bright, monochromatic, colorful, black and white, pastel, etc.
Mood: Sedate, calm, raucous, energetic, etc.
Composition: Portrait, headshot, closeup, birds-eye view, etc.

Plural words leave a lot to chance. Try specific numbers. "Three cats" is more specific than "cats." Collective nouns also work, “flock of birds” instead of "birds.”

A product mockup is a model of what your final product will look like. Product mockups are frequently used to present a final product in a real-life context. You can use product mockups to get feedback on a product concept before mass production or in a presentation to administrators, stakeholders, or investors. 

** based on everything discussed above help me to write prompt to create exact same image that i am providing in the reference + also describe the information of the subject in detail in the prompt + also describe about the environment and shadows and lightning as they are very important in a mockup
"""


def generate_image(image):
    genai.configure(api_key='AIzaSyAGXl51WsKcEjIO5_x3Cwt5jFa0ByKR_30')
    model = genai.GenerativeModel('gemini-pro-vision')

    response = model.generate_content([predefined_prompt, image])

    return response.text


# Define the input component for the Gradio interface
image_input = gr.Image(label="Upload an image", type="pil")

# Create the Gradio interface
iface = gr.Interface(
    fn=generate_image,
    inputs=image_input,
    outputs=gr.Textbox(label="Generated Image"),
    title="Image Generation with Midjourney Bot",
    description="Generate an image based on a predefined prompt and an uploaded image."
)

# Launch the Gradio interface
iface.launch()