import frappe

@frappe.whitelist(allow_guest=True)
def get_website_content():
    website_contents = frappe.db.get_all("Website Content", fields=["*"])

    for wc in website_contents:
        wc["services"] = frappe.db.get_all(
            "Services Item",
            filters={"parent": wc.name, "parentfield": "services"},
            fields=["*"]
        )
        wc["why_choose_us"] = frappe.db.get_all(
            "Why Choose Us Item",
            filters={"parent": wc.name, "parentfield": "why_choose_us"},
            fields=["*"]
        )
        wc["carousel_image"] = frappe.db.get_all(
            "Carousel  Item",  # Keep double space as returned
            filters={"parent": wc.name, "parentfield": "carousel_image"},
            fields=["*"]
        )

    return website_contents
