import colormap_unittests

try:
	colormap_unittests.test_no_copy_save()
except AssertionError, e:
	print(e)

try:
	colormap_unittests.test_no_copy_modify_save()
except AssertionError, e:
	print(e)

try:
	colormap_unittests.test_copy_save_old()
except AssertionError, e:
	print(e)

try:
	colormap_unittests.test_copy_save_new()
except AssertionError, e:
	print(e)

try:
	colormap_unittests.test_copy_modify_save_new()
except AssertionError, e:
	print(e)

try:
	colormap_unittests.test_copy_modify_save_multiple()
except AssertionError, e:
	print(e)