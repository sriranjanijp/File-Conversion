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

text = f"""
  J   TAU   ENERGY(EV)   MATRIX  IR     A(K,NU)
 --------------------------------------------------------------
  2
      -2   0.102402E-03    E+     A  
                                        A( 0 0 )= {b}
                                        A( 0 1 )= {c}
                                        A( 2 0 )= {a}
                                        A( 2 1 )= {c}
 --------------------------------------------------------------
"""
print(text)

text = f"""      
      SUBROUTINE ASYMTOP(j,itau,ntau,n,ac,eg)
      IMPLICIT REAL*4 (A-H, O-Z)
 
c
c     This subroutine has to be replaced with proper Ac and Eg values
c     for other C2v molecules.
c     These data are for the Pyridazine molecule with up to J=5(AXX= $axx  BYY= $byy  CZZ= $czz)
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
          eg(1) = 0.176773E-04
          eg(2) = 0.178104E-04 
          eg(3) = 0.215223E-04
          eg(4) = 0.230859E-04 
          eg(5) = 0.239351E-04
          ac(1,1,1) = -0.145820E0
          ac(1,1,2) = 0.0
          ac(1,3,1) = 0.989311E0
          ac(1,3,2) = 0.0
          ac(2,2,1) = 0.0
          ac(2,2,2) = 1.0
          ac(3,3,1) = 0.0
          ac(3,3,2) = 1.0
          ac(4,2,1) = 1.0
          ac(4,2,2) = 0.0
          ac(5,1,1) = 0.989311E0
          ac(5,1,2) = 0.0
          ac(5,3,1) = 0.145820E0
          ac(5,3,2) = 0.0
          RETURN
        ELSE IF ( j.EQ.3 ) THEN
          eg(1) = 0.340260E-04 
          eg(2) = 0.340481E-04
          eg(3) = 0.409958E-04
          eg(4) = 0.416124E-04
          eg(5) = 0.446394E-04
          eg(6) = 0.477445E-04
          eg(7) = 0.482206E-04
          ac(1,2,1) = 0.0
          ac(1,2,2) = -0.095534E0
          ac(1,4,1) = 0.0
          ac(1,4,2) = 0.995426E0
          ac(2,1,1) = -0.073893E0
          ac(2,1,2) = 0.0
          ac(2,3,1) = 0.997266E0
          ac(2,3,2) = 0.0
          ac(3,2,1) = -0.292142E0
          ac(3,2,2) = 0.0
          ac(3,4,1) = 0.956375E0
          ac(3,4,2) = 0.0
          ac(4,3,1) = 0.0
          ac(4,3,2) = 1.0
          ac(5,2,1) = 0.0
          ac(5,2,2) = 0.995426E0
          ac(5,4,1) = 0.0
          ac(5,4,2) = 0.095534E0
          ac(6,1,1) = 0.997266E0
          ac(6,1,2) = 0.0
          ac(6,3,1) = 0.073893E0
          ac(6,3,2) = 0.0
          ac(7,2,1) = 0.956375E0
          ac(7,2,2) = 0.0
          ac(7,4,1) = 0.292142E0
          ac(7,4,2) = 0.0
          RETURN
        ELSE IF ( j.EQ.4 ) THEN
          eg(1) = 0.552654E-04
          eg(2) = 0.552684E-04
          eg(3) = 0.654229E-04
          eg(4) = 0.655713E-04
          eg(5) = 0.718351E-04
          eg(6) = 0.734536E-04
          eg(7) = 0.756721E-04 
          eg(8) = 0.807357E-04
          eg(9) = 0.809615E-04
          ac(1,1,1) = 0.011359E0
          ac(1,1,2) = 0.0
          ac(1,3,1) = -0.421080E0
          ac(1,3,2) = 0.0
          ac(1,5,1) = 0.906952E0
          ac(1,5,2) = 0.0
          ac(2,2,1) = 0.0
          ac(2,2,2) = -0.076049
          ac(2,4,1) = 0.0
          ac(2,4,2) = 0.997104
          ac(3,3,1) = 0.0
          ac(3,3,2) = -0.206250E0
          ac(3,5,1) = 0.0
          ac(3,5,2) = 0.978499E0
          ac(4,2,1) = -0.137714
          ac(4,2,2) = 0.0
          ac(4,4,1) = 0.990472
          ac(4,4,2) = 0.0
          
          ac(5,1,1) = -0.078215E0
          ac(5,1,2) = 0.0
          ac(5,3,1) = 0.903858E0
          ac(5,3,2) = 0.0
          ac(5,5,1) = 0.420623E0
          ac(5,5,2) = 0.0
          
          ac(6,2,1) = 0.0
          ac(6,2,2) = 0.997104E0
          ac(6,4,1) = 0.0
          ac(6,4,2) = 0.076049
          
          ac(7,3,1) = 0.0
          ac(7,3,2) = 0.978499E0
          ac(7,5,1) = 0.0
          ac(7,5,2) = 0.206250E0
          
          ac(8,2,1) = 0.990472
          ac(8,2,2) = 0.0
          ac(8,4,1) = 0.137714
          ac(8,4,2) = 0.0
          
          ac(9,1,1) = 0.996872E0
          ac(9,1,2) = 0.0
          ac(9,3,1) = 0.075715E0
          ac(9,3,2) = 0.0
          ac(9,5,1) = 0.022668E0
          ac(9,5,2) = 0.0
          RETURN
        ELSE IF ( j.EQ.5 ) THEN
          eg(1) = 0.814338E-04
          eg(2) = 0.814341E-04
          eg(3) = 0.946179E-04
          eg(4) = 0.946444E-04
          eg(5) = 0.104420E-03
          eg(6) = 0.104966E-03
          eg(7) = 0.110246E-03
          eg(8) = 0.113418E-03
          eg(9) = 0.114841E-03
          eg(10) = 0.122112E-03
          eg(11) = 0.122208E-03
          
          ac(1,2,1) = 0.0
          ac(1,2,2) = 0.007711E0
          ac(1,4,1) = 0.0
          ac(1,4,2) = -0.344331E0
          ac(1,6,1) = 0.0
          ac(1,6,2) = 0.938817E0
          
          ac(2,1,1) = 0.006185E0
          ac(2,1,2) = 0.0
          ac(2,3,1) = -0.200544E0
          ac(2,3,2) = 0.0
          ac(2,5,1) = 0.979665E0
          ac(2,5,2) = 0.0
          
          ac(3,2,1) = 0.033976E0
          ac(3,2,2) = 0.0
          ac(3,4,1) = -0.514471E0
          ac(3,4,2) = 0.0
          ac(3,6,1) = 0.856835E0
          ac(3,6,2) = 0.0
          
          ac(4,3,1) = 0.0
          ac(4,3,2) = -0.145820E0
          ac(4,5,1) = 0.0
          ac(4,5,2) = 0.989311E0
          
          ac(5,2,1) = 0.0
          ac(5,2,2) = -0.073435E0
          ac(5,4,1) = 0.0
          ac(5,4,2) = 0.936115E0
          ac(5,6,1) = 0.0
          ac(5,6,2) = 0.343943E0
          
          ac(6,1,1) = -0.073224E0
          ac(6,1,2) = 0.0
          ac(6,3,1) = 0.976963E0
          ac(6,3,2) = 0.0
          ac(6,5,1) = 0.200453E0
          ac(6,5,2) = 0.0
          
          ac(7,2,1) = -0.155176E0
          ac(7,2,2) = 0.0
          ac(7,4,1) = 0.844217E0
          ac(7,4,2) = 0.0
          ac(7,6,1) = 0.513048E0
          ac(7,6,2) = 0.0
          
          ac(8,3,1) = 0.0
          ac(8,3,2) = 0.989311E0
          ac(8,5,1) = 0.0
          ac(8,5,2) = 0.145820E0
          
          ac(9,2,1) = 0.0
          ac(9,2,2) = 0.997270E0
          ac(9,4,1) = 0.0
          ac(9,4,2) = 0.071594E0
          ac(9,6,1) = 0.0
          ac(9,6,2) = 0.018068E0
          
          ac(10,1,1) = 0.997296E0
          ac(10,1,2) = 0.0
          ac(10,3,1) = 0.072975E0
          ac(10,3,2) = 0.0
          ac(10,5,1) = 0.008642E0
          ac(10,5,2) = 0.0
          
          ac(11,2,1) = 0.987302E0
          ac(11,2,2) = 0.0
          ac(11,4,1) = 0.150391E0
          ac(11,4,2) = 0.0
          ac(11,6,1) = 0.051150E0
          ac(11,6,2) = 0.0
          RETURN 
        ELSE
          eg(1) = 0.617550E-05
          eg(2) = 0.669670E-05 
          eg(3) = 0.793400E-05 
          ac(1,2,1) = 0.0
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




