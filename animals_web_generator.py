import json
def load_data(file_path):
  """ Loads the JSON file """
  with open(file_path, "r") as file:
    return json.load(file)

def print_animal_details(animals_data):
  """ Iterates through animals and prints their details."""
  for animal in animals_data:
    if "name" in animal:
      print(f"Name: {animal['name']}")
    if "characteristics" in animal:
      characteristics = animal["characteristics"]
      if "diet" in characteristics:
        print(f"Diet: {characteristics['diet']}")
    if "locations" in animal and animal["locations"]:
      print(f"Location: {animal['locations'][0]}")
      if "type" in characteristics:
        print(f"Type: {characteristics['type']}")
    print() #Blank Line between entries

animals_data = load_data("animals_data.json")
print_animal_details(animals_data)

def generate_animal_info(animals_data):
  """Generates a string with the animals' details."""
  output = '' # Define an empty string
  for animal in animals_data:
    output += '<li class="cards__item"><br/>\n'
    if "name" in animal:
      output += f"Name: {animal['name']}<br/>\n"
    if "characteristics" in animal:
      characteristics = animal["characteristics"]
      if "diet" in characteristics:
        output += f"Diet: {characteristics['diet']}<br/>\n"
    if "locations" in animal and animal["locations"]:
      output += f"Location: {animal['locations'][0]}<br/>\n"
      if "type" in characteristics:
        output += f"Type: {characteristics['type']}<br/>\n"
    output += '</li>\n' # Add a blank line between animals
  return output

def generate_html(template_path, output_path, animal_info):
  """ Replaces the placeholder in the template with the animal data and writes it to a new file."""
  with open(template_path, "r") as file:
    template_content = file.read()
  # Replace placeholder with generated animal information
  new_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animal_info)

  # Write the new content to the output file
  with open(output_path, "w") as file:
    file.write(new_content)

animals_data = load_data("animals_data.json")

animal_info = generate_animal_info(animals_data)

generate_html("animals_template.html", "animals.html", animal_info)

print("HTML file generated suceesfully as 'animals.html'.")