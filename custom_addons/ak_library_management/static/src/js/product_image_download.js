/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";


publicWidget.registry.ProductImage = publicWidget.Widget.extend({
     selector: "#product_detail",
     events: {
            'click #download': '_onDownloadClick'
        },

     _onDownloadClick: function(event){
        let image_ids = $(event.currentTarget).data('download');
        $.ajax({
          type: "POST",
          url: '/download_images',
          data: {'image_ids[]': image_ids},
          success: function(data){
                console.log(data)
            }
          });
     },
});