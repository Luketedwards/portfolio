
/** when #skills is in viewport */
$(window).scroll(function() {
    var hT = $('#skills').offset().top,
        hH = $('#skills').outerHeight(),
        wH = $(window).height(),
        wS = $(this).scrollTop();
    if (wS > (hT+hH-wH)){
        $('.HTML').css({'width':'100%'});
        $('.CSS').css({'width':'90%'});
        $('.JavaScript').css({'width':'75%'});
        $('.PHP').css({'width':'80%'});
        $('.WordPress').css({'width':'90%'});
        $('.Photoshop').css({'width':'55%'});
    } else {
        $('.HTML').css({'width':'0%'});
        $('.CSS').css({'width':'0%'});
        $('.JavaScript').css({'width':'0%'});
        $('.PHP').css({'width':'0%'});
        $('.WordPress').css({'width':'0%'});
        $('.Photoshop').css({'width':'0%'});
    }
});

/** on page load */
$( document ).ready(function() {
    /** when .mobnav is hovered scale 1.2*/
    $('.mobnav').hover(function() {
        $(this).css({'transform':'scale(1.2)'});
    });
    /** when .mobnav is not hovered scale 1*/
    $('.mobnav').mouseleave(function() {
        $(this).css({'transform':'scale(1)'});
    });
    $('.back-to-top').hover(function() {
        $(this).css({'transform':'scale(1.2)'});
    });
    /** when .mobnav is not hovered scale 1*/
    $('.back-to-top').mouseleave(function() {
        $(this).css({'transform':'scale(1)'});
    });

});

