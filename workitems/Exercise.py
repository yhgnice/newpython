#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/07/13 
import  sys
x = 0x1234
print sys.getsizeof(x)
print sys.getrefcount(x)
y = x

import types
x = 20
print type(x) is types.IntType

print x.__class__

y = x
print hex(id(x)),hex(id(y))


hex(id(int)),hex(id(types.IntType))

if __name__ == '__main__':
    pass