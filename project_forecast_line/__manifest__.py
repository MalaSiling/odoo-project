# Copyright 2022 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Project Forecast Lines",
    "summary": "Project Forecast Lines",
    "version": "14.0.1.0.3",
    "author": "Camptocamp SA, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Project",
    "website": "https://github.com/OCA/project",
    "depends": ["sale_timesheet", "sale_project", "hr_holidays", "project_status"],
    "data": [
        "security/forecast_line_security.xml",
        "security/ir.model.access.csv",
        "views/sale_order_views.xml",
        "views/hr_employee_views.xml",
        "views/forecast_line_views.xml",
        "views/forecast_role_views.xml",
        "views/product_views.xml",
        "views/project_task_views.xml",
        "views/project_status_views.xml",
        "views/res_config_settings_views.xml",
        "data/ir_cron.xml",
        "data/project_status.xml",
    ],
    "demo": [
        "demo/res_users.xml",
        "demo/forecast_role.xml",
        "demo/hr_job.xml",
        "demo/hr_employee.xml",
        "demo/product.xml",
        "demo/project.xml",
        "demo/sale.xml",
    ],
    "installable": True,
    "development_status": "Alpha",
    "application": True,
}
