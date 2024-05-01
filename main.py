import requests

# Fetch data from the API
response = requests.get("https://rickandmortyapi.com/api/character/?page=7")
data = response.json()

# Extract character information
characters = [(char['name'], char['image'], char['status']) for char in data['results']]

# Generate HTML with CSS
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rick and Morty Characters</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }
        li {
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            margin: 10px;
            padding: 20px;
            text-align: center;
            width: 200px;
        }
        li img {
            max-width: 100%;
            height: auto;
            border-radius: 5px;
        }
        strong {
            color: #555;
        }
    </style>
</head>
<body>
    <h1>List of Rick and Morty Characters</h1>
    <ul>
"""
for character in characters:
    name, image, status = character
    html_content += f"""        <li>
            <img src="{image}" alt="{name}">
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Status:</strong> {status}</p>
        </li>\n"""

html_content += """
    </ul>
</body>
</html>
"""

# Write HTML content to a file
with open("rick_and_morty.html", "w") as file:
    file.write(html_content)

print("HTML file created successfully.")
