import os

file_names = [
    "Introduction to G20",
    "Objectives of G20",
    "Structure of G20",
    "Functions and Role of G20",
    "Summits and Key Outcomes",
    "G20’s Role in Global Economic Governance",
    "G20 and Developing Countries",
    "G20 and Climate Change",
    "G20 and Global Health",
    "G20 and Digital Economy",
    "G20 and Trade",
    "G20 and Global Taxation",
    "Criticism and Challenges Facing G20",
    "India’s Role in the G20",
    "Future of the G20"
]

# Define the folder path using a raw string to avoid escaping issues
folder = r"C:\Users\KARAN JADHAV\Desktop\UPSC_notes\International_Relations\notes\Multilateral Relations\G20"

# Loop through each name and create a file with the .md extension
for name in file_names:
    # Join the folder path and file name with .md extension
    file_name = os.path.join(folder, f"{name}.md")
    
    # Create and open the file in write mode
    with open(file_name, 'w') as file:
        # Write the title in markdown format
        file.write(f"# {name}\n\n")

print("Files created successfully.")
