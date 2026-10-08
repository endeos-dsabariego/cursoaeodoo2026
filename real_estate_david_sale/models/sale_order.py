from odoo import models, fields, api


class SaleOrder(models.Model):
   _inherit = 'sale.order'
   
   contract_id = fields.Many2one('realestate.contract', string='Contract')
   
   def action_confirm(self):
      res = super().action_confirm()
      
      for order in self:
         if order.contract_id:
            continue
         
         rental_line = order.order_line.filtered(lambda l: l.product_id.is_rental)[:1]
         if not rental_line:
            continue
         
         contract = self.env['realestate.contract'].create({
            'partner_id': order.partner_id.id,
            'product_id': rental_line.product_id.id,
            'rent': rental_line.price_unit,
            'contract_type': 'rent',
            'state': 'draft',
         })
         
         order.contract_id = contract.id
      return res  
         