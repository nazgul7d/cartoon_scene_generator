# 🎥 cartoon_scene_generator
This script utilizes OpenAI's GPT-3.5-turbo language model to generate a movie script based on user prompts and a predefined universe. 
It creates a cohesive and entertaining narrative with multiple scenes, characters, and emotions.

## Getting Started

To use this script, you'll need an API key from OpenAI. Replace `PUT YOUR KEY HERE` in the code with your actual OpenAI API key.

```python
# API key for OpenAI GPT-3.5-turbo
TEST_OPENAI_API_KEY = "PUT YOUR KEY HERE"
```

Prerequisites
OpenAI API key
Python environment with necessary libraries (see requirements.txt)

## Functions
generate_first_scene(prompt, universe)
Generates the first scene based on the given prompt and universe details. Returns the scene in JSON format.

generate_additional_scenes(prev_scene, universe, num_scenes)
Generates additional scenes based on the previous scene, ensuring coherence and entertainment. Returns a list of scenes in JSON format.

generate_movie_script(prompt, universe, num_scenes)
Generates a complete movie script with multiple scenes. Returns a dictionary containing all scenes in JSON format.

## Example
prompt = "Hanging around looking for something to do"

universe = {
    # ... (characters, locations, emotions)
}

generated_script = generate_movie_script(prompt, universe, 4)
print(generated_script)

