import os
# Path to the folder containing your .cpp and .h files
folder_path = 'c:/temp/arduino/compass_belt_BNO085_Adafruit_BNO08x_library/'
# Output file where all contents will be combined
output_file = 'combined_output.txt'
# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        # Consider only .cpp and .h files
        if filename.endswith('.cpp') or filename.endswith('.h') or filename.endswith('.ino'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as infile:
                # Write the contents of the current file to the output file
                outfile.write(f'// Content from {filename}\n')
                outfile.write(infile.read())
                outfile.write('\n\n')
print(f"Files combined into {output_file}")
