import re

def findexponential(table_text):
    energy_values = re.findall(r"\s+([-+]?\d+\.\d+E[+-]\d+)\s+[EOB][+-]?\s+\w+", table_text)
    energy_tuple = tuple(energy_values)
    return energy_tuple

def extract_matrix_values(lines):
    """Extract values from lines containing 'A( ... )=' """
    pattern = r"A\(\s*\d+\s+\d+\s*\)\s*=\s*([-+]?\d+\.\d+)"  # Match A( x y )= value
    values = re.findall(pattern, "\n".join(lines))  # Extract only the values
    
    formatted_values = tuple(
        "0.0" if float(value) == 0.0 else 
        f"{float(value):.6E}".replace("E+00", "E0").replace("E-00", "E0")
        if abs(float(value)) >= 1.0 else f"{float(value):.6f}E0"
        for value in values
    )
    return formatted_values

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

out_file = input("Enter .out filename (with .out like: Pyridazine.out) - ")

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
    
part1_matvals = extract_matrix_values((out_content[25:35]))
part2_matvals = extract_matrix_values((out_content[37:58]))
part3_matvals = extract_matrix_values((out_content[57:91]))
part4_matvals = extract_matrix_values((out_content[92:144]))
part5_matvals = extract_matrix_values((out_content[145:219]))

