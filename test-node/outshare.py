#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/07/20 

import tushare


import tushare as ts

# result = ts.get_hist_data('600848',start='2015-01-05',end='2015-01-09')
# print type(result)
# print result
# print ts.get_hist_data('600848', ktype='W')
# print result[['open','close','high','low','volume']]
# df[['code','name','price','bid','ask','volume','amount','time']]

print ts.get_today_all()
if __name__ == '__main__':
    pass

 
 @python