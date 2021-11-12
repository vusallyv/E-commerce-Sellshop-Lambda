$(function () {
    $(".pagin").click(function () {
        console.log("ok");
        if ($(this).hasClass("active")) {
            $(this).removeClass("active");
            $(this).removeClass('bg-primary')
            
        }  else {
            $(this).addClass("active");
            $(this).addClass('bg-primary')
        }
    });
});