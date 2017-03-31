import matplotlib.pyplot as plt
import copy
import numpy as np

#test should not crash and the console should be empty

#test that copying and modifying still produces a modified colormap
#test should create 2 graphs
#test_copy_modify_save_new-new_modified_copy.png should look identical to modified.png
#test_copy_modify_save_new-original.png should look identical to original.png

data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])
cm1 = plt.cm.Reds
plt.imshow(data,cmap=cm1)
plt.savefig("test_copy_modify_save_new-original.png")
plt.cla()

cm2 = copy.copy(cm1)
cm2.set_bad('b')
plt.imshow(data,cmap=cm2)
plt.savefig("test_copy_modify_save_new-new_modified_copy.png")
plt.cla()
