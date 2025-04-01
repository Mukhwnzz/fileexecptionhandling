def process_file():
    """Read a file, modify its content, and write to a new file with error handling"""
    try:
        # Get input filename from user
        input_filename = input("Enter the name of the file to read: ")
        
        # Read the file
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (convert to uppercase in this example)
        modified_content = content.upper()
        
        # Get output filename from user
        output_filename = input("Enter the name of the new file to create: ")
        
        # Write the modified content to new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Success! Modified content written to {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read/write files.")
    except IsADirectoryError:
        print(f"Error: '{input_filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print("Error: Could not decode the file (might be a binary file).")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Run the program
if __name__ == "__main__":
    process_file()