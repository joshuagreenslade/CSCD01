import matplotlib
from matplotlib import pyplot as plt
fig = plt.figure()
def animate(i):
    print("hi")
from matplotlib import animation
anim=animation.FuncAnimation(fig, animate)
plt.show()
