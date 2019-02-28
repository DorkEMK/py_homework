import os
import sys
import datetime
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, date, timedelta
import pymystem3
mystem=pymystem3.Mystem()

date_start = datetime.strptime(sys.argv[1],"%Y/%m/%d")
date_finish = datetime.strptime(sys.argv[2],"%Y/%m/%d")

source = 'lenta.ru'

