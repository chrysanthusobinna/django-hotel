$('.carousel').carousel({
    interval: 4000
});

$(document).ready(function () {
    // Toggle to close nav
    $(document).click(function (event) {
        var clickOver = $(event.target);
        var _opened = $("#mainNavbar").hasClass("show");
        if (_opened && !clickOver.closest('.navbar').length) {
            $(".navbar-toggler").click();
        }
    });

    // Delete Room Category Image
    $('.delete-image-btn').click(function () {
        var deleteUrl = $(this).data('action');
        $('#deleteImageForm').attr('action', deleteUrl);
    });
});
