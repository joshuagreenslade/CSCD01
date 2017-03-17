import matplotlib.pyplot as plt
import copy
import numpy as np

#test should not crash and the console should be empty

#test that the adding a colormap still works
#test_no_copy_save.png should look identical to original.png

data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])
cm1 = plt.cm.Reds
plt.imshow(data,cmap=cm1)
plt.savefig("test_no_copy_save.png")
plt.cla()
