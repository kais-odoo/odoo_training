from email.policy import default
from odoo import models, fields,api
import datetime
from odoo.exceptions import ValidationError,UserError

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'estate_property_offer'
    _rec_name = 'property_id'

    price = fields.Float()
    status = fields.Selection([('accepted','Accepted'),('refuse','Refuse')])
    partner_id = fields.Many2one('res.partner')
    property_id = fields.Many2one('estate.property')
    offer_date = fields.Date(related='property_id.date_availability', readonly=False)
    validity = fields.Integer(default=7)
    deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline", search="_search_date_deadline")


    def action_refused(self):
        for record in self:
            if record.status == 'accepted':
                raise UserError("Accepted offer can't be Refuse")
            record.status = 'refuse'

    def action_accepted(self):
        for record in self:
            if record.status == 'refuse':
                raise UserError("Refused offer can't be Accept")
            record.status = 'accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id


    


    @api.depends('validity','offer_date')
    def _compute_date_deadline(self):
        for record in self:
            record.deadline = fields.Date.add(record.offer_date, days=record.validity)

    @api.onchange('deadline')
    def _inverse_date_deadline(self):
        for record in self:
            diff = record.deadline - record.offer_date
            record.validity = diff.days



    def _search_date_deadline(self,operator,value):
        self.env.cr.execute(
            "SELECT id from estate_property_offer where deadline %s %s"% (operator,value))
        ids = self.env.cr.fetchall()
        return [('id','in',[id[0] for id in ids])]    

    
    


    @api.constrains('offer_date','validity')
    def _check_date_end(self):
        for record in self:
            if record.offer_date > record.deadline or record.validity < 0:
                raise ValidationError("Offer date can't be greater-than deadline date")
                
    



class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'estate_property_tag'


    name = fields.Char()
    color=fields.Integer()



class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'property_type'

    name = fields.Char(string='Property Type', required=True)
    property_ids = fields.One2many('estate.property', 'property_type_id')
    


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property"


    def _get_description(self):
        if self.env.context.get('is_my_property'):
            return self.env.user.name + "'s Property"
 
    ref_seq = fields.Char(string="Reference ID",default="New")

    name = fields.Char(string="Title", default="Unknown", required=True)
    description = fields.Text(default=_get_description)
    postcode = fields.Char()
    date_availability = fields.Date(default=lambda self: fields.Datetime.now(), copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False, readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(required=True)
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ("north", "North"),
        ("south", "South"),
        ("east", "East"),
        ("west", "West")
    ])
    active = fields.Boolean(default=True)
    property_type_id = fields.Many2one('estate.property.type')
    image = fields.Image()
    state = fields.Selection([('new', 'New'), ('sold', 'Sold'), ('cancel', 'Cancelled')], default='new')
    salesman_id = fields.Many2one('res.users',default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner')
    property_tag_ids = fields.Many2many('estate.property.tag')
    property_offer_ids = fields.One2many('estate.property.offer','property_id')
    total_area = fields.Integer(compute="_compute_area" ,store=True)
    best_price = fields.Integer(compute="_compute_best_price")
    partner_name = fields.Many2one('res.partner','partner name', default=lambda self: self.env.user.partner_id.id,readonly=True)


    

    @api.depends('garden_area','living_area')
    def _compute_area(self):
        for record in self:
           record.total_area = record.living_area + record.garden_area



    @api.depends('property_offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            max_price = 0
            for offer in record.property_offer_ids:
                if offer.price > max_price:
                    max_price = offer.price
            record.best_price = max_price
            

    @api.onchange('garden')
    def _onchange_garden(self):
        for record in self:

            if record.garden:
                record.garden_area = 10
                record.garden_orientation = "north"
            else:
                record.garden_area = 0
                record.garden_orientation= None


    # Methods for button actions
    def action_sold(self):
        for record in self:
            if record.state=='cancel':
                raise UserError("Cancel Property cannot be sold")
            record.state = 'sold'
    

    def action_cancel(self):
        for record in self:
            if record.state=='sold':
                raise UserError("Sold Property cannot be canceled")
            record.state = 'cancel'


    def _get_description(self):
        if self.env.context.get('is_my_property'):
            return self.env.user.name + '\'s Property'