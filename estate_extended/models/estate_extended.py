from odoo import models,fields,api


class Estate_Property_extended(models.Model):
    _name  = "estate.leased.property"
    _inherits = {'estate.property':'property_id'}


    property_id = fields.Many2one('estate.property')

    lease_duration = fields.Integer()
    lease_rent_monthly = fields.Float()
