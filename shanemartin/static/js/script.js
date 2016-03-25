(function($, window) {

    function goToTab(hash) {
        $('#nav-tabs a[href$="'+hash+'"]').trigger('click');
    }

    // tab switching from tab
    $('#nav-tabs a').click(function(e) {
        $(this).tab('show');
    });

    // tab switching from content panel
    $('.tab-content a[href^="#"]').click(function(e) {
        var hash = $(this).attr('href').substr();
        $('#nav-tabs a[href$="'+hash+'"]').trigger('click');
    });

    // switch to tab onload
    var hash = $.trim( window.location.hash );
    if (hash) goToTab(hash);

}).call(this, jQuery, window);
