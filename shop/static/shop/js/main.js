(function ($)
  { "use strict"
  

/* 1. Proloder */
    $(window).on('load', function () {
      $('#preloader-active').delay(450).fadeOut('slow');
      $('body').delay(450).css({
        'overflow': 'visible'
      });
    });

/* 2. sticky And Scroll UP */
    $(window).on('scroll', function () {
      var scroll = $(window).scrollTop();
      if (scroll < 400) {
        $(".header-sticky").removeClass("sticky-bar");
        $('#back-top').fadeOut(500);
      } else {
        $(".header-sticky").addClass("sticky-bar");
        $('#back-top').fadeIn(500);
      }
    });

  // Scroll Up
    $('#back-top a').on("click", function () {
      $('body,html').animate({
        scrollTop: 0
      }, 800);
      return false;
    });
  

/* 3. slick Nav */
// mobile_menu
    var menu = $('ul#navigation');
    if(menu.length){
      menu.slicknav({
        prependTo: ".mobile_menu",
        closedSymbol: '+',
        openedSymbol:'-'
      });
    };



    /* 4. MainSlider-1 */
    // h1-hero-active
    function mainSlider() {
      var BasicSlider = $('.slider-active');
      BasicSlider.on('init', function (e, slick) {
        var $firstAnimatingElements = $('.single-slider:first-child').find('[data-animation]');
        doAnimations($firstAnimatingElements);
      });
      BasicSlider.on('beforeChange', function (e, slick, currentSlide, nextSlide) {
        var $animatingElements = $('.single-slider[data-slick-index="' + nextSlide + '"]').find('[data-animation]');
        doAnimations($animatingElements);
      });
      BasicSlider.slick({
        autoplay: false,
        autoplaySpeed: 4000,
        dots: false,
        fade: true,
        arrows: false, 
        prevArrow: '<button type="button" class="slick-prev"><i class="ti-angle-left"></i></button>',
        nextArrow: '<button type="button" class="slick-next"><i class="ti-angle-right"></i></button>',
        responsive: [{
            breakpoint: 1024,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              infinite: true,
            }
          },
          {
            breakpoint: 991,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              arrows: false
            }
          },
          {
            breakpoint: 767,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              arrows: false
            }
          }
        ]
      });

      function doAnimations(elements) {
        var animationEndEvents = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
        elements.each(function () {
          var $this = $(this);
          var $animationDelay = $this.data('delay');
          var $animationType = 'animated ' + $this.data('animation');
          $this.css({
            'animation-delay': $animationDelay,
            '-webkit-animation-delay': $animationDelay
          });
          $this.addClass($animationType).one(animationEndEvents, function () {
            $this.removeClass($animationType);
          });
        });
      }
    }
    mainSlider();

    

/* 4. Testimonial Active*/
var testimonial = $('.h1-testimonial-active');
if(testimonial.length){
testimonial.slick({
    dots: true,
    infinite: true,
    speed: 1000,
    autoplay:true,
    loop:true,
    arrows: true,
    prevArrow: '<button type="button" class="slick-prev"><i class="ti-arrow-top-left"></i></button>',
    nextArrow: '<button type="button" class="slick-next"><i class="ti-arrow-top-right"></i></button>',
    slidesToShow: 1,
    slidesToScroll: 1,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: true,
          dots: true,
          arrows:true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows:true
        }
      },
      {
        breakpoint: 500,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false,
          dots:false
        }
      }
    ]
  });
}

  
/* 6. Nice Selectorp  */
  var nice_Select = $('select');
    if(nice_Select.length){
      nice_Select.niceSelect();
    }

 // Brand Active
 $('.brand-active').slick({
  dots: false,
  infinite: true,
  autoplay: true,
  speed: 400,
  arrows: false,
  slidesToShow: 4,
  slidesToScroll: 1,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 4,
        slidesToScroll: 3,
        infinite: true,
        dots: false,
      }
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 4,
        slidesToScroll: 3,
        infinite: true,
        dots: false,
      }
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    },
  ]
});



 // services active
 $('.services-active').slick({
  dots: false,
  infinite: true,
  autoplay: true,
  speed: 400,
  arrows: true,
  prevArrow: '<button type="button" class="slick-prev"><i class="ti-arrow-top-left"></i></button>',
  nextArrow: '<button type="button" class="slick-next"><i class="ti-arrow-top-right"></i></button>',
  slidesToShow: 3,
  slidesToScroll: 1,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        infinite: true,
        dots: false,
      }
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
        infinite: true,
        dots: false,
      }
    },
    {
      breakpoint: 800,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 680,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false
      }
    },
  ]
});

 // services active
 $('.blog-active').slick({
  dots: false,
  infinite: true,
  autoplay: true,
  speed: 400,
  arrows: true,
  prevArrow: '<button type="button" class="slick-prev"><i class="ti-arrow-top-left"></i></button>',
  nextArrow: '<button type="button" class="slick-next"><i class="ti-arrow-top-right"></i></button>',
  slidesToShow: 3,
  slidesToScroll: 1,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        infinite: true,
        dots: false,
      }
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
        infinite: true,
        dots: false,
      }
    },
    {
      breakpoint: 800,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 680,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false
      }
    },
  ]
});



