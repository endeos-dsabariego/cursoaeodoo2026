from odoo import models, fields


class RRealEstateContract(models.Model):
   _name = 'realestate.contract'
   _description = 'Contract'
   
   name = fields.Char(string='Name')
   
   contract_type = fields.Selection([
      ('sale', 'Sale'),
      ('rent', 'Rent')
   ], string='Contract Type', default='rent')
   
   property_id = fields.Many2one(
      comodel_name='realestate.property', 
      string='Property',
      required=True
   )
   
   partner_id = fields.Many2one(
      comodel_name='res.partner',  
      string='Partner',
      required=True
   )
   
   start_date = fields.Date(string='Start Date')
   
   end_date = fields.Date(string='End Date')
   
   rent = fields.Float(string='Rent')
   
   deposit = fields.Float(string='Deposit')
   
   state = fields.Selection([
      ('draft', 'Draft'),
      ('in_progress', 'In Progress'),
      ('finished', 'Finished'),
      ('canceled', 'Canceled')
   ], default='draft', string='State')
   
   def action_draft(self):
      self.state = 'draft'
      
   def action_in_progress(self):
      self.state = 'in_progress'
   
   def action_finished(self):
      self.state = 'finished'
      
   def action_canceled(self):
      self.state = 'canceled'