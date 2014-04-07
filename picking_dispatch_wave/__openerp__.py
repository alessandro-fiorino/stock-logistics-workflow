# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Alexandre Fayolle, Romain Deheele
#    Copyright 2014 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    "name": "Picking Dispatch Wave",
    "version": "0.1",
    "depends": ['picking_dispatch'],
    "author": "Camptocamp",
    'license': 'AGPL-3',
    "description": """Allows to set a 'sale order wave' to pick
    according the number of sales that you set.
    1.The picker sets a number n of sale orders.
    2.The wizard will select moves from n oldest sales
    that are linked to ready pickings.
    3.A picking dispatch is created with found moves""",
    "website": "http://www.camptocamp.com",
    "category": "Warehouse Management",
    "demo": [],
    "data": ['dispatch_wave_view.xml'],
    "test": [],
    "installable": True,
}
