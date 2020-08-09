
// Card toggle
$(".card-header").each(function() {
  $(this).mouseover().css({'cursor': 'pointer'});
  $(this).click(function() {
    $(this).parents(".card").find(".bbody").slideToggle("normal");
    $(this).find("i").toggleClass("fas fa-chevron-down fas fa-chevron-right");
    $(this).parents(".card").find(".pint").find("i").toggleClass("fas fa-caret-down fas fa-caret-right");

  })
})

$(".bheader").each(function() {
  $(this).mouseover().css({'cursor': 'pointer'})
  $(this).click(function() {
    $(this).parents(".pint").find(".bbody").slideToggle("normal");
    $(this).parents(".pint").find("i").toggleClass("fas fa-caret-down fas fa-caret-right");
  })
})

function toggle(){
    $(".card-header").each(function(){
      $(this).parents(".card").find(".bbody").slideToggle("normal");
      $(this).find("i").toggleClass("fas fa-chevron-down fas fa-chevron-right");
      $(this).parents(".card").find(".pint").find("i").toggleClass("fas fa-caret-down fas fa-caret-right");
    })
}
function toggleInternal(x){
    $(x).find(".bbody").each(function(){
      $(this).slideToggle("slow");
      $(this).parents(".pint").find("i").toggleClass("fas fa-caret-down fas fa-caret-right");
    })
}

function reduce(){
  $(".card-body").each(function(){
    $(this).parents(".card").find(".bbody").slideUp("normal");
    $(this).find(".pint").find("i").removeClass("fas fa-caret-down").addClass("fas fa-caret-right");
    $(this).parents(".card").find(".card-header").find("i").removeClass("fas fa-chevron-down").addClass("fas fa-chevron-right");
  })
}
