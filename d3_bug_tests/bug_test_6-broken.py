#animate does not run but it should

import matplotlib
from matplotlib import pyplot as plt
fig = plt.figure()
def animate(i):
    print("hi")
from matplotlib import animation
animation.FuncAnimation(fig, animate)
plt.show()
