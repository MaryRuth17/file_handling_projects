file = open("mylife.txt", "w")

while True:
    line = input("Enter line: ")
    file.write(line + "\n")
    more = input("Are there more lines y/n? ").strip().lower()
    if more != "yes":
        print("okay! thnx!")
        break

file.close()