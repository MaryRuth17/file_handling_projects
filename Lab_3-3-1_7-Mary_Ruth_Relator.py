file = open("gwa.txt", "r")
lines = file.readlines()

highest_name = ""
highest_gwa = 5.0  # Start with the lowest GWA

for line in lines:
    parts = line.strip().split(",") 
    if len(parts) == 2:
        name = parts[0].strip()
        gwa = float(parts[1].strip())

        if gwa < highest_gwa:
            highest_gwa = gwa
            highest_name = name

# Print the top student after processing all lines
print("Top Student:", highest_name, highest_gwa)

file.close()