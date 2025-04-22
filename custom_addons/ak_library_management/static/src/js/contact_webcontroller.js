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
        window['location']['href'] = '/contacts/' + contactSlug;
     },
});

publicWidget.registry.ContactSavePage = publicWidget.Widget.extend({
    selector: "#contact_form",
    events: {
        'click .btn-save': '_onSaveClick',
        'click .btn-edit': '_onEditClick'
    },
    _onSaveClick: function(event){
        event.preventDefault()
        var form_data = {
            "email": $('#InputEmail').val(),
            "name": $('#InputName').val(),
            "contact_address": $('#InputAddress').val(),
            "website": $('#InputWebsite').val(),
            "phone": $('#InputPhone').val(),
        }
        var contact_id = $(event.currentTarget).data('id')
        form_data['contact_id'] = contact_id
        rpc('/contact/save',form_data).then(
            function(response){
                alert('Your data has been save successfully.')
                var form_input_tag = document.getElementById('contact_form').getElementsByTagName('input')
                for (let i=0; i<form_input_tag.length; i++){
                    form_input_tag[i].setAttribute('readonly',true)
                }
            }
        )},

    _onEditClick: function(event){
        event.preventDefault()
        var form_input_tag = document.getElementById('contact_form').getElementsByTagName('input')
        for (let i=0; i<form_input_tag.length; i++){
               form_input_tag[i].removeAttribute('readonly')
        }
    }
});
