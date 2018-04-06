
filename = "doi_expanded.txt"
file = open(filename, "r", newline="\r\n")

contents = file.read().replace('\r\n', '\n')
total = 0

for line in contents.split('\n'):
    if "$" in line:
        total += float(line.replace('$', ''))

print(str(total))