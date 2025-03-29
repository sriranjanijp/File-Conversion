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
    
part1_matvals = extract_matrix_values((out_content[25:35]))
part2_matvals = extract_matrix_values((out_content[37:58]))
part3_matvals = extract_matrix_values((out_content[57:91]))
part4_matvals = extract_matrix_values((out_content[92:144]))
part5_matvals = extract_matrix_values((out_content[145:219]))

print (part2_matvals)

text = f"""      
      SUBROUTINE ASYMTOP(j,itau,ntau,n,ac,eg)
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
          eg(2) = 0.192097E-03
          eg(3) = 0.255847E-03
          eg(4) = 0.256248E-03
          eg(5) = 0.291237E-03
          eg(6) = 0.298283E-03
          eg(7) = 0.307931E-03
          ac(1,2,1) = {part3_matvals[0]} 
          ac(1,2,2) = -0.022956E0
          ac(1,4,1) = 0.0
          ac(1,4,2) = 0.999736E0
          ac(2,1,1) = -0.021433E0
          ac(2,1,2) = 0.0
          ac(2,3,1) = 0.999770E0
          ac(2,3,2) = 0.000000
          ac(3,2,1) = -0.087712E0
          ac(3,2,2) = 0.0
          ac(3,4,1) = 0.996146E0
          ac(3,4,2) = 0.0
          ac(4,3,1) = 0.0
          ac(4,3,2) = 1.0
          ac(5,2,1) = 0.0
          ac(5,2,2) = 0.999736E0
          ac(5,4,1) = 0.0
          ac(5,4,2) = 0.022956E0
          ac(6,1,1) = 0.999770E0
          ac(6,1,2) = 0.0
          ac(6,3,1) = 0.021433E0
          ac(6,3,2) = 0.0
          ac(7,2,1) = 0.996146E0
          ac(7,2,2) = 0.0
          ac(7,4,1) = 0.087712E0
          ac(7,4,2) = 0.0
          RETURN
        ELSE IF ( j.EQ.4 ) THEN
          eg(1) = {part4_evals[0]} 
          eg(2) = 0.307359E-03
          eg(3) = 0.396941E-03
          eg(4) = 0.396965E-03
          eg(5) = 0.460146E-03
          eg(6) = 0.461331E-03
          eg(7) = 0.494079E-03 
          eg(8) = 0.505805E-03
          eg(9) = 0.513735E-03
          ac(1,1,1) = {part4_matvals[0]} 
          ac(1,1,2) = 0.0
          ac(1,3,1) = -0.148707E0
          ac(1,3,2) = 0.0
          ac(1,5,1) = 0.988881E0
          ac(1,5,2) = 0.0
          ac(2,2,1) = 0.0
          ac(2,2,2) = -0.020195E0
          ac(2,4,1) = 0.0
          ac(2,4,2) = 0.999796E0
          ac(3,3,1) = 0.0
          ac(3,3,2) = -0.048061E0
          ac(3,5,1) = 0.0
          ac(3,5,2) = 0.998844E0
          ac(4,2,1) =-0.042884E0
          ac(4,2,2) = 0.0
          ac(4,4,1) = 0.999080E0
          ac(4,4,2) = 0.0
          
          ac(5,1,1) =-0.020234E0
          ac(5,1,2) = 0.0
          ac(5,3,1) = 0.988676E0
          ac(5,3,2) = 0.0
          ac(5,5,1) = 0.148692E0
          ac(5,5,2) = 0.0
          
          ac(6,2,1) = 0.0
          ac(6,2,2) = 0.999796E0
          ac(6,4,1) = 0.0
          ac(6,4,2) = 0.020195E0
          
          ac(7,3,1) = 0.0
          ac(7,3,2) = 0.998844E0
          ac(7,5,1) = 0.0
          ac(7,5,2) = 0.048061E0
          
          ac(8,2,1) = 0.999080E0
          ac(8,2,2) = 0.0
          ac(8,4,1) = 0.042884E0
          ac(8,4,2) = 0.0
          
          ac(9,1,1) = 0.999795E0
          ac(9,1,2) = 0.0
          ac(9,3,1) = 0.020125E0
          ac(9,3,2) = 0.0
          ac(9,5,1) = 0.002241E0
          ac(9,5,2) = 0.0
          RETURN
        ELSE IF ( j.EQ.5 ) THEN
          eg(1) = {part5_evals[0]} 
          eg(2) = 0.448237E-03
          eg(3) = 0.563454E-03
          eg(4) = 0.563455E-03
          eg(5) = 0.652901E-03
          eg(6) = 0.652998E-03
          eg(7) = 0.715091E-03
          eg(8) = 0.717785E-03
          eg(9) = 0.747807E-03
          eg(10) = 0.765335E-03
          eg(11) = 0.771520E-03
          
          ac(1,2,1) = {part5_matvals[0]} 
          ac(1,2,2) = 0.000490E0
          ac(1,4,1) = 0.0
          ac(1,4,2) = -0.080483E0
          ac(1,6,1) = 0.0
          ac(1,6,2) = 0.996756E0
          
          ac(2,1,1) = 0.000462E0
          ac(2,1,2) = 0.0
          ac(2,3,1) = -0.067930E0
          ac(2,3,2) = 0.0
          ac(2,5,1) = 0.997690E0
          ac(2,5,2) = 0.0
          
          ac(3,2,1) = 0.002332E0
          ac(3,2,2) = 0.0
          ac(3,4,1) = -0.218480E0
          ac(3,4,2) = 0.0
          ac(3,6,1) = 0.975839E0
          ac(3,6,2) = 0.0
          
          ac(4,3,1) = 0.0
          ac(4,3,2) = -0.039592E0
          ac(4,5,1) = 0.0
          ac(4,5,2) = 0.999216E0
          
          ac(5,2,1) = 0.0
          ac(5,2,2) = -0.019220E0
          ac(5,4,1) = 0.0
          ac(5,4,2) = 0.996571E0
          ac(5,6,1) = 0.0
          ac(5,6,2) = 0.080477E0
          
          ac(6,1,1) = -0.019219E0
          ac(6,1,2) = 0.0
          ac(6,3,1) = 0.997505E0
          ac(6,3,2) = 0.0
          ac(6,5,1) = 0.067926E0
          ac(6,5,2) = 0.0
          
          ac(7,2,1) = -0.039774E0
          ac(7,2,2) = 0.0
          ac(7,4,1) = 0.975049E0
          ac(7,4,2) = 0.0
          ac(7,6,1) = 0.218399E0
          ac(7,6,2) = 0.0
          
          ac(8,3,1) = 0.0
          ac(8,3,2) = 0.999216E0
          ac(8,5,1) = 0.0
          ac(8,5,2) = 0.039592E0
          
          ac(9,2,1) = 0.0
          ac(9,2,2) = 0.999815E0
          ac(9,4,1) = 0.0
          ac(9,4,2) = 0.019197E0
          ac(9,6,1) = 0.0
          ac(9,6,2) = 0.001059E0
          
          ac(10,1,1) = 0.999815E0
          ac(10,1,2) = 0.0
          ac(10,3,1) = 0.019206E0
          ac(10,3,2) = 0.0
          ac(10,5,1) = 0.000844E0
          ac(10,5,2) = 0.0
          
          ac(11,2,1) = 0.999206E0
          ac(11,2,2) = 0.0
          ac(11,4,1) = 0.039322E0
          ac(11,4,2) = 0.0
          ac(11,6,1) = 0.006416E0
          ac(11,6,2) = 0.0
          RETURN 
        ELSE
          eg(1) = {part1_evals[0]} 
          eg(2) = 0.390220E-04 
          eg(3) = 0.512550E-04 
          ac(1,2,1) = {part1_evals[0]} 
          ac(1,2,2) = 1.0
          ac(2,1,1) = 1.0
          ac(2,1,2) = 0.0
          ac(3,2,1) = 1.0
          ac(3,2,2) = 0.0
          RETURN
        END IF
      END IF
      eg(1) = 0.0
      ac(1,1,1) = 1.0
      ac(1,1,2) = 0.0

      RETURN
      END"""
    
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




