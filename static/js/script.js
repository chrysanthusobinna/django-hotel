
$(document).ready(function () {
    // Toggle to close nav
    $(document).click(function (event) {
        var clickOver = $(event.target);
        var _opened = $("#mainNavbar").hasClass("show");
        if (_opened && !clickOver.closest('.navbar').length) {
            $(".navbar-toggler").click();
        }
    });
});
