openerp.menubar_badge_number = function (instance) {
    var QWeb = instance.web.qweb;

    instance.web.Menu.include({
        on_needaction_loaded : function(){
            var self = this;
            this._super.apply(this, arguments);

            var $menu2s = this.$secondary_menus.find('.oe_secondary_menu');
            _.each($menu2s, function(menu2, idx){
                var $menu2 = $(menu2);
                var $badges = $menu2.find('.badge');
                var sum = _.reduce($badges, function(acc, item){
                    return acc + parseInt($(item).text().trim());
                }, 0);

                var menu_id = $menu2.attr('data-menu-parent');
                var $menu1 = self.$el.find('a[data-menu='+menu_id+']');
                $menu1.find('.badge').remove();
                if (sum > 0 && menu_id != '4') {
                    $menu1.append(QWeb.render("Menu.needaction_counter", {widget: {needaction_counter: sum}}));
                }
            });
        }
    })
};