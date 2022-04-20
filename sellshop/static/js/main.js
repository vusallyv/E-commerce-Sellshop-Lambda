(function($) {
        "use strict";
        // jQuery MeanMenu
        jQuery('nav#dropdown').meanmenu();
        //menu a active jquery
        var pgurl = window.location.href.substr(window.location.href
            .lastIndexOf("/") + 1);
        $("ul li a").each(function() {
                if ($(this).attr("href") == pgurl || $(this).attr("href") == '')
                    $(this).addClass("active");
                $('header ul li ul li a.active').parent('li').addClass('parent-li');
                $('header ul li ul li.parent-li').parent('ul').addClass('parent-ul');
                $('header ul li ul.parent-ul').parent('li').addClass('parent-active');
            })
            //search bar exprnd
        $('.header-top-two .right button').on('click', function() {
            $('.header-top-two .right').toggleClass('widthfull');
        });
        //search bar border color
        $('.middel-top .center').on('click', function() {
            $('.middel-top .center').toggleClass('bordercolor');
        });
        //color select jquery
        $('.color-select > span').on('click', function() {
            $('.color-select > span').toggleClass('outline');
            $(this).addClass("outline").siblings().removeClass("outline");
        });
        /*----------------------------
         nivoSlider active
        ------------------------------ */
        $('#mainSlider').nivoSlider({
            directionNav: true,
            animSpeed: 500,
            effect: 'random',
            slices: 18,
            pauseTime: 10000,
            pauseOnHover: false,
            controlNav: true,
            prevText: '<i class="mdi mdi-chevron-left"></i>',
            nextText: '<i class="mdi mdi-chevron-right"></i>'
        });
        /*----------------------------
         plus-minus-button
        ------------------------------ */
        $(".qtybutton").on("click", function() {
            var $button = $(this);
            var oldValue = $button.parent().find("input").val();
            if ($button.text() == "+") {
                var quantity = document.getElementById("quantity").getAttribute("max");
                if (oldValue < parseInt(quantity)) {
                    var newVal = parseFloat(oldValue) + 1;
                }else{
                    var newVal = parseFloat(oldValue);
                }
            } else {
                // Don't allow decrementing below zero
                if (oldValue > 0) {
                    var newVal = parseFloat(oldValue) - 1;
                } else {
                    newVal = 0;
                }
            }
            $button.parent().find("input").val(newVal);
        });
        /*----------------------------
         price-slider active
        ------------------------------ */
        try{

            var url = window.location.href
            var url_arr = []
            for (let i = 0; i < url.split("?")[1].split("&").length; i++) {
                if (url.split("?")[1].split("&")[i].includes("price")) {
                    url_arr.unshift(url.split("?")[1].split("&")[i]);
                }
            }
            url_arr = url_arr.sort();
        }catch{
            
        }

        try{$("#slider-range").slider({
                range: true,
                min: 5,
                max: 600,
                values: [url_arr[1].split("=")[1], url_arr[0].split("=")[1]],
            slide: function(event, ui) {
                $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
                window.location.href = `?min_price=${ui.values[0]}&max_price=${ui.values[1]}`;
            }
        }); }
        catch{
            $("#slider-range").slider({
                range: true,
                min: 5,
                max: 600,
                values: [150,399],
            slide: function(event, ui) {
                $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
                window.location.href = `?min_price=${ui.values[0]}&max_price=${ui.values[1]}`;
            }
        }); 
        }
        $("#amount").val("$" + $("#slider-range").slider("values", 0) + " - $" + $("#slider-range").slider("values", 1))
    /*--------------------------
    scrollUp
    ---------------------------- */
    
    $.scrollUp({
        scrollText: '<i class="mdi mdi-chevron-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });
    /*--------------------------
     // simpleLens
     ---------------------------- */
    $('.simpleLens-image').simpleLens({

    });

})(jQuery);