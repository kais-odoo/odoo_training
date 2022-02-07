from odoo import http
from odoo.http import request

class Estate_Property_Controller(http.Controller):

    # @http.route('/hello', auth="public")
    # def hello(self, **kw):
    #     return "hello world"


    # @http.route('/hello_user', auth="user")
    # def hello_user(self, **kw):
    #     return "Hello %s" %(request.env.user.name)



    # @http.route('/hello_template')
    # def hello_template(self, **kw):
    #     return request.render('estate.hello_world')


    # @http.route('/hello_template_user')
    # def hello_template_user(self, **kw):
    #     properties = request.env['estate.property'].search([('state', '=', 'new')])
    #     print ("Properties ::: ", properties)
    #     return request.render('estate.properties_list', { 'user': request.env.user, 'properties': properties })



    @http.route('/estate',website=True,auth='public')
    def estate_porperty_show(self,**kw):
        # return "property page"

        properties = request.env['estate.property'].search([])
        return request.render("estate.property_call",{

                'properties':properties,



        }) 


    @http.route(['/estate/<model("estate.property"):property>'], auth="public", website=True)
    def property_details(self, property=False, **kw):
        # properties = request.env['estate.property'].search([])
        if property:
            return request.render('estate.property_details', {
                'properties':property,
            })