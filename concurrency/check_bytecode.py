from dis import dis

count = 0

def increment():
    global count
    count += 1

# prints the bytecode
dis(increment)