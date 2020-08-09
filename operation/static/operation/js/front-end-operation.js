$(".card-header").each(function (){
    $(this).mouseover().css(
            { 'cursor':'pointer' }
        );
    $(this).click(function(){
        $(this).parents(".card").find(".card-body").slideToggle("normal");
        $(this).find("i").toggleClass("fas fa-chevron-down fas fa-chevron-right");
    })
})

$(".bheader").each(function (){
    $(this).mouseover().css({'cursor': 'pointer'})
    $(this).click(function(){
        $(this).parents(".bcard").find(".bbody").slideToggle("normal");
        $(this).parents(".bcard").find("i").toggleClass("fas fa-caret-down fas fa-caret-right");
    })
})
