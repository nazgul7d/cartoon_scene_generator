# Importing necessary libraries and modules
import json
from openai import OpenAI

# API key for OpenAI GPT-3.5-turbo
TEST_OPENAI_API_KEY = "PUT YOUR KEY HERE"
# System prompt to set the context for the conversation
SYSTEM_PROMPT = "You are a great cartoon scene writer."

# Function to get a response from the language model
def get_llm_response(user_prompt):
    # Creating an OpenAI client with the provided API key
    client = OpenAI(
        api_key=TEST_OPENAI_API_KEY,
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.05,
        frequency_penalty=0.05
    )
    return completion.choices[0].message.content

# Function to generate the first scene based on a prompt and universe details
def generate_first_scene(prompt,universe):
    # Creating a super prompt that guides the user in scene creation
    super_prompt = f"""Your task is to create a scene based on the content provided below \
    delimited by triple backticks. 

    ```
    {universe}
    ```
    
    When creating a scene, make sure to use any subset of characters from that content. Make sure \
    that the scene is happening in one of the locations from the content above. Make sure the characters \
    only express emotions from the content above. The theme is also provided by: `{prompt}`.

    Generate the output in a JSON format with a "location" as a key for the location of the scene, \
    "characters" as the key for the list of characters in the scene and "dialogue" as an object \
    which contains "speaker" as a key for the speaking character, "text" as a the key for character's words \
    and "emotion" as the key for the emotion the character is feeling at that time. "dialogue" should be between \
    4 to 6 entries long.
    """

    # Getting the language model's response based on the super prompt
    output = get_llm_response(super_prompt)
    print("======== SCENE #1 ==========")
    print(output)
    return output

# Function to generate additional scenes based on the previous scene
def generate_additional_scenes(prev_scene, universe, num_scenes):

    scenes = []
    while num_scenes > 0:
        # Creating a prompt for generating the next scene
        prompt = f"""Your task is to create the next scene of a story based on the previous scene, \
        which is delimited by triple quotes below:

        \"\"\"
        {prev_scene}
        \"\"\"

        You are also provided the content below, delimited by triple backticks which provides you with the options \
        to choose characters, locations, and emotions from.

        ```
        {universe}
        ```

        Make the story cohesive and entertaining and the scene is happening in a different location. \
        Generate the output in the same JSON format as the previous scene. \
        Do not repeat the lines said by the characters in the previous scene. \
        Limit the "dialogue" length to maximum of 10 entries.
    """
        # Getting the language model's response based on the prompt
        output = get_llm_response(prompt)
        scenes.append(output)
        print(f"========= FOLLOWING SCENES ==========")
        print(output)
        prev_scene = output
        num_scenes -=1 
    return scenes

# Function to generate a movie script with multiple scenes
def generate_movie_script(prompt, universe, num_scenes):
    all_scenes = []
    all_converted_scenes = []

    # Generating the first scene
    first_scene = generate_first_scene(prompt,universe)
    # Generating additional scenes based on the first scene
    other_scenes = generate_additional_scenes(first_scene,universe,num_scenes)
    all_scenes = [first_scene]
    all_scenes.extend(other_scenes)

    # Converting the scenes to JSON format
    for scene in all_scenes:
        converted_scene = json.loads(scene)
        all_converted_scenes.append(converted_scene)
    
    return {"scenes": all_converted_scenes}

# Main function to execute the script generation
if __name__ == "__main__":
    prompt = "Hanging around looking for something to do"

    universe = {
        "characters": {
            "Alice": "7 years old girl, very curious",
            "Jack": "Alice's brother, 10 years old, likes to play with his friends",
            "Bob": "Alice's father, a programmer",
            "Mary": "Alice's mother, a teacher",
        },
        "locations": {
            "reception": "a big room in Alice's house with a big table, TV and a fireplace",
            "kitchen": "a cosy kitchen in Alice's house",
            "hall": "a long hall in Alice's house",
            "park": "a park near Alice's house",
        },
        "emotions": ["happy", "sad", "angry", "surprised", "scared"],
    }

    # Generating the complete movie script with 4 scenes
    generated_script = generate_movie_script(prompt, universe, 4)
    print(generated_script)
   