/* 7. data-background */
    $("[data-background]").each(function () {
      $(this).css("background-image", "url(" + $(this).attr("data-background") + ")")
      });


/* 10. WOW active */
    new WOW().init();

// 11. ---- Mailchimp js --------//  
    function mailChimp() {
      $('#mc_embed_signup').find('form').ajaxChimp();
    }
    mailChimp();


// 12 Pop Up Img
    var popUp = $('.single_gallery_part, .img-pop-up');
      if(popUp.length){
        popUp.magnificPopup({
          type: 'image',
          gallery:{
            enabled:true
          }
        });
      }
// 12 Pop Up Video
    var popUp = $('.popup-video');
    if(popUp.length){
      popUp.magnificPopup({
        type: 'iframe'
      });
    }

/* 13. counterUp*/
    $('.counter').counterUp({
      delay: 10,
      time: 3000
    });

/* 14. Datepicker */
  $('#datepicker1').datepicker();

// 15. Time Picker
  $('#timepicker').timepicker();

//16. Overlay
  $(".snake").snakeify({
    speed: 200
  });


//17.  Progress barfiller

  $('#bar1').barfiller();
  $('#bar2').barfiller();
  $('#bar3').barfiller();
  $('#bar4').barfiller();
  $('#bar5').barfiller();
  $('#bar6').barfiller();




// Modal Activation
    $('.search-switch').on('click', function () {
      $('.search-model-box').fadeIn(400);
    });

    $('.search-close-btn').on('click', function () {
      $('.search-model-box').fadeOut(400, function () {
          $('#search-input').val('');
      });
    });

})(jQuery);

