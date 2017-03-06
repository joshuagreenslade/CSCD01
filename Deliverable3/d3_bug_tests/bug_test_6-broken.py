#animate does not run but it should
#the animation.FuncAnimation(fig, animate) is not saved in a var so python's garbage collection cleans it up
#before it can execute

#fix by possibly saving the animation in figure

import matplotlib
from matplotlib import pyplot as plt
fig = plt.figure()
def animate(i):
    print("hi")
from matplotlib import animation
animation.FuncAnimation(fig, animate)
plt.show()
