
// Card toggle
$(".card-header").each(function (){
    $(this).mouseover().css(
            { 'cursor':'pointer' }
        );
    $(this).click(function(){
        $(this).parents(".card").find(".card-body").slideToggle("normal");
        $(this).find("i").toggleClass("fas fa-chevron-down fas fa-chevron-right");
    })
})

function toggle(){
    $(".card-body").each(function(){
      $(this).slideToggle("slow");
      $(this).parents(".card").find("i").toggleClass("fas fa-chevron-down fas fa-chevron-right");
    })
}

function reduce(){
  $(".card-body").each(function(){
    $(this).slideUp("slow");
    $(this).parents(".card").find("i").removeClass("fas fa-chevron-down").addClass("fas fa-chevron-right");
  })
}
