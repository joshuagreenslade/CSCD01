import matplotlib.pyplot as plt
import copy
import numpy as np

#test should not crash and the console should be empty

#test that modifying a colormap still works
#test should create 2 graphs
#test_no_copy_modify_save-modified.png should look identical to modified.png
#test_no_copy_modify_save-unmodified.png should look identical to original.png

data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])
cm1 = plt.cm.Reds
plt.imshow(data,cmap=cm1)
plt.savefig("test_no_copy_modify_save-unmodified.png")
plt.cla()

cm1.set_bad('b')
plt.imshow(data,cmap=cm1)
plt.savefig("test_no_copy_modify_save-modified.png")
plt.cla()

