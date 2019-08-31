#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 13.08.19
@author: Reuven M. Lerner
"""

import pytest
from exercise47 import MeetingRoom, MeetingRoomTakenException


def test_simple():
    mr1 = MeetingRoom('Meeting Room 1')
    mr1.add_meeting('2018-May-07 10:00:00', 2)
    mr1.add_meeting('2018-May-07 13:00:00', 3)

    with pytest.raises(MeetingRoomTakenException):
        mr1.add_meeting('2018-May-07 11:00:00', 2)

    with pytest.raises(MeetingRoomTakenException):
        mr1.add_meeting('2018-May-07 09:00:00', 2)

    with pytest.raises(MeetingRoomTakenException):
        mr1.add_meeting('2018-May-08 15:00:00', 2)
