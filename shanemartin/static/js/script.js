(function($, window) {

    // tab switching
    $('#nav-tabs a').click(function(e) {
        // e.preventDefault();
        $(this).tab('show');
    });

    // switch to tab onload
    var hash = $.trim( window.location.hash );
    if (hash) $('#nav-tabs a[href$="'+hash+'"]').trigger('click');

}).call(this, jQuery, window);
