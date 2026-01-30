# Copyright (c) 2026, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AttachedProfessor(Document):
# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING, Literal

	if TYPE_CHECKING:

		parent: str
		parentfield: str
		parenttype: str
		professor_id: str | None
		professor_name: str | None
		related_project: str | None
	# end: auto-generated types
	pass
