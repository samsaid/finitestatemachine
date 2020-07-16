import time

#states
def trafficLight(state):
    green
    red
    yellow


#functions (transitions)
def transitions(state):
    if state == 'green':
        state = 'yellow'
        print("The traffic light has changed from green to " + state + "\nStop!")
    elif state == 'yellow':
        state = 'red'
        print("The traffic light has changed from yellow to " + state + "\nStop!")
    elif state == 'red':
        state = 'green'
        print("The traffic light has changed from red to " + state + "\nGo!")
    else:
       print("none")

#initial start state
print("Traffic Light Cycle begins with initial Green State")
time.sleep(9)

for i in range(2):
    transitions('green')
    time.sleep(5)
    transitions('red')
    time.sleep(5)
    transitions('yellow')
    time.sleep(5)
 
