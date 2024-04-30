from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_email = fields.Char(string='Adreça de correu preferencial del client')
    num_articles = fields.Integer(string='Nombre d\'articles', compute='_compute_num_articles')

    commercial_name = fields.Char(string='Commercial Name', related='user_id.name')
    state_count = fields.Integer(string='State Count', compute='_compute_state_count')
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount')

    def _compute_num_articles(self):
        for order in self:
            order.num_articles = len(order.order_line)

    @api.depends('commercial_name', 'state')
    def _compute_state_count(self):
        for order in self:
            order.state_count = self.search_count([('user_id', '=', order.user_id.id), ('state', '=', order.state)])

    @api.depends('commercial_name', 'state')
    def _compute_total_amount(self):
        for order in self:
            orders = self.search([('user_id', '=', order.user_id.id), ('state', '=', order.state)])
            order.total_amount = sum(orders.mapped('amount_total'))