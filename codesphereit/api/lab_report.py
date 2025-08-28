import frappe
from frappe import _

@frappe.whitelist()
def get_test_name_data():
    records = frappe.get_all("Test Name", fields=["name", "health_assessment_center", "health_assessment_name"])
    
    for rec in records:
        doc = frappe.get_doc("Test Name", rec["name"])
        rec["test_components"] = [
            {
                "test_component_name": row.test_component_name,
                "normal_range": row.normal_range,
                "unit": row.unit
            }
            for row in doc.test_component
        ]

    return records
