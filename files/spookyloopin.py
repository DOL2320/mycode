#!/usr/bin/python3

# Create a count variable to keep track of how many times vampire appears
vamp_count = 0

# Read in the content of Dracula as a file object
with open('dracula.txt', 'r') as draculafile:
    # Open vampytimes file
    with open('vampytimes.txt', 'w') as vampyfile:
        # Loop over every line in Dracula, print each line out!
        for line in draculafile:
            # Print the line if it has the word vampire in it (case insensitive)
            if 'vampire' in line.lower():
                # Increment the count
                vamp_count += 1
                # Print the line
                print(line)
                # Write the line to vampytimes file
                vampyfile.write(line)

# Print the count
print('The word vampire appears', vamp_count, 'times.')


