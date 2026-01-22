# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ArticleSubmission(Document):
# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING, Literal

	if TYPE_CHECKING:
		from erpnext.projects.doctype.article_author.article_author import ArticleAuthor
		from erpnext.projects.doctype.attached_professor.attached_professor import AttachedProfessor
		article_file: str | None
		article_title: str
		date_paper: str | None
		is_scopus: Literal["วารสารอยู่ใน Scopus หรือไม่", "Scopus", "Non Scopus"]
		professor: list[ArticleAuthor]
		professor_attach_paper: list[AttachedProfessor]
		related_project: str | None
	# end: auto-generated types
	pass
