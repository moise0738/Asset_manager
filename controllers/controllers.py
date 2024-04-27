# -*- coding: utf-8 -*-
#from odoo import http


# class AssetManager(http.Controller):
#     @http.route('/asset_manager/asset_manager', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asset_manager/asset_manager/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('asset_manager.listing', {
#             'root': '/asset_manager/asset_manager',
#             'objects': http.request.env['asset_manager.asset_manager'].search([]),
#         })

#     @http.route('/asset_manager/asset_manager/objects/<model("asset_manager.asset_manager"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asset_manager.object', {
#             'object': obj
#         })

