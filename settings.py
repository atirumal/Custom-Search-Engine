SEARCH_KEY = "AIzaSyCvuqhrzcQhIZ36BQXCUdkTt_yBytfsUxw"
SEARCH_ID = "1081c3d1d5a00439b"
COUNTRY = "us"
SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl=" + COUNTRY
RESULT_COUNT = 20

import os
if os.path.exists("private.py"):
    from private import *