from struct import Struct as _Struct
from struct import *

class BetterStruct(_Struct):

    def __init__(self, format):
        if type(format) == unicode:
            format = format.encode("utf-8")
        super(BetterStruct, self).__init__(format)

    def pack_into(self, buff, offset, *args):
        return super(BetterStruct, self).pack_into(buff, offset, *args)

    def unpack_from(self, buff, offset):
        return super(BetterStruct, self).unpack_from(buffer(buff), offset)


Struct = BetterStruct
