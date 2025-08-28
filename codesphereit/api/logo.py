import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_website_logo():
    data = frappe.db.get_all('Website Content', fields=["logo"])
    return {"logo": data[0]["logo"] if data else None}
