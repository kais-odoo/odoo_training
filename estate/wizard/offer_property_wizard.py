from odoo import api, fields, models, _

class property_wizard(models.TransientModel):
    _name = "property.wizard"
    _description = "offer wizard"

    price = fields.Char()
    status = fields.Selection([('accepted','Accepted'),('refuse','Refuse')])
    partner_id = fields.Many2one('res.partner', 'Name', required=True)


    def action_add_offer(self):
        self.ensure_one()
        activeIds = self.env.context.get('active_ids')
        Offer = self.env['estate.property.offer']
        data = {
            'price' : self.price,
            'status' : self.status,
            'partner_id' : self.partner_id.id
        }
        for property in self.env['estate.property'].browse(activeIds):
            ## Method 1
            # data['property_id'] = property.id
            # Offer.create(data)

            # Method 2
            property.write({'property_offer_ids' : [(0,0,data)]})
            ##                                       t,i
            ## here t -> create,write,link,delete,...etc
            ## here i -> id (id to perform operation)

        return True
        # Method 3
        # for x in activeIds:
        #     self.env['estate.property.offer'].create({'status':self.status,'price':self.price ,'partner_id': self.partner_id.id,'property_id':x})
        # return True