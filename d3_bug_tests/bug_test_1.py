#gives error "OverflowError: In draw_path: Exceeded cell block limit"
#should give better error

import math
import matplotlib.pylab as plt
x=range(200000)
y=[]
for i in x:
        y.append(math.sin(x[i]))

plt.plot(x, y)
plt.show()

