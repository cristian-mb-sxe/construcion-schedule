# -*- coding: utf-8 -*-
# from odoo import http


# class BetterNotes(http.Controller):
#     @http.route('/better_notes/better_notes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/better_notes/better_notes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('better_notes.listing', {
#             'root': '/better_notes/better_notes',
#             'objects': http.request.env['better_notes.better_notes'].search([]),
#         })

#     @http.route('/better_notes/better_notes/objects/<model("better_notes.better_notes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('better_notes.object', {
#             'object': obj
#         })
