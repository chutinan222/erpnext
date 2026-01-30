# Copyright (c) 2026, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ArticleAuthor(Document):
# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING, Literal

	if TYPE_CHECKING:

		full_teacher_name: str | None
		parent: str
		parentfield: str
		parenttype: str
		teacher_id: str | None
		teacher_name: str | None
	# end: auto-generated types
	pass
