from odoo import http
from odoo.http import request, route

class OwlPlayground(http.Controller):
    @http.route(['/awesome_owl'], type='http', auth='public')
    def show_playground(self):
        """
        Renders the owl playground page
        """
        response = {
            'title': 'Owl Playground',
            'description': 'This is the playground page for Owl',
        }
        return response
