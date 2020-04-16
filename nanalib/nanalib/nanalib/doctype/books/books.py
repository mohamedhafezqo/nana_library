# -*- coding: utf-8 -*-
# Copyright (c) 2020, nana and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class Books(Document):
    pass


@frappe.whitelist()
def borrow_request(id):
    userId = frappe.session.user

    return {
        "data": create_transaction(id, userId, 7)
    }


def create_transaction(bookId, userId, defaultPeriod=7):
    if isBorrowedBefore(bookId, userId):
        return "Sorry, we can't borrow you the same book twice"

    transaction = frappe.get_doc({
        "doctype": "Borrowed Transactions",
        "user": userId,
        "book": bookId,
        "borrowing_date": frappe.utils.nowdate(),
        "returning_date": frappe.utils.add_days(frappe.utils.nowdate(), defaultPeriod)
    })
    transaction.insert(ignore_permissions=True)

    return transaction


def isBorrowedBefore(bookId, userId):
    return frappe.get_value('Borrowed Transactions',
                            filters={
                                'book': bookId,
                                'user': userId,
                                'returning_date': ('>', frappe.utils.nowdate())
                            }
                            )
