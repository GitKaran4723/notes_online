import os

file_names = [
      "Introduction to the World Bank",
      "Structure and Organization of the World Bank",
      "Functions and Role of the World Bank",
      "World Bank's Projects and Initiatives",
      "Criticism and Challenges Facing the World Bank"
    ]

# Define the folder path using a raw string to avoid escaping issues
folder = r"C:\Users\KARAN JADHAV\Desktop\UPSC_notes\International_Relations\notes\Global Institutions\World Bank"

# Loop through each name and create a file with the .md extension
for name in file_names:
    # Join the folder path and file name with .md extension
    file_name = os.path.join(folder, f"{name}.md")
    
    # Create and open the file in write mode
    with open(file_name, 'w') as file:
        # Write the title in markdown format
        file.write(f"# {name}\n\n")

print("Files created successfully.")
