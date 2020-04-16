# -*- coding: utf-8 -*-
# Copyright (c) 2020, nana and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class Author(Document):
    pass


@frappe.whitelist()
def test_function(doc_name):
    author = frappe.get_doc('Author', doc_name)

    author.age = 23
    author.save(ignore_permissions = True)

    return doc_name
