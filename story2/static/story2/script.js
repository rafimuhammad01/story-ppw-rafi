$("#explore").click(function() {
    $('html, body').animate({
        scrollTop : $("#skills").offset().top - 50
    }, 10);
})