# -*- coding: utf-8 -*-
# from odoo import http


# class InventSolutionTaskOdoo15(http.Controller):
#     @http.route('/invent_solution_task_odoo15/invent_solution_task_odoo15/', auth='public')
#     d# -*- coding: utf-8 -*-
# from odoo import http


# class InventSolutionTaskOdoo15(http.Controller):
#     @http.route('/invent_solution_task_odoo15/invent_solution_task_odoo15/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invent_solution_task_odoo15/invent_solution_task_odoo15/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invent_solution_task_odoo15.listing', {
#             'root': '/invent_solution_task_odoo15/invent_solution_task_odoo15',
#             'objects': http.request.env['invent_solution_task_odoo15.invent_solution_task_odoo15'].search([]),
#         })

#     @http.route('/invent_solution_task_odoo15/invent_solution_task_odoo15/objects/<model("invent_solution_task_odoo15.invent_solution_task_odoo15"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invent_solution_task_odoo15.object', {
#             'object': obj
#         })
