// Copyright (c) 2020, nana and contributors
// For license information, please see license.txt

frappe.ui.form.on('Books', {
	refresh: function(frm) {
		frm.add_custom_button(__('Borrow'), function () {
			// alert('test');
			borrowRequest(frm);
		});
	}
});


function borrowRequest(frm) {
    frappe.call({
        method: 'nanalib.nanalib.doctype.books.books.borrow_request',
        args: {
            id: frm.docname
        },
        callback: function (msg) {
            frappe.msgprint(__(msg));
            frm.refresh();
            frm.reload_doc();
            frm.reload()
        }
    });
}

