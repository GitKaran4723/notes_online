import os

file_names = [
    "Objectives and Structure of NATO",
    "NATO's Role in Collective Defense and Security",
    "NATO's Response to Global Terrorism and Emerging Threats",
    "NATO's Involvement in Peacekeeping and Humanitarian Missions",
    "Challenges and Future Prospects of NATO in Global Security"
]

# Define the folder path using a raw string to avoid escaping issues
folder = r"C:\Users\KARAN JADHAV\Desktop\UPSC_notes\International_Relations\notes\Multilateral Relations\NATO"
# Loop through each name and create a file with the .md extension
for name in file_names:
    # Join the folder path and file name with .md extension
    file_name = os.path.join(folder, f"{name}.md")
    
    # Create and open the file in write mode
    with open(file_name, 'w') as file:
        # Write the title in markdown format
        file.write(f"# {name}\n\n")

print("Files created successfully.")
