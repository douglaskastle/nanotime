# -*- coding: utf-8 -*-
import datetime
import unittest
import nanotime.nanotime as nanotime
from nanotime.Test.utils import checkAttributes, hasAttributes

class TestNanoTimeDelta(unittest.TestCase):
	
	def testNanoTimeDeltaInit(self):
		d = ('days', 'seconds', 'microseconds', 'nanoseconds','max', 'min','total_seconds')
		t = nanotime.timedelta()
		hasAttributes(t, d)
		
		t = nanotime.timedelta(days=1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['days'] = 1
		checkAttributes(t, d)

		if not str(t) == "1 day, 0:00:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(hours=1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['seconds'] = 3600
		checkAttributes(t, d)

		if not str(t) == "1:00:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(minutes=1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['seconds'] = 60
		checkAttributes(t, d)
	
		if not str(t) == "0:01:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(seconds=1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['seconds'] = 1
		checkAttributes(t, d)
	
		if not str(t) == "0:00:01":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(microseconds=1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['microseconds'] = 1
		checkAttributes(t, d)
	
		if not str(t) == "0:00:00.000001":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(nanoseconds=1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['nanoseconds'] = 1
		checkAttributes(t, d)

		t = nanotime.timedelta(nanoseconds=1001)
		d = {'days': 0, 'seconds': 0, 'microseconds': 1, 'nanoseconds': 0,}
		d['nanoseconds'] = 1
		checkAttributes(t, d)

		if not str(t) == "0:00:00.000001:001":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(days=1, hours=1, minutes=1, seconds=1, microseconds=1, nanoseconds=1)
		d = {'days': 1, 'seconds': 3661, 'microseconds': 1, 'nanoseconds': 1,}
		checkAttributes(t, d)

		if not str(t) == "1 day, 1:01:01.000001:001":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(days=-1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['days'] = -1
		checkAttributes(t, d)

		if not str(t) == "-1 day, 0:00:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(hours=-1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['days'] = -1
		d['seconds'] = 82800
		checkAttributes(t, d)

		if not str(t) == "-1 day, 23:00:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(minutes=-1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['days'] = -1
		d['seconds'] = 86340
		checkAttributes(t, d)
	
		if not str(t) == "-1 day, 23:59:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(seconds=-1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['days'] = -1
		d['seconds'] = 86399
		checkAttributes(t, d)
	
		if not str(t) == "-1 day, 23:59:59":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(microseconds=-1)
		d = {'days': 0, 'seconds': 0, 'microseconds': 0, 'nanoseconds': 0,}
		d['days'] = -1
		d['seconds'] = 86399
		d['microseconds'] = 999999
		checkAttributes(t, d)
	
		if not str(t) == "-1 day, 23:59:59.999999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(days=-1, hours=-1)
		d = {'days': -2, 'seconds': 82800, 'microseconds': 0, 'nanoseconds': 0,}
		checkAttributes(t, d)

		if not str(t) == "-2 days, 23:00:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(days=-1, hours=-1, minutes=-1)
		d = {'days': -2, 'seconds': 82740, 'microseconds': 0, 'nanoseconds': 0,}
		checkAttributes(t, d)

		if not str(t) == "-2 days, 22:59:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(days=-1, hours=-1, minutes=-1, seconds=-1)
		d = {'days': -2, 'seconds': 82739, 'microseconds': 0, 'nanoseconds': 0,}
		checkAttributes(t, d)

		if not str(t) == "-2 days, 22:58:59":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(days=-1, hours=-1, minutes=-1, seconds=-1, microseconds=-1, nanoseconds=1)
		d = {'days': -2, 'seconds': 82738, 'microseconds': 999999, 'nanoseconds': 1,}
		checkAttributes(t, d)

		if not str(t) == "-2 days, 22:58:58.999999:001":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(nanoseconds=-1)
		d = {'days': -1, 'seconds': 86399, 'microseconds': 999999, 'nanoseconds': 999,}
		checkAttributes(t, d)

		if not str(t) == "-1 day, 23:59:59.999999:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(nanoseconds=-1001)
		d = {'days': -1, 'seconds': 86399, 'microseconds': 999998, 'nanoseconds': 999,}
		checkAttributes(t, d)

		if not str(t) == "-1 day, 23:59:59.999998:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(microseconds=-1, nanoseconds=-1)
		d = {'days': -1, 'seconds': 86399, 'microseconds': 999998, 'nanoseconds': 999,}
		checkAttributes(t, d)

		if not str(t) == "-1 day, 23:59:59.999998:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(seconds=-1, microseconds=-1, nanoseconds=-1)
		d = {'days': -1, 'seconds': 86398, 'microseconds': 999998, 'nanoseconds': 999,}
		checkAttributes(t, d)

		if not str(t) == "-1 day, 23:59:58.999998:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

		t = nanotime.timedelta(minutes=-1, seconds=-1, microseconds=-1, nanoseconds=-1)
		d = {'days': -1, 'seconds': 86338, 'microseconds': 999998, 'nanoseconds': 999,}
		checkAttributes(t, d)

		if not str(t) == "-1 day, 23:58:58.999998:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))


		t = datetime.timedelta(hours=-1, minutes=-1, seconds=-1, microseconds=-1)
		if not str(t) == "-1 day, 22:58:58.999999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))
		d = {'days': -1, 'seconds': 82738, 'microseconds': 999999}
		checkAttributes(t, d)

		t = nanotime.timedelta(hours=-1, minutes=-1, seconds=-1, microseconds=-1)
		d = {'days': -1, 'seconds': 82738, 'microseconds': 999999, 'nanoseconds': 0,}
		checkAttributes(t, d)

		if not str(t) == "-1 day, 22:58:58.999999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))
		
		t = nanotime.timedelta(hours=-1, minutes=-1, seconds=-1, microseconds=-1, nanoseconds=-1)
		d = {'days': -1, 'seconds': 82738, 'microseconds': 999998, 'nanoseconds': 999,}
		checkAttributes(t, d)

		if not str(t) == "-1 day, 22:58:58.999998:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))
		

		t = nanotime.timedelta(days=-1, hours=-1, minutes=-1, seconds=-1, microseconds=-1, nanoseconds=-1)
		d = {'days': -2, 'seconds': 82738, 'microseconds': 999998, 'nanoseconds': 999,}
		checkAttributes(t, d)

		if not str(t) == "-2 days, 22:58:58.999998:999":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

	def testNanoTimeDeltaSub(self):
		t = datetime.timedelta(seconds=1)
		if not str(t) == "0:00:01":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))
		d = {'days': 0, 'seconds': 1, 'microseconds': 0}
		checkAttributes(t, d)
		t0 = nanotime.nanotime(1973,10,1,0,0,0,0,0)
		t2 = t0 - t
		if not str(t2) == "1973-9-30 23:59:59.000000:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t2))
		if not isinstance(t2, nanotime.nanotime):
			assert False, "Incorrect Instance type: '{0}' {1}".format(str(t2), t2.__class__.__name__)
		
		t = nanotime.timedelta(seconds=1)
		if not str(t) == "0:00:01":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t))
		d = {'days': 0, 'seconds': 1, 'microseconds': 0}
		checkAttributes(t, d)
		t0 = nanotime.nanotime(1973,10,1,0,0,0,0,0)
		t2 = t0 - t
		if not str(t2) == "1973-9-30 23:59:59.000000:000":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t2))
		if not isinstance(t2, nanotime.nanotime):
			assert False, "Incorrect Instance type: '{0}' {1}".format(str(t2), t2.__class__.__name__)
		
		t =  datetime.datetime(1973,1,1,0,0,0,0)
		t0 = datetime.datetime(1973,10,1,0,0,0,0)
		t2 = t0 - t
		if not str(t2) == "273 days, 0:00:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t2))
		if not isinstance(t2, datetime.timedelta):
			assert False, "Incorrect Instance type: '{0}' {1}".format(str(t2), t2.__class__.__name__)


		t =  datetime.datetime(1973,1,1,0,0,0,0)
		t0 = nanotime.nanotime(1973,10,1,0,0,0,0,0)
		t2 = t0 - t
		if not str(t2) == "273 days, 0:00:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t2))
		if not isinstance(t2, nanotime.timedelta):
			assert False, "Incorrect Instance type: '{0}' {1}".format(str(t2), t2.__class__.__name__)

		t =  nanotime.nanotime(1973,1,1,0,0,0,0,0)
		t2 = t0 - t
		if not str(t2) == "273 days, 0:00:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t2))
		if not isinstance(t2, nanotime.timedelta):
			assert False, "Incorrect Instance type: '{0}' {1}".format(str(t2), t2.__class__.__name__)

		t =  nanotime.nanotime(1973,1,1,0,0,0,0,0)
		t0 = datetime.datetime(1973,10,1,0,0,0,0)
		t2 = t0 - t
		if not str(t2) == "273 days, 0:00:00":
				assert False, "Incorrect Time Formatting: '{0}'".format(str(t2))
		if not isinstance(t2, datetime.timedelta):
			assert False, "Incorrect Instance type: '{0}' {1}".format(str(t2), t2.__class__.__name__)
