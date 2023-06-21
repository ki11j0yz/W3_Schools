# as in the 'for' loop section, a continue statement can stop the current iteration, and continue with the next - this might mean something is going to be skipped:

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# watch how the output skips '3' - it is because we gave the while loop a condition, and since that condition was met - we continue on
