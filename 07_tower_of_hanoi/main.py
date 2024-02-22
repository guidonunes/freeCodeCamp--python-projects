NUMBER_OF_DISKS = 3

A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n <= 0:
        return
        # Move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
        
        # Move the nth disk from source to target
    target.append(source.pop())
        
        # Display our progress
    print( A, B, C, '\n')
        
        # Move the n - 1 disks that we left on auxiliary onto target
    move(n - 1, auxiliary, source, target)

move(NUMBER_OF_DISKS, A, B, C)