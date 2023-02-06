from py4DSTEM import emd
import sample_custom_class_module

import numpy as np
from os.path import exists
from os import remove


# prepare filepath
fp = "/Users/Ben/Desktop/test.h5"
if exists(fp):
    remove(fp)



# instantiate
instance = sample_custom_class_module.classes.MyCustomClass(
    name = 'test_instance',
    data = np.arange(12).reshape((3,4))
)



# save
emd.save(fp,instance)




# load
loaded_data = emd.read(fp)



print(loaded_data)
print()
print(loaded_data.tree('test_instance').data)
print()
print(loaded_data.tree('test_instance').moredata)




