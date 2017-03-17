import matplotlib.pyplot as plt
import copy
import numpy as np

#test should not crash and the console should be empty

#test that copying still creates a colormap
#test should create 2 graphs
#test_copy_save_new-original.png and test_copy_save_new-copy.png should look identical to original.png

data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])
cm1 = plt.cm.Reds
plt.imshow(data,cmap=cm1)
plt.savefig("test_copy_save_new-original.png")
plt.cla()

cm2 = copy.copy(cm1)
plt.imshow(data,cmap=cm2)
plt.savefig("test_copy_save_new-copy.png")
plt.cla()
