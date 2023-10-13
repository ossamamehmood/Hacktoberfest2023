# Copyright (c) 2023, Raaj Tailor and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime

def execute(filters=None):
	columns = get_columns()
	data = [] 
	data = get_report(filters)
	return columns, data

def get_columns():
	return[
		{
			'fieldname': 'month',
			'label': 'Month',
			'fieldtype': 'Data',
			'width': 150
		},
		{
			'fieldname': 'nature_of_supply',
			'label': 'Nature Of Supply',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'tax_type',
			'label': 'Tax Type',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'customer_code',
			'label': 'Customer Code',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'customer',
			'label': 'Customer Name',
			'fieldtype': 'Link',
			'options': 'Customer',
			"width": 150
		},
		{
			'fieldname': 'customer_gstin',
			'label': 'Client GSTIN',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'place_of_supply',
			'label': 'Place of Supply',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'document_type',
			'label': 'Document Type',
			'fieldtype': 'Link',
			'options': 'Purchase Invoice',
			'width': 150
		},
		{
			'fieldname': 'name',
			'label': 'Document No.',
			'fieldtype': 'Link',
			'options': 'Sales Invoice',
			"width": 150
		},
		{
			'fieldname': 'posting_date',
			'label': 'Document Date',
			'fieldtype': 'Date',
			"width": 150
		},
		{
			'fieldname': 'gst_hsn_code',
			'label': 'HSN',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'item_name',
			'label': 'Description of Supply',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'qty',
			'label': 'Quantity',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'rate',
			'label': 'Rate',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'amount',
			'label': 'Invoice Value',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'item_tax_template',
			'label': 'Rate of GST',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'igst_rate',
			'label': 'IGST Rate',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'cgst_rate',
			'label': 'CGST Rate',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'sgst_rate',
			'label': 'SGST Rate',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'igst_amount',
			'label': 'IGST',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'cgst_amount',
			'label': 'CGST',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'sgst_amount',
			'label': 'SGST',
			'fieldtype': 'Data',
			"width": 150
		},
		{
			'fieldname': 'total_taxes_and_charges',
			'label': 'Total GST',
			'fieldtype': 'Data',
			"width": 150
		}
	]     

def get_report(filters):
	conditions = get_condition(filters)
	query = """select si.name,
			si.posting_date as 'month',
			si.posting_date,
			si.customer_code,
			si.customer,
			si.customer_gstin,
			si.company_gstin,
			si.place_of_supply,
			si.nature_of_supply,
			si.document_type,
			sii.gst_hsn_code,
			sii.item_name,
			sii.item_code, 
			sii.qty, 
			sii.rate, 
			sii.amount,
			sii.item_tax_template, 
			stc.account_head, 
			stc.rate as gst_rate,
			stc.tax_amount,
			si.total_taxes_and_charges,
			(CASE WHEN stc.account_head LIKE %(cgst)s THEN 'CGST' WHEN stc.account_head LIKE %(sgst)s THEN 'SGST' ELSE 'IGST' END) AS 'gst'			 
		from `tabSales Invoice` as si
		inner join `tabSales Invoice Item` sii on sii.parent=si.name 
		inner join `tabSales Taxes and Charges` stc on stc.parent=si.name
		where si.docstatus = 1 and si.is_return = 0 {0} """.format(conditions) 
	parameters = {
    'cgst': '%CGST%',
    'sgst': '%SGST%',
	'filters': filters}
	data = frappe.db.sql(query, parameters, as_dict=True)
	
	data1 =  [d for d in data if d.get('gst') in ['CGST', 'IGST']]
	for i in data1:
		i.month = i.month.strftime('%b-%Y')
		if i.gst == 'CGST':	
			i['cgst_amount'] = i.tax_amount 
			i['sgst_amount'] = i.tax_amount
			i['cgst_rate'] = i.gst_rate
			i['sgst_rate'] = i.gst_rate		
		elif i.gst == 'IGST':
			i['igst_amount'] = i.tax_amount 
			i['igst_rate'] = i.gst_rate
			i['cgst_amount'] = ''
			i['sgst_amount'] = ''
			i['cgst_rate'] = ''
			i['sgst_rate'] = ''
		if i.company_gstin and i.customer_gstin and i.company_gstin[0:2] == i.customer_gstin[0:2]:
			i['tax_type'] = 'Intra'
		elif i.company_gstin and i.customer_gstin and i.company_gstin[0:2] != i.customer_gstin[0:2]:
			i['tax_type'] = 'Inter'
		else:
			i['tax_type'] = ''

	return data1

def get_condition(filters=None):
	conditions = ''
	if filters.get('item_name'):
		conditions += " and sii.item_code = '{0}'".format(filters.get('item_name'))
	if filters.get("from_date"):
		conditions += " and si.posting_date>= '{0}' ".format(filters.get('from_date'))
	if filters.get("to_date"): 
		conditions += " and date(si.posting_date)<='{0}' ".format(filters.get('to_date'))
	if filters.get('customer'):
		conditions += " and si.customer = '{0}'".format(filters.get('customer'))
	return conditions
