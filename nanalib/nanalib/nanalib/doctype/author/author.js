// Copyright (c) 2020, nana and contributors
// For license information, please see license.txt

frappe.ui.form.on('Author', {
	refresh: function(frm) {
		if (frappe.user.has_role('System Manager')) {
			frm.add_custom_button(__('Test Button'), function () {
				testFunction(frm)
			});
		}
	}

});

function testFunction(frm) {
    frappe.call({
        method: 'nanalib.nanalib.doctype.author.author.test_function',
        args: {
            doc_name: frm.docname
        },
        callback: function (msg) {
            frappe.msgprint(__(msg));
            frm.refresh();
            frm.reload_doc();
            frm.reload()
        }
    });
}