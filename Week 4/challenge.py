def modify_file_content():
    filename = input("Enter the filename to read: ")
    
    try:
        # Step 1: Open and read the content of the file
        with open(filename, 'r') as file:  # 'r' is for read mode
            content = file.read()  # Read the entire content of the file
            print("Original content:", content)  # Display the original content
        
        # Step 2: Modify the content
        modified_content = content.upper()  # Convert the content to uppercase

        # Step 3: Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:  # 'w' is for write mode
            new_file.write(modified_content)  # Write the modified content to the new file
        
        print(f"Modified content has been saved to {new_filename}")
    
    # Step 4: Error handling
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: There was an issue reading or writing the file.")

# Call the function to execute the file modification process
modify_file_content()
