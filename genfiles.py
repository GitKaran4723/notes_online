# List of file names
file_names = [
      "Introduction to WTO",
      "Objectives of WTO",
      "Structure of WTO",
      "Principles of WTO",
      "Agreements under WTO",
      "WTO Dispute Settlement Mechanism",
      "WTO and Developing Countries",
      "Doha Development Round",
      "Recent Developments in WTO",
      "Criticism of WTO",
      "India and WTO",
      "Future of WTO"
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
