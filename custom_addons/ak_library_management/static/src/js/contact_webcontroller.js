/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";


publicWidget.registry.ContactControllerPage = publicWidget.Widget.extend({
     selector: ".contacts_page",
     events: {
            'click .contact-card': '_onContactClick'
        },

     _onContactClick: function(event){
        let contactSlug = $(event.currentTarget).data('contact-slug');
        window.location.href = '/contacts/' + contactSlug;
     },

});
