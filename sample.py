import re

def extract_data(out_file):
    with open(out_file, "r", encoding="utf-8") as file:
        out_content = file.readlines()

    # Extract rotational constants
    rot_constants_pattern = r"AXX=\s*([\d.E+-]+)\s*BYY=\s*([\d.E+-]+)\s*CZZ=\s*([\d.E+-]+)"
    rot_constants_match = re.search(rot_constants_pattern, "".join(out_content))

    axx, byy, czz = rot_constants_match.groups() if rot_constants_match else (None, None, None)

    # Extract energy levels
    energy_pattern = r"\s*(-?\d+)\s+([\d.E+-]+)\s+\S+\s+\S+"
    energy_levels = []
    current_j = None

    for line in out_content:
        j_match = re.match(r"\s*(\d+)\s*$", line)
        if j_match:
            current_j = int(j_match.group(1))
        
        energy_match = re.match(energy_pattern, line)
        if energy_match and current_j is not None:
            tau, energy = energy_match.groups()
            energy_levels.append((current_j, int(tau), float(energy)))

    return axx, byy, czz, energy_levels

def update_f_file(f_file, axx, byy, czz, energy_levels, output_file):
    with open(f_file, "r", encoding="utf-8") as file:
        f_content = file.readlines()

    updated_f_content = []
    in_energy_section = False
    j_values_inserted = set()

    for line in f_content:
        if "These data are for the Pyridazine molecule" in line and axx and byy and czz:
            line = f"c     These data are for the Pyridazine molecule with up to J=5(AXX= {axx}  BYY= {byy}  CZZ= {czz})\n"
        
        if "IF ( j.EQ." in line:
            in_energy_section = True
            current_j = int(re.search(r"j.EQ.(\d+)", line).group(1))
        
        if in_energy_section and "eg(" in line and current_j in {j for j, _, _ in energy_levels}:
            if current_j not in j_values_inserted:
                j_values_inserted.add(current_j)
                relevant_energies = [e for j, _, e in energy_levels if j == current_j]
                energy_lines = [f"          eg({i+1}) = {energy:.6E} \n" for i, energy in enumerate(relevant_energies)]
                line = "".join(energy_lines)

        updated_f_content.append(line)

    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(updated_f_content)

# File paths
out_file = "Pyridazine.out"
f_file = "asym.f.txt"
output_file = "asym_updated.f.txt"

# Process files
axx, byy, czz, energy_levels = extract_data(out_file)
update_f_file(f_file, axx, byy, czz, energy_levels, output_file)

print(f"Updated file saved as {output_file}")
