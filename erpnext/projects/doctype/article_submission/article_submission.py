# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ArticleSubmission(Document):
# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING, Literal

	if TYPE_CHECKING:

		article_file: str | None
		article_title: str
		is_scopus: Literal["วารสารอยู่ใน Scopus หรือไม่", "Scopus", "Non Scopus"]
		professor: str | None
		task: str | None
	# end: auto-generated types
	pass
