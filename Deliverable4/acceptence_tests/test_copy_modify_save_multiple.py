import matplotlib.pyplot as plt
import copy
import numpy as np

#test should not crash and the console should be empty

#test that copying and modifying only modifies the modified colormap and not the original
#test will create 4 graphs
#test_copy_modify_save_multiple-original.png and test_copy_modify_save_multiple-unmodified.png and test_copy_modify_save_multiple-unmodified2.png should look identical to original.png
#test_copy_modify_save_multiple-modified.png should look identical to modified.png

data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])
cm1 = plt.cm.Reds
plt.imshow(data,cmap=cm1)
plt.savefig("test_copy_modify_save_multiple-original.png")
plt.cla()

cm2 = copy.copy(cm1)
cm2.set_bad('b')
plt.imshow(data,cmap=cm1)
plt.savefig("test_copy_modify_save_multiple-unmodified.png")
plt.cla()

plt.imshow(data,cmap=cm2)
plt.savefig("test_copy_modify_save_multiple-modified.png")
plt.cla()

plt.imshow(data,cmap=cm1)
plt.savefig("test_copy_modify_save_multiple-unmodified2.png")
plt.cla()
