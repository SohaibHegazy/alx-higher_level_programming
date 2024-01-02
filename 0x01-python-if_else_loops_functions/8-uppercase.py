#!/usr/bin/python3
#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False

def uppercase(str):
    for c in str:
        print("{:c}".format(ord(c) - 32 if islower else ord(c)), end="")
print("")