text = f"""      SUBROUTINE ASYMTOP(j,itau,ntau,n,ac,eg)
      IMPLICIT REAL*4 (A-H, O-Z)
 
c
c     This subroutine has to be replaced with proper Ac and Eg values
c     for other C2v molecules.
c     These data are for the Pyridazine molecule with up to J=5(AXX= {a_const}  BYY= {b_const} CZZ= {c_const})
c     The energies eg(i) are in the units of eV.
c
      DIMENSION eg(11) , ac(11,6,2) , itau(11) , ntau(11)

      DO ii = 1 , 11
        DO jj = 1 , 6
          DO kk = 1 , 2
            ac(ii,jj,kk) = 0.0
          END DO
        END DO
      END DO

      n = j + j + 1
      DO i = 1 , n
        ip = i
        ntau(i) = ip
        itau(i) = i - j - 1
      END DO
      IF ( j.NE.0 ) THEN
        IF ( j.EQ.2 ) THEN
          eg(1) = {part2_evals[0]} 
          eg(2) = {part2_evals[1]} 
          eg(3) = {part2_evals[2]}
          eg(4) = {part2_evals[3]} 
          eg(5) = {part2_evals[4]}
          ac(1,1,1) = {part2_matvals[0]} 
          ac(1,1,2) = {part2_matvals[1]} 
          ac(1,3,1) = {part2_matvals[2]} 
          ac(1,3,2) = {part2_matvals[3]} 
          ac(2,2,1) = {part2_matvals[4]} 
          ac(2,2,2) = {part2_matvals[5]} 
          ac(3,3,1) = {part2_matvals[6]} 
          ac(3,3,2) = {part2_matvals[7]} 
          ac(4,2,1) = {part2_matvals[8]} 
          ac(4,2,2) = {part2_matvals[9]} 
          ac(5,1,1) = {part2_matvals[10]} 
          ac(5,1,2) = {part2_matvals[11]} 
          ac(5,3,1) = {part2_matvals[12]} 
          ac(5,3,2) = {part2_matvals[13]} 
          RETURN
        ELSE IF ( j.EQ.3 ) THEN
          eg(1) = {part3_evals[0]} 
          eg(2) = {part3_evals[1]}
          eg(3) = {part3_evals[2]}
          eg(4) = {part3_evals[3]}
          eg(5) = {part3_evals[4]}
          eg(6) = {part3_evals[5]}
          eg(7) = {part3_evals[6]}
          ac(1,2,1) = {part3_matvals[0]} 
          ac(1,2,2) = {part3_matvals[1]}
          ac(1,4,1) = {part3_matvals[2]}
          ac(1,4,2) = {part3_matvals[3]}
          ac(2,1,1) = {part3_matvals[4]}
          ac(2,1,2) = {part3_matvals[5]}
          ac(2,3,1) = {part3_matvals[6]}
          ac(2,3,2) = {part3_matvals[7]}
          ac(3,2,1) = {part3_matvals[8]}
          ac(3,2,2) = {part3_matvals[9]}
          ac(3,4,1) = {part3_matvals[10]}
          ac(3,4,2) = {part3_matvals[11]}
          ac(4,3,1) = {part3_matvals[12]}
          ac(4,3,2) = {part3_matvals[13]}
          ac(5,2,1) = {part3_matvals[14]}
          ac(5,2,2) = {part3_matvals[15]}
          ac(5,4,1) = {part3_matvals[16]}
          ac(5,4,2) = {part3_matvals[17]}
          ac(6,1,1) = {part3_matvals[18]}
          ac(6,1,2) = {part3_matvals[19]}
          ac(6,3,1) = {part3_matvals[20]}
          ac(6,3,2) = {part3_matvals[21]}
          ac(7,2,1) = {part3_matvals[22]}
          ac(7,2,2) = {part3_matvals[23]}
          ac(7,4,1) = {part3_matvals[24]}
          ac(7,4,2) = {part3_matvals[25]}
          RETURN
        ELSE IF ( j.EQ.4 ) THEN
          eg(1) = {part4_evals[0]} 
          eg(2) = {part4_evals[1]}
          eg(3) = {part4_evals[2]}
          eg(4) = {part4_evals[3]}
          eg(5) = {part4_evals[4]}
          eg(6) = {part4_evals[5]}
          eg(7) = {part4_evals[6]} 
          eg(8) = {part4_evals[7]}
          eg(9) = {part4_evals[8]}
          ac(1,1,1) = {part4_matvals[0]} 
          ac(1,1,2) = {part4_matvals[1]}
          ac(1,3,1) = {part4_matvals[2]}
          ac(1,3,2) = {part4_matvals[3]}
          ac(1,5,1) = {part4_matvals[4]}
          ac(1,5,2) = {part4_matvals[5]}
          ac(2,2,1) = {part4_matvals[6]}
          ac(2,2,2) = {part4_matvals[7]}
          ac(2,4,1) = {part4_matvals[8]}
          ac(2,4,2) = {part4_matvals[9]}
          ac(3,3,1) = {part4_matvals[10]}
          ac(3,3,2) = {part4_matvals[11]}
          ac(3,5,1) = {part4_matvals[12]}
          ac(3,5,2) = {part4_matvals[13]}
          ac(4,2,1) = {part4_matvals[14]}
          ac(4,2,2) = {part4_matvals[15]}
          ac(4,4,1) = {part4_matvals[16]}
          ac(4,4,2) = {part4_matvals[17]}
          
          ac(5,1,1) = {part4_matvals[18]}
          ac(5,1,2) = {part4_matvals[19]}
          ac(5,3,1) = {part4_matvals[20]}
          ac(5,3,2) = {part4_matvals[21]}
          ac(5,5,1) = {part4_matvals[22]}
          ac(5,5,2) = {part4_matvals[23]}
          
          ac(6,2,1) = {part4_matvals[24]}
          ac(6,2,2) = {part4_matvals[25]}
          ac(6,4,1) = {part4_matvals[26]}
          ac(6,4,2) = {part4_matvals[27]}
          
          ac(7,3,1) = {part4_matvals[28]}
          ac(7,3,2) = {part4_matvals[29]}
          ac(7,5,1) = {part4_matvals[30]}
          ac(7,5,2) = {part4_matvals[31]}
          
          ac(8,2,1) = {part4_matvals[32]}
          ac(8,2,2) = {part4_matvals[33]}
          ac(8,4,1) = {part4_matvals[34]}
          ac(8,4,2) = {part4_matvals[35]}
          
          ac(9,1,1) = {part4_matvals[36]}
          ac(9,1,2) = {part4_matvals[37]}
          ac(9,3,1) = {part4_matvals[38]}
          ac(9,3,2) = {part4_matvals[39]}
          ac(9,5,1) = {part4_matvals[40]}
          ac(9,5,2) = {part4_matvals[41]}
          RETURN
        ELSE IF ( j.EQ.5 ) THEN
          eg(1) = {part5_evals[0]} 
          eg(2) = {part5_evals[1]}
          eg(3) = {part5_evals[2]}
          eg(4) = {part5_evals[3]}
          eg(5) = {part5_evals[4]}
          eg(6) = {part5_evals[5]}
          eg(7) = {part5_evals[6]}
          eg(8) = {part5_evals[7]}
          eg(9) = {part5_evals[8]}
          eg(10) = {part5_evals[9]}
          eg(11) = {part5_evals[10]}

          ac(1,2,1) = {part5_matvals[0]} 
          ac(1,2,2) = {part5_matvals[1]}
          ac(1,4,1) = {part5_matvals[2]}
          ac(1,4,2) = {part5_matvals[3]}
          ac(1,6,1) = {part5_matvals[4]}
          ac(1,6,2) = {part5_matvals[5]}
          
          ac(2,1,1) = {part5_matvals[6]}
          ac(2,1,2) = {part5_matvals[7]}
          ac(2,3,1) = {part5_matvals[8]}
          ac(2,3,2) = {part5_matvals[9]}
          ac(2,5,1) = {part5_matvals[10]}
          ac(2,5,2) = {part5_matvals[11]}
          
          ac(3,2,1) = {part5_matvals[12]}
          ac(3,2,2) = {part5_matvals[13]}
          ac(3,4,1) = {part5_matvals[14]}
          ac(3,4,2) = {part5_matvals[15]}
          ac(3,6,1) = {part5_matvals[16]}
          ac(3,6,2) = {part5_matvals[17]}
          
          ac(4,3,1) = {part5_matvals[18]}
          ac(4,3,2) = {part5_matvals[19]}
          ac(4,5,1) = {part5_matvals[20]}
          ac(4,5,2) = {part5_matvals[21]}
          
          ac(5,2,1) = {part5_matvals[22]}
          ac(5,2,2) = {part5_matvals[23]}
          ac(5,4,1) = {part5_matvals[24]}
          ac(5,4,2) = {part5_matvals[25]}
          ac(5,6,1) = {part5_matvals[26]}
          ac(5,6,2) = {part5_matvals[27]}
          
          ac(6,1,1) = {part5_matvals[28]}
          ac(6,1,2) = {part5_matvals[29]}
          ac(6,3,1) = {part5_matvals[30]}
          ac(6,3,2) = {part5_matvals[31]}
          ac(6,5,1) = {part5_matvals[32]}
          ac(6,5,2) = {part5_matvals[33]}
          
          ac(7,2,1) = {part5_matvals[34]}
          ac(7,2,2) = {part5_matvals[35]}
          ac(7,4,1) = {part5_matvals[36]}
          ac(7,4,2) = {part5_matvals[37]}
          ac(7,6,1) = {part5_matvals[38]}
          ac(7,6,2) = {part5_matvals[39]}
          
          ac(8,3,1) = {part5_matvals[40]}
          ac(8,3,2) = {part5_matvals[41]}
          ac(8,5,1) = {part5_matvals[42]}
          ac(8,5,2) = {part5_matvals[43]}
          
          ac(9,2,1) = {part5_matvals[44]}
          ac(9,2,2) = {part5_matvals[45]}
          ac(9,4,1) = {part5_matvals[46]}
          ac(9,4,2) = {part5_matvals[47]}
          ac(9,6,1) = {part5_matvals[48]}
          ac(9,6,2) = {part5_matvals[49]}
          
          ac(10,1,1) = {part5_matvals[50]}
          ac(10,1,2) = {part5_matvals[51]}
          ac(10,3,1) = {part5_matvals[52]}
          ac(10,3,2) = {part5_matvals[53]}
          ac(10,5,1) = {part5_matvals[54]}
          ac(10,5,2) = {part5_matvals[55]}
          
          ac(11,2,1) = {part5_matvals[56]}
          ac(11,2,2) = {part5_matvals[57]}
          ac(11,4,1) = {part5_matvals[58]}
          ac(11,4,2) = {part5_matvals[59]}
          ac(11,6,1) = {part5_matvals[60]}
          ac(11,6,2) = {part5_matvals[61]}
          RETURN 
        ELSE
          eg(1) = {part1_evals[0]} 
          eg(2) = {part1_evals[1]}
          eg(3) = {part1_evals[2]}
          ac(1,2,1) = {part1_matvals[0]} 
          ac(1,2,2) = {part1_matvals[1]}
          ac(2,1,1) = {part1_matvals[2]}
          ac(2,1,2) = {part1_matvals[3]}
          ac(3,2,1) = {part1_matvals[4]}
          ac(3,2,2) = {part1_matvals[5]}
          RETURN
        END IF
      END IF
      eg(1) = 0.0
      ac(1,1,1) = 1.0
      ac(1,1,2) = 0.0

      RETURN
      END"""

new_filename = input("Enter filename to be saved as (with .f like: update.f) - ")   
create_fortran_file(new_filename, text)  
