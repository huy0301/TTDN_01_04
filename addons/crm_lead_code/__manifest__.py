

{
    "name": "Sequential Code for Leads / Opportunities",
    "summary": 'Generate Leads/Opportunities based on country, industries, size, etc.',
    "category": 'Customer Relationship Management',
    "version": '1.2',
    "depends": ["crm"],
    "data": ["data/lead_sequence.xml", "views/crm_lead_view.xml"],
    "auto_install": True,
    "assets": {
        'web.assets_backend': [
            'crm_iap_mine/static/src/js/**/*',
        ],
        'web.assets_qweb': [
            'crm_iap_mine/static/src/xml/**/*',
        ],
    },
    "license": "AGPL-3",
}

