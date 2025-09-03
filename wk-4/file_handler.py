def process_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

        modified_content = content.upper()

        with open("output.txt", 'w') as file:
            file.write(modified_content)

        print("✅ File processed successfully! Output written to 'output.txt'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: Permission denied when trying to read the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function
process_file()
