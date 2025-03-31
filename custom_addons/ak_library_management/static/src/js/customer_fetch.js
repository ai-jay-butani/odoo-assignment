/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";


publicWidget.registry.CustomerPage = publicWidget.Widget.extend({
     selector: '.customers_page',
     events: {
            'change #InputEmail': '_onEmailChange'
        },

     _onEmailChange: function(ev){
        var email = $('#InputEmail').val()
        rpc("/customer/email",{'email':email}).then(
            function(data){
                $('#InputName').val(data.name);
                $('#InputAddress').val(data.address);
                $('#InputPhone').val(data.phone);
            });
     },
});