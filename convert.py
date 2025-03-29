import re
from string import Template 
def findexponential(table_text):
    energy_values = re.findall(r"\s+([-+]?\d+\.\d+E[+-]\d+)\s+[EOB][+-]?\s+\w+", table_text)
    energy_tuple = tuple(energy_values)
    return energy_tuple

def extract_matrix_values(lines):
    """Extract values from lines containing 'A( ... )=' """
    pattern = r"A\(\s*\d+\s+\d+\s*\)\s*=\s*([-+]?\d+\.\d+)"  # Match A( x y )= value
    values = re.findall(pattern, "\n".join(lines))  # Extract only the values
    formatted_values = tuple(f"{float(value):.6E}".replace("E+00", "E0").replace("E-00", "E0") for value in values)
    return formatted_values

out_file = input("Enter .out filename - ")

with open(out_file, "r", encoding="utf-8") as file:
     out_content = file.readlines()
    
#Finding AXX, BYY, CZZ
rot_constants_pattern = r"AXX=\s*([\d.E+-]+)\s*BYY=\s*([\d.E+-]+)\s*CZZ=\s*([\d.E+-]+)"
#Assigning to a tuple
rot_constants_match = re.search(rot_constants_pattern, "".join(out_content))

#Tuple to constants
if rot_constants_match:
    a_const, b_const, c_const = rot_constants_match.groups()

part1_evals = findexponential("\n".join(out_content[25:35]))
part2_evals = findexponential("\n".join(out_content[37:58]))
part3_evals = findexponential("\n".join(out_content[57:91]))
part4_evals = findexponential("\n".join(out_content[92:144]))
part5_evals = findexponential("\n".join(out_content[145:219]))
    
part1_matvals = extract_matrix_values("\n".join(out_content[25:35]))
part2_matvals = extract_matrix_values("\n".join(out_content[37:58]))
part3_matvals = extract_matrix_values("\n".join(out_content[57:91]))
part4_matvals = extract_matrix_values("\n".join(out_content[92:144]))
part5_matvals = extract_matrix_values("\n".join(out_content[145:219]))


    
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




