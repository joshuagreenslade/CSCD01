import matplotlib.pyplot as plt
import copy
import numpy as np
import os

from matplotlib.testing.decorators import cleanup
from numpy.testing import assert_array_equal


#test should not crash and the console should be empty

@cleanup
def test_no_copy_save():
	'''
	Tests that adding a colormap still works. 
	'''
	plt.cla()
	data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])
	cm1 = plt.cm.Reds
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_no_copy_save.png")
	os.remove("test_no_copy_save.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_no_copy_save, Adding a colormap failed")
	plt.cla()

@cleanup
def test_no_copy_modify_save():
	'''
	Tests that modifying the colormap still works.
	'''
	plt.cla()
	data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])
	cm1 = plt.cm.Reds
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_no_copy_modify_save-unmodified.png")
	os.remove("test_no_copy_modify_save-unmodified.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_no_copy_modify_save, Original colormap was wrong")
	plt.cla()

	cm1.set_bad('b')
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_no_copy_modify_save-modified.png")
	os.remove("test_no_copy_modify_save-modified.png")
	assert_array_equal(cm1._lut, np.load("modified.npy"), "test_no_copy_modify_save, Modifying a colormap failed")
	plt.cla()

@cleanup
def test_copy_save_old():
	'''
	Tests that copying does not affect original colormap.
	'''
	plt.cla()
	data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])
	cm1 = plt.cm.Reds
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_copy_save_old-original.png")
	os.remove("test_copy_save_old-original.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_copy_save_old, Original colormap was wrong")
	plt.cla()


	cm2 = copy.copy(cm1)
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_copy_save_old-notcopy.png")
	os.remove("test_copy_save_old-notcopy.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_copy_save_old, Original colormap was changed")
	plt.cla()


@cleanup
def test_copy_save_new():
	'''
	Tests that copying still creates a colormap.
	'''
	plt.cla()
	data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])
	cm1 = plt.cm.Reds
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_copy_save_new-original.png")
	os.remove("test_copy_save_new-original.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_copy_save_new, Original colormap was wrong")
	plt.cla()

	cm2 = copy.copy(cm1)
	plt.imshow(data,cmap=cm2)
	plt.savefig("test_copy_save_new-copy.png")
	os.remove("test_copy_save_new-copy.png")
	assert_array_equal(cm2._lut, np.load("unchanged.npy"), "test_copy_save_new, Copied colormap was changed")
	plt.cla()

@cleanup
def test_copy_modify_save_new():
	'''
	Tests that copying and modifying a colormap still produces a modified
	colormap.
	'''
	plt.cla()
	data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])
	cm1 = plt.cm.Reds
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_copy_modify_save_new-original.png")
	os.remove("test_copy_modify_save_new-original.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_copy_modify_save_new, Original colormap was wrong")
	plt.cla()

	cm2 = copy.copy(cm1)
	cm2.set_bad('b')
	plt.imshow(data,cmap=cm2)
	plt.savefig("test_copy_modify_save_new-new_modified_copy.png")
	os.remove("test_copy_modify_save_new-new_modified_copy.png")
	assert_array_equal(cm2._lut, np.load("modified.npy"), "test_copy_modify_save_new, Copied colormap was not modified")
	plt.cla()

@cleanup
def test_copy_modify_save_multiple():
	'''
	Tests that copying and modifying only modifies the modified colormap and
	not the original.
	'''
	plt.cla()
	data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])
	cm1 = plt.cm.Reds
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_copy_modify_save_multiple-original.png")
	os.remove("test_copy_modify_save_multiple-original.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_copy_modify_save_multiple, Original colormap was wrong")
	plt.cla()

	cm2 = copy.copy(cm1)
	cm2.set_bad('b')
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_copy_modify_save_multiple-unmodified.png")
	os.remove("test_copy_modify_save_multiple-unmodified.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_copy_modify_save_multiple, Original colormap was changed")
	plt.cla()

	plt.imshow(data,cmap=cm2)
	plt.savefig("test_copy_modify_save_multiple-modified.png")
	os.remove("test_copy_modify_save_multiple-modified.png")
	assert_array_equal(cm2._lut, np.load("modified.npy"), "test_copy_modify_save_multiple, Copied colormap was not changed")
	plt.cla()

	plt.imshow(data,cmap=cm1)
	plt.savefig("test_copy_modify_save_multiple-unmodified2.png")
	os.remove("test_copy_modify_save_multiple-unmodified2.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_copy_modify_save_multiple, Original colormap was changed after copied one was saved")
	plt.cla()
