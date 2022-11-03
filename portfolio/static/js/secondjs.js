function checkElementLocation() {
    var $window = $(window);
    var bottom_of_window = $window.scrollTop() + $window.height();
  
    $('.elem').each(function(i) {
      var $that = $(this);
      var bottom_of_object = $that.position().top + $that.outerHeight();
  
      //if element is in viewport, add the animate class
      if (bottom_of_window > bottom_of_object) {
        $(this).addClass('fade-in');
      }
    });
  }
  // if in viewport, show the animation
  checkElementLocation();
  
  $(window).on('scroll', function() {
    checkElementLocation();
  });




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
        $('.React').css({'width':'60%'});
        $('.Python').css({'width':'50%'});
        $('.Django').css({'width':'50%'});
        $('.SQL').css({'width':'50%'});
        $('.Git').css({'width':'50%'});
        $('.MongoDB').css({'width':'50%'});
        $('.Bootstrap').css({'width':'50%'});
        $('.Amazon').css({'width':'50%'});
        $('.Google').css({'width':'50%'});
        $('.Analytics').css({'width':'50%'});

        
    } else {
        $('.HTML').css({'width':'0%'});
        $('.CSS').css({'width':'0%'});
        $('.JavaScript').css({'width':'0%'});
        $('.PHP').css({'width':'0%'});
        $('.WordPress').css({'width':'0%'});
        $('.Photoshop').css({'width':'0%'});
        $('.React').css({'width':'0%'});
        $('.Python').css({'width':'0%'});
        $('.Django').css({'width':'0%'});
        $('.SQL').css({'width':'0%'});
        $('.Git').css({'width':'0%'});
        $('.MongoDB').css({'width':'0%'});
        $('.Bootstrap').css({'width':'0%'});
        $('.Amazon').css({'width':'0%'});
        $('.Google').css({'width':'0%'});
        $('.Analytics').css({'width':'0%'});

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

