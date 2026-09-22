def f(x): 
    return -(x-5)**2 + 25


def hill_climbing(start):
    current=start
    while True:
        #Check left and right neighbours
        left=current-1
        right=current+1
        #Find the best neighbour
        if f(left)>f(current):
            next_state=left
        elif f(right)> f(current):
            next_state=right
        else:
            #No better neighbor
            break

        current=next_state
        return current,f(current)
#Starting point
start=0
#Apply Hill Climbing
solution,value = hill_climbing(start)

print("Starting point:",start)
print("Best Solution:",solution)
print("Maximum value:",value)
