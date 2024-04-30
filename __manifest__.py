{
    "name": "Custom Report",
    "images": ["static/description/icon.png"],
    "summary": "Custom report adding features to sale order",
    "author": "Ismael Semmar Galvez",
    "website": "https://github.com/Ism1tha/technical-training",
    "version": "16.0.0",
    "application": True,
    'depends': ['base', 'sale'],
    "data": [ 
        "views/sale_order_report_extension.xml",
        "views/sale_order_view_extension.xml",
        "views/sale_order_custom_report.xml",
        "reports/custom_sale_report_template.xml",
    ],
    "installable": True,
    'license': 'LGPL-3',   
}
