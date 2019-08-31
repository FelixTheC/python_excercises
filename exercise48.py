#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 24.08.19
@author: felix
"""
from typing import Optional

from arrow import Arrow


class Loan:
    _total_loan = 0
    _year = 1

    def __init__(self, loan: int, interest: float, starts_on: Optional[Arrow]=None):
        self.loan = loan
        self.interest = 1 + (interest / 100)
        if starts_on is not None:
            self.starts_on = starts_on
        else:
            self.starts_on = Arrow.utcnow()

    def total_on(self, end_date: Arrow):
        total_years = len(list(Arrow.span_range('year', self.starts_on, end_date))) - 1
        self._total_loan = (self.loan * self.interest) * total_years
        return self._total_loan

    def total_on_each(self, starts_on: Arrow, ends_on: Arrow):
        for i, v in enumerate(list(Arrow.span_range('year', starts_on, ends_on)), 1):
            yield (self.loan * self.interest) * i, v[-1]