$(document).ready(function(){
  let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
  var testEmail = /^\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i;
  let passwordRegex = new RegExp(/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$/);

  $(document).on('click', '#loginBtn', function (e) {
    let modalMessage = $(this).closest('#loginSection').find('.modal-error-message');
    let email = $('#login_email').val();
    let password = $('#login_password').val();

    $.ajax({
      url: 'login/',
      type: 'POST',
      data: {
        email: email,
        password: password,
        csrfmiddlewaretoken: csrfmiddlewaretoken,
      },
      success: function (data) {
        window.location.href = '/';
        
      },
      error: function (data) {
        console.log('error')
        // get status code
        let status = data.status;
        console.log(status)
        if(status == 401){
          $(modalMessage).removeClass('d-none');
          $(modalMessage).text('Please verify your email in order to log in');
        }
      else{
        $(modalMessage).removeClass('d-none');
        $(modalMessage).text('Invalid email or password');
      }
        
      }
    })


  });


$(document).on('click', '#registerBtn', function (e) {
  let email = $('#register_email').val();
  let password = $('#register_password1').val();
  let confirmPassword = $('#register_password2').val();
  let message = $(this).closest('#registerSection').find('.modal-error-message');


  if(email == '' || password == '' || confirmPassword == ''){
    message.removeClass('d-none');
    message.html('Please fill all fields')
    return false;
  }
  if (!testEmail.test(email)) {
    message.removeClass('d-none');
    message.html('Please enter a valid email');
    return false;
  }
  if(!passwordRegex.test(password)){
    message.removeClass('d-none');
    message.html('Password must be at least 8 characters long and contain at least one number and one special character')
    return false;
  }
  if(password != confirmPassword){
    message.removeClass('d-none');
    message.html('Passwords do not match')
    return false;
  }

  $.ajax({
    url: 'register/',

    type: 'POST',
    data: {
      email: email,
      password: password,
      csrfmiddlewaretoken: csrfmiddlewaretoken,
    },
    success: function (data) {
      $("#registered_email").html(email)
      $("#registerInputs").addClass('d-none');
      $("#successfulRegister").removeClass('d-none');
    },
    error: function (data) {
      let status_code = parseInt(data.status)
      console.log(status_code)
      if(status_code == 404){
        message.html('Email already exists')
      }
      else if(status_code == 401){
        message.html('Our servers are overloaded today! Please try again tomorrow')
      }
      
      message.removeClass('d-none');
    }
  })

});
$(document).on('click', '#changePasswordBtn', function (e) {
    let current_password = $('#current_password').val();
    let password1 = $('#changed_password1').val();
    let password2 = $('#changed_password2').val();
    let message = $("#changePasswordMessage");
    if(!passwordRegex.test(password1)){
      message.addClass('text-danger')
      message.removeClass('d-none');
      message.html('Password must be at least 8 characters long and contain at least one number and one special character')
      return false;
    }
    if(password1 != password2){
      message.removeClass('d-none');
      message.addClass('text-danger')
      message.html('Passwords do not match')
      return false;
    }

    $.ajax({
      url: 'change-password/',
      type: 'POST',
      data: {
        current_password: current_password,
        password: password1,
        csrfmiddlewaretoken: csrfmiddlewaretoken,
      },
      success: function (data) {
        message.removeClass('text-danger d-none')
        message.addClass('text-success')
        message.html('Password changed successfully')
      },
      error: function (data) {
        if(data.status == 403){
            message.removeClass('d-none');
            message.addClass('text-danger')
            message.html('Wrong current password')
        }

      }
    })

});
$(document).on('click', '#send_contact_message', function (e) {
    let from_mail = $('#contact_message_from').val();
    let message = $('#contact_message_text').val();
    console.log(from_mail)
    console.log(message)
    

    $.ajax({
      url: 'send-contact-message/',
      type: 'POST',
      data: {
        from_mail: from_mail,
        message: message,
        csrfmiddlewaretoken: csrfmiddlewaretoken,
      },
      success: function (data) {
        $('#contact_message_from').val('');
        $('#contact_message_text').val('Message sent successfully');
      }
    })

});

$(document).on('click', '.loginPromtBtn', function (e) {
    // show login modal
    $('#loginModal').modal('show');
});


$(document).on('click', '#show_change_password_form_btn', function (e) {
  $('#changePassword_form').removeClass('d-none');
});
// detect when loginModal is shown
$('#loginModal').on('shown.bs.modal', function () {
  $('#login_email').focus();
  $('body').addClass('modal-open');
});

// detect when loginModal is hidden
$('#loginModal').on('hidden.bs.modal', function () {
  $('body').removeClass('modal-open');
});

$(document).on("click", '#register-link', function (e) {
  e.preventDefault();
  $('#loginSection').addClass('d-none');
  $('#registerSection').removeClass('d-none');
});

$(document).on("click", '#login-link', function (e) {
  e.preventDefault();
  $('#registerSection').addClass('d-none');
  $('#loginSection').removeClass('d-none');
});

$(document).on("click", "#apply_coupon", function(e){
    e.preventDefault();
    let coupon_code = $("#coupon_code").val()
    if(coupon_code == ''){
      $("#coupon_code").val("Input can't be empty.");
      return;
    }

    $.ajax({
      url: 'apply-coupon/',
      type: 'POST',
      data: {
        'coupon_name': coupon_code,
        csrfmiddlewaretoken: csrfmiddlewaretoken,
      },
      success: function (data) {
        $("#coupon_code").val('Coupon applied.')
        $(".product_card_price").each(function (index){
          let discount = parseFloat(data.discount);
          let price = parseFloat($(this).text());
          let updated_price = price - (price * discount);
          $(this).html(updated_price)


        })
      },
      error: function (data) {
        $("#coupon_code").val('No such coupon.')
      }
    })

});




});

