def create_fortran_file(filename, content):
    """
    Creates a .f file with the given filename and content.

    Args:
        filename (str): The name of the .f file to create (e.g., "my_program.f").
        content (str): The content to write into the file.
    """
    try:
        with open(filename, "w") as file:
            file.write(content)
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
fortran_code = """
      program hello
      print *, "Hello, Fortran World!"
      end program hello
"""
create_fortran_file("hello.f", fortran_code)