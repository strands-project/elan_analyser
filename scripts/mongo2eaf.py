#! /usr/bin/env python

from pympi import Eaf
import rospy
from mongodb_store import message_store

if __name__ == '__main__':
    rospy.init_node('mongo2eaf')
    m = message_store.MessageStoreProxy(collection='people_perception')
    q = m.query('bayes_people_tracker_logging/Logging')
    eaf = Eaf()
    eaf.add_linked_file('/home/cdondrup/matlab/toolbox/matlab/audiovideo/xylophone.mpg')
    eaf.add_tier("test tier")
    times = [e.header.stamp.secs for (e, m) in q]
    min_time = min(times)
    for (e, m) in q:
        ts = e.header.stamp.secs - min_time
        eaf.add_annotation("test tier", ts, ts+1000, str(e))
    eaf.to_file("output.eaf")