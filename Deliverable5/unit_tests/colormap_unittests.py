import matplotlib.pyplot as plt
import copy
import numpy as np
import os

from matplotlib.testing.decorators import cleanup
from numpy.testing import assert_array_equal


@cleanup
def test_no_copy_save():
	'''
	Tests that adding a colormap still works. 
	'''
	data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])

	#use a copy to make it independent from other tests
	cm1 = copy.copy(plt.cm.Reds)
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_no_copy_save.png")

	#remove temporary image
	os.remove("test_no_copy_save.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_no_copy_save, Adding a colormap failed")

@cleanup
def test_no_copy_modify_save():
	'''
	Tests that modifying the colormap still works.
	'''
	data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])

	#use a copy to make it independent from other tests
	cm1 = copy.copy(plt.cm.Reds)
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_no_copy_modify_save-unmodified.png")

	#remove temporary image
	os.remove("test_no_copy_modify_save-unmodified.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_no_copy_modify_save, Original colormap was wrong")

	#modify the colormap
	cm1.set_bad('b')
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_no_copy_modify_save-modified.png")

	#remove temporary image
	os.remove("test_no_copy_modify_save-modified.png")
	assert_array_equal(cm1._lut, np.load("modified.npy"), "test_no_copy_modify_save, Modifying a colormap failed")

@cleanup
def test_copy_save_old():
	'''
	Tests that copying does not affect original colormap.
	'''
	data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])

	#use a copy to make it independent from other tests
	cm1 = copy.copy(plt.cm.Reds)
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_copy_save_old-original.png")

	#remove temporary image
	os.remove("test_copy_save_old-original.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_copy_save_old, Original colormap was wrong")

	#copy the colormap and save the original
	cm2 = copy.copy(cm1)
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_copy_save_old-notcopy.png")

	#remove temporary image
	os.remove("test_copy_save_old-notcopy.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_copy_save_old, Original colormap was changed")

@cleanup
def test_copy_save_new():
	'''
	Tests that copying still creates a colormap.
	'''
	data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])

	#use a copy to make it independent from other tests
	cm1 = copy.copy(plt.cm.Reds)
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_copy_save_new-original.png")

	#remove temporary image
	os.remove("test_copy_save_new-original.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_copy_save_new, Original colormap was wrong")

	#copy the colormap and save the copy
	cm2 = copy.copy(cm1)
	plt.imshow(data,cmap=cm2)
	plt.savefig("test_copy_save_new-copy.png")

	#remove temporary image
	os.remove("test_copy_save_new-copy.png")
	assert_array_equal(cm2._lut, np.load("unchanged.npy"), "test_copy_save_new, Copied colormap was changed")

@cleanup
def test_copy_modify_save_new():
	'''
	Tests that copying and modifying a colormap still produces a modified
	colormap.
	'''
	data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])

	#use a copy to make it independent from other tests
	cm1 = copy.copy(plt.cm.Reds)
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_copy_modify_save_new-original.png")

	#remove temporary image
	os.remove("test_copy_modify_save_new-original.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_copy_modify_save_new, Original colormap was wrong")

	#copy the colormap, modify the colormap, and save the copy
	cm2 = copy.copy(cm1)
	cm2.set_bad('b')
	plt.imshow(data,cmap=cm2)
	plt.savefig("test_copy_modify_save_new-new_modified_copy.png")

	#remove temporary image
	os.remove("test_copy_modify_save_new-new_modified_copy.png")
	assert_array_equal(cm2._lut, np.load("modified.npy"), "test_copy_modify_save_new, Copied colormap was not modified")

@cleanup
def test_copy_modify_save_multiple():
	'''
	Tests that copying and modifying only modifies the modified colormap and
	not the original.
	'''
	data = np.ma.masked_array([[1,2,3],[2,3,4]], mask=[[1,0,0],[0,0,0]])

	#use a copy to make it independent from other tests
	cm1 = copy.copy(plt.cm.Reds)
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_copy_modify_save_multiple-original.png")

	#remove temporary image
	os.remove("test_copy_modify_save_multiple-original.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_copy_modify_save_multiple, Original colormap was wrong")

	#copy the colormap, modify the colormap, and save the original
	cm2 = copy.copy(cm1)
	cm2.set_bad('b')
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_copy_modify_save_multiple-unmodified.png")

	#remove temporary image
	os.remove("test_copy_modify_save_multiple-unmodified.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_copy_modify_save_multiple, Original colormap was changed")

	#save the copy
	plt.imshow(data,cmap=cm2)
	plt.savefig("test_copy_modify_save_multiple-modified.png")

	#remove temporary image
	os.remove("test_copy_modify_save_multiple-modified.png")
	assert_array_equal(cm2._lut, np.load("modified.npy"), "test_copy_modify_save_multiple, Copied colormap was not changed")

	#save the original
	plt.imshow(data,cmap=cm1)
	plt.savefig("test_copy_modify_save_multiple-unmodified2.png")

	#remove temporary image
	os.remove("test_copy_modify_save_multiple-unmodified2.png")
	assert_array_equal(cm1._lut, np.load("unchanged.npy"), "test_copy_modify_save_multiple, Original colormap was changed after copied one was saved")
