
def count (string, letter):
    number_found = 0 
    for char in string:
        if char == letter:
            number_found = number_found + 1
    return number_found

found = count("the twin peaks of kilimanjaro", "i")
print found