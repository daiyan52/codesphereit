import frappe
from frappe.model.naming import getseries

def set_custom_name(doc, method):
    if not doc.get("customer"):
        frappe.throw("Customer is required to generate the name.")

    digits = 4
    prefix = "DN-"

    n = getseries(prefix, digits)           # atomic, transactional
    num = str(n).zfill(digits)
    cust = (doc.customer or "").strip()

    doc.name = f"{prefix}{num}-{cust}-{num}"
