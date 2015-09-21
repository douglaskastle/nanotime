# -*- coding: utf-8 -*-
import datetime
import unittest
import nanotime.nanotime as nanotime
from nanotime.tests.utils import checkAttributes

class TestNanotime(unittest.TestCase):

    def testNanotimeError(self):
        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        
        d['nanosecond'] = 1
        t = t.replace(nanosecond=1)
        checkAttributes(t, d)
        d['microsecond'] = 1
        t = t.replace(microsecond=1)
        checkAttributes(t, d)
        d['second'] = 1
        t = t.replace(second=1)
        checkAttributes(t, d)
        d['minute'] = 1
        t = t.replace(minute=1)
        checkAttributes(t, d)
        d['hour'] = 1
        t = t.replace(hour=1)
        checkAttributes(t, d)
        d['day'] = 1
        t = t.replace(day=1)
        checkAttributes(t, d)
        d['month'] = 1
        t = t.replace(month=1)
        checkAttributes(t, d)
        d['year'] = 1970
        t = t.replace(year=1970)
        checkAttributes(t, d)
        
        self.assertRaises(NameError, t.replace, tree=1)
        self.assertRaises(NameError, t.replace, nanoseconds=1)
        
        self.assertRaises(ValueError, t.replace, microsecond=10000000)
        self.assertRaises(ValueError, t.replace, second=61)
        self.assertRaises(ValueError, t.replace, minute=61)
        self.assertRaises(ValueError, t.replace, hour=24)
        self.assertRaises(ValueError, t.replace, day=32)
        self.assertRaises(ValueError, t.replace, month=13)

        self.assertRaises(TypeError, t.__sub__, 1)
        self.assertRaises(TypeError, t.__add__, 1)
        self.assertRaises(TypeError, t.__add__, t)
        self.assertRaises(TypeError, t.__add__, datetime.datetime.now())

        t = t.replace(nanosecond=999)
        self.assertRaises(ValueError, t.replace, nanosecond=1000)
        self.assertRaises(ValueError, t.replace, nanosecond=1001)
    
    
    def testNanotimeDatetime(self):
        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t + datetime.timedelta(days=1)
        d['day'] = 13
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-13 16:24:34.123456:000":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        tn = t - datetime.timedelta(days=1)
        d['day'] = 11
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-11 16:24:34.123456:000":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))
        

    def testNanotimeAddition(self):
        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t + nanotime.timedelta(days=1)
        d['day'] = 13
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-13 16:24:34.123456:000":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t + nanotime.timedelta(hours=1)
        d['hour'] = 17
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 17:24:34.123456:000":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t + nanotime.timedelta(minutes=1)
        d['minute'] = 25
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:25:34.123456:000":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t + nanotime.timedelta(seconds=1)
        d['second'] = 35
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:35.123456:000":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))


        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t + nanotime.timedelta(microseconds=1)
        d['microsecond'] = 123457
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:34.123457:000":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))


        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t + nanotime.timedelta(nanoseconds=1)
        d['nanosecond'] = 1
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:34.123456:001":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t + nanotime.timedelta(nanoseconds=999)
        d['nanosecond'] = 999
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:34.123456:999":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t + nanotime.timedelta(nanoseconds=1000)
        d['nanosecond'] = 0
        d['microsecond'] = 123457
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:34.123457:000":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t + nanotime.timedelta(nanoseconds=1001)
        d['nanosecond'] = 1
        d['microsecond'] = 123457
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:34.123457:001":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 999999, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t + nanotime.timedelta(nanoseconds=1001)
        d['nanosecond'] = 1
        d['microsecond'] = 0
        d['second'] = 35
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:35.000000:001":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 1,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'], d['nanosecond'])
        checkAttributes(t, d)
        tn = t + nanotime.timedelta(nanoseconds=1)
        d['nanosecond'] = 2
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:34.123456:002":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 501,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'], d['nanosecond'])
        checkAttributes(t, d)
        tn = t + nanotime.timedelta(nanoseconds=501)
        d['nanosecond'] = 2
        d['microsecond'] = 123457
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:34.123457:002":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 1,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'], nanosecond=d['nanosecond'])
        checkAttributes(t, d)
        tn = t + nanotime.timedelta(nanoseconds=1)
        d['nanosecond'] = 2
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:34.123456:002":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 501,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'], nanosecond=d['nanosecond'])
        checkAttributes(t, d)
        tn = t + nanotime.timedelta(nanoseconds=501)
        d['nanosecond'] = 2
        d['microsecond'] = 123457
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:34.123457:002":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

    def testNanotimeSubtraction(self):
        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(days=1)
        d['day'] = 11
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-11 16:24:34.123456:000":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(hours=1)
        d['hour'] = 15
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 15:24:34.123456:000":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(minutes=1)
        d['minute'] = 23
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:23:34.123456:000":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(seconds=1)
        d['second'] = 33
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:33.123456:000":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))


        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(microseconds=1)
        d['microsecond'] = 123455
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:34.123455:000":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))


        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 54,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(nanoseconds=1)
        d['nanosecond'] = 53
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:34.123456:053":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(nanoseconds=1)
        d['nanosecond'] = 999
        d['microsecond'] = 123455
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:34.123455:999":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 0, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(nanoseconds=1)
        d['nanosecond'] = 999
        d['microsecond'] = 999999
        d['second'] = 33
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:24:33.999999:999":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 0, 'microsecond': 0, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(nanoseconds=1)
        d['nanosecond'] = 999
        d['microsecond'] = 999999
        d['second'] = 59
        d['minute'] = 23
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 16:23:59.999999:999":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(nanoseconds=1)
        d['nanosecond'] = 999
        d['microsecond'] = 999999
        d['second'] = 59
        d['minute'] = 59
        d['hour'] = 15
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-12 15:59:59.999999:999":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(nanoseconds=1)
        d['nanosecond'] = 999
        d['microsecond'] = 999999
        d['second'] = 59
        d['minute'] = 59
        d['hour'] = 23
        d['day'] = 11
        checkAttributes(tn, d)
        if not str(tn) == "1972-11-11 23:59:59.999999:999":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 11 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(nanoseconds=1)
        d['nanosecond'] = 999
        d['microsecond'] = 999999
        d['second'] = 59
        d['minute'] = 59
        d['hour'] = 23
        d['day'] = 31
        d['month'] = 10
        checkAttributes(tn, d)
        if not str(tn) == "1972-10-31 23:59:59.999999:999":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(nanoseconds=1)
        d['nanosecond'] = 999
        d['microsecond'] = 999999
        d['second'] = 59
        d['minute'] = 59
        d['hour'] = 23
        d['day'] = 31
        d['month'] = 12
        d['year'] = 1971
        checkAttributes(tn, d)
        if not str(tn) == "1971-12-31 23:59:59.999999:999":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1970, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(nanoseconds=1)
        d['nanosecond'] = 999
        d['microsecond'] = 999999
        d['second'] = 59
        d['minute'] = 59
        d['hour'] = 23
        d['day'] = 31
        d['month'] = 12
        d['year'] = 1969
        checkAttributes(tn, d)
        if not str(tn) == "1969-12-31 23:59:59.999999:999":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(nanoseconds=1001)
        d['nanosecond'] = 999
        d['microsecond'] = 999998
        d['second'] = 59
        d['minute'] = 59
        d['hour'] = 23
        d['day'] = 31
        d['month'] = 12
        d['year'] = 1971
        checkAttributes(tn, d)
        if not str(tn) == "1971-12-31 23:59:59.999998:999":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

        d = {'year': 1972, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 501,}
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
        checkAttributes(t, d)
        tn = t - nanotime.timedelta(nanoseconds=1002)
        d['nanosecond'] = 499
        d['microsecond'] = 999999
        d['second'] = 59
        d['minute'] = 59
        d['hour'] = 23
        d['day'] = 31
        d['month'] = 12
        d['year'] = 1971
        checkAttributes(tn, d)
        if not str(tn) == "1971-12-31 23:59:59.999999:499":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(tn))

    def testNanotimeCreation(self):
        
        d = {'year': 2000, 'month': 1 , 'day': 1, 'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0, 'nanosecond': 0,}
        
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        
        if not str(t) == "2000-1-1 00:00:00.000000:000":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

        d = {'year': 1972, 'month': 11 , 'day': 12, 'hour': 16, 'minute': 24, 'second': 34, 'microsecond': 123456, 'nanosecond': 0}
        
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'])
        checkAttributes(t, d)
        
        if not str(t) == "1972-11-12 16:24:34.123456:000":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

        d['nanosecond'] = 235
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],d['nanosecond'])
        checkAttributes(t, d)

        if not str(t) == "1972-11-12 16:24:34.123456:235":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(t))

        d['nanosecond'] = 123
        t = nanotime.nanotime(d['year'],d['month'],d['day'],d['hour'],d['minute'],d['second'],d['microsecond'],nanosecond=d['nanosecond'])
        checkAttributes(t, d)

        if not str(t) == "1972-11-12 16:24:34.123456:123":
                assert False, "Incorrect Time Formatting: '{0}'".format(str(t))


    def testPTPnow(self):
        microsecond = 999999
        while microsecond > 499999:
            t = datetime.datetime.now()
            microsecond = t.microsecond

        d = {'year': t.year, 
             'month':  t.month, 
             'day': t.day, 
             'hour': t.hour, 
             'minute': t.minute, 
             'second': t.second, 
             'nanosecond': 0, 
            }
        
        t = nanotime.nanotime.now()
        checkAttributes(t, d)
        
