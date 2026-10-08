from odoo import models, fields


class ProductTemplate(models.Model):
   _inherit = 'product.template'
   _description = 'Product Template'
   
   is_rental = fields.Boolean(string='Is Rental', help='Indicates if the product is a rental property.')
   