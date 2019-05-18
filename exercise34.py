#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 18.05.19
@author: felix
"""
import abc


class CannotChargeError(BaseException):
    pass


class CannotReverseError(BaseException):
    pass


class AbstractPayment(abc.ABC):

    @abc.abstractmethod
    def authorize_payment(self, user_id, amount, currency) -> bool:
        pass

    @abc.abstractmethod
    def charge_payment(self, user_id, amount, currency, merchant_id) -> int or Exception:
        # returns a transaction ID number or raises CannotCharge
        pass

    @abc.abstractmethod
    def reverse_payment(self, user_id, amount, currency, merchant_id) -> int or Exception:
        # returns a transaction ID number or raises CannotReverse
        pass
