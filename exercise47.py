#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 13.08.19
@author: felix
"""
from collections import namedtuple
from datetime import datetime, timedelta

Meeting = namedtuple('Meeting', ['start_date', 'end_date'])


class MeetingRoomTakenException(Exception):
    pass


class MeetingRoom:

    def __init__(self, room_name: str):
        self.room_name = room_name
        self.meetings = []

    def _is_meeting_room_free(self, nm: Meeting) -> bool:
        return not any((nm.start_date <= om.end_date) or (nm.end_date <= om.end_date) for om in self.meetings)

    def add_meeting(self, meeting_date: str, duration: int) -> None:
        """
        :param meeting_date: must in the format 2019-May-01 10:00:00
        :param duration: in full hours
        :exception: MeetingRoomTakenException
        :return: None
        """
        start_date = datetime.strptime(meeting_date, '%Y-%b-%d %H:%M:%S')
        end_date = start_date + timedelta(hours=duration)
        new_meeting = Meeting(start_date, end_date)
        if self._is_meeting_room_free(new_meeting):
            self.meetings.append(new_meeting)
        else:
            raise MeetingRoomTakenException()
