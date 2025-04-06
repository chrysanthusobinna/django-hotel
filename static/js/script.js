$('.carousel').carousel({ interval: 4000 });


 // toggle to close nav
    $(document).ready(function () {
        $(document).click(function (event) {
            var clickOver = $(event.target);
            var _opened = $("#mainNavbar").hasClass("show");
            if (_opened && !clickOver.closest('.navbar').length) {
                $(".navbar-toggler").click();  
            }
        });
    });
 
