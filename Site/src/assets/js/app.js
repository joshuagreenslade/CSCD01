;
(function() {

    'use strict';


    var isMobile = {
        Android: function() {
            return navigator.userAgent.match(/Android/i);
        },
        BlackBerry: function() {
            return navigator.userAgent.match(/BlackBerry/i);
        },
        iOS: function() {
            return navigator.userAgent.match(/iPhone|iPad|iPod/i);
        },
        Opera: function() {
            return navigator.userAgent.match(/Opera Mini/i);
        },
        Windows: function() {
            return navigator.userAgent.match(/IEMobile/i);
        },
        any: function() {
            return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
        }
    };


    var fullHeight = function() {

        if (!isMobile.any()) {
            $('.js-fullheight').css('height', $(window).height());
            $(window).resize(function() {
                $('.js-fullheight').css('height', $(window).height());
            });
        }

    };


    var offcanvasMenu = function() {

        $('#page').prepend('<div id="offcanvas" />');
        $('#page').prepend('<a href="#" class="js-nav-toggle nav-toggle nav-white"><i></i></a>');
        var clone1 = $('.menu-1 > ul').clone();
        $('#offcanvas').append(clone1);
        var clone2 = $('.menu-2 > ul').clone();
        $('#offcanvas').append(clone2);

        $('#offcanvas .has-dropdown').addClass('offcanvas-has-dropdown');
        $('#offcanvas')
            .find('li')
            .removeClass('has-dropdown');

        // Hover dropdown menu on mobile
        $('.offcanvas-has-dropdown').mouseenter(function() {
            var $this = $(this);

            $this
                .addClass('active')
                .find('ul')
                .slideDown(500, 'easeOutExpo');
        }).mouseleave(function() {

            var $this = $(this);
            $this
                .removeClass('active')
                .find('ul')
                .slideUp(500, 'easeOutExpo');
        });


        $(window).resize(function() {

            if ($('body').hasClass('offcanvas')) {

                $('body').removeClass('offcanvas');
                $('.js-nav-toggle').removeClass('active');

            }
        });
    };


    var burgerMenu = function() {

        $('body').on('click', '.js-nav-toggle', function(event) {
            var $this = $(this);


            if ($('body').hasClass('overflow offcanvas')) {
                $('body').removeClass('overflow offcanvas');
            } else {
                $('body').addClass('overflow offcanvas');
            }
            $this.toggleClass('active');
            event.preventDefault();

        });
    };


    // Magnific Popup

    var imagePopup = function() {
        $('.image-popup').magnificPopup({
            type: 'image',
            removalDelay: 10,
            titleSrc: 'title',
            gallery: {
                enabled: false
            }
        });
    };


    // Window Scroll
    var windowScroll = function() {
        var lastScrollTop = 0;

        $(window).scroll(function(event) {

            var header = $('#header'),
                scrlTop = $(this).scrollTop();

            if (scrlTop > 500 && scrlTop <= 2000) {
                header.addClass('navbar-fixed-top animated slideInDown');
            } else if (scrlTop <= 500) {
                if (header.hasClass('navbar-fixed-top')) {
                    header.addClass('navbar-fixed-top animated slideOutUp');
                    setTimeout(function() {
                        header.removeClass('navbar-fixed-top animated slideInDown slideOutUp');
                    }, 100);
                }
            }

        });
    };


    // Document on load.
    $(function() {

        fullHeight();
        burgerMenu();
        imagePopup();
        offcanvasMenu();

    });


}());