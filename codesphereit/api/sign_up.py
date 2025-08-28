import frappe
from frappe.utils import random_string
from frappe.auth import LoginManager

@frappe.whitelist(allow_guest=True)
def signup(email, full_name=None):
    if frappe.db.exists("User", email):
        frappe.throw("Email already registered")

    user = frappe.get_doc({
        "doctype": "User",
        "email": email,
        "first_name": full_name or email.split("@")[0],
        "enabled": 1,
        "new_password": random_string(10)
    })
    user.flags.ignore_permissions = True
    user.insert()

    return {"message": "Signup successful."}
