import os

file_names = [
    "Border Disputes and the Line of Actual Control (LAC)",
    "Economic and Trade Relations",
    "Geopolitical Rivalry in South Asia and Indo-Pacific",
    "China’s Belt and Road Initiative (BRI) and India's Response",
    "Military and Strategic Cooperation and Competition"
]

# Define the folder path using a raw string to avoid escaping issues
folder = r"C:\Users\KARAN JADHAV\Desktop\UPSC_notes\International_Relations\notes\India and Neighbourhood\Indo–China Relations"
# Loop through each name and create a file with the .md extension
for name in file_names:
    # Join the folder path and file name with .md extension
    file_name = os.path.join(folder, f"{name}.md")
    
    # Create and open the file in write mode
    with open(file_name, 'w') as file:
        # Write the title in markdown format
        file.write(f"# {name}\n\n")

print("Files created successfully.")
