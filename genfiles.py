# List of file names
file_names = [
    "Historical Perspective",
    "Shared Values",
    "People-to-People Ties",
    "Strategic Ties",
    "Defence Cooperation",
    "Joint Military Exercises",
    "China Factor",
    "Multilateral Cooperation",
    "Economic Cooperation",
    "Supply Chain Resilience Initiative (SCRI)",
    "Bilateral Trade",
    "Cooperation in the Education Sector",
    "Cooperation on Clean Energy",
    "Adani Coal Mine Controversy",
    "Visa Issues",
    "Violence with Indian Diaspora"
]

# Loop through each name and create a file with the .md extension
for name in file_names:
    # File name with spaces and .md extension
    file_name = f"{name}.md"
    
    # Create and open the file in write mode
    with open(file_name, 'w') as file:
        # You can optionally write something in the file here
        file.write(f"# {name}\n\n")

print("Files created successfully.")
