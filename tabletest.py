import re

table_text = """
  J   TAU   ENERGY(EV)   MATRIX  IR     A(K,NU)
 --------------------------------------------------------------
  0
       0   0.000000E+00    E+     A  
                                        A( 0 0 )= 1.000000
                                        A( 0 1 )= 0.000000
 --------------------------------------------------------------
  1
      -1   0.378470E-04    O-    BX  
                                        A( 1 0 )= 0.000000
                                        A( 1 1 )= 1.000000
       0   0.390220E-04    O+    BY  
                                        A( 1 0 )= 1.000000
                                        A( 1 1 )= 0.000000
       1   0.512550E-04    E+    BZ  
                                        A( 0 0 )= 1.000000
                                        A( 0 1 )= 0.000000
 --------------------------------------------------------------
  2
      -2   0.102402E-03    E+     A  
                                        A( 0 0 )=-0.039592
                                        A( 0 1 )= 0.000000
                                        A( 2 0 )= 0.999216
                                        A( 2 1 )= 0.000000
      -1   0.102483E-03    E-    BZ  
                                        A( 2 0 )= 0.000000
                                        A( 2 1 )= 1.000000
       0   0.139182E-03    O-    BY  
                                        A( 1 0 )= 0.000000
                                        A( 1 1 )= 1.000000
       1   0.142707E-03    O+    BX  
                                        A( 1 0 )= 1.000000
                                        A( 1 1 )= 0.000000
       2   0.153846E-03    E+     A  
                                        A( 0 0 )= 0.999216
                                        A( 0 1 )= 0.000000
                                        A( 2 0 )= 0.039592
                                        A( 2 1 )= 0.000000
"""

# Regex to find all scientific notation numbers in the ENERGY column
energy_values = re.findall(r"\s+([-+]?\d+\.\d+E[+-]\d+)\s+[EOB][+-]?\s+\w+", table_text[9:])

# Convert to tuple
energy_tuple = tuple(energy_values)

#print(energy_tuple)

with open("Pyridazine.out", "r") as file:
    lines = file.readlines()  # Read all lines

selected_lines = lines[37:56]  # Extract lines 38 to 56 (0-based index)

# Pass the extracted lines to the function
print(selected_lines)