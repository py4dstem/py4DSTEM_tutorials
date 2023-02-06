# Demos use of the emd.Custom class


from typing import Optional,Union
import numpy as np
from os.path import basename

from py4DSTEM.emd import (
    Custom,
    Array,
    Metadata
)






class MyCustomClass(Custom):
    """
    """

    def __init__(
        self,
        data,
        name = 'my_custom_class'
        ):
        """ `data` is a numpy array
        """
        Custom.__init__(self,name=name)


        # define some data arrays
        self.data = Array(
            data = data,
            name = 'data'
        )
        self.moredata = Array(
            data = np.tile(data,(2,2)),
            name = 'moredata'
        )


        # add some metadata
        self.metadata = Metadata(
            name = 'my_metadata',
            data = {
                'cats' : 'aregreat'
            }
        )



    # write inherited from Custom

    # read

    @classmethod
    def _get_constructor_args(cls,group):
        """
        """
        # get EMD group data
        emd_data = cls._get_emd_attr_data(cls,group)

        kwargs = {
            'name' : basename(group.name),
            'data' : emd_data['data'].data
        }

        return kwargs


