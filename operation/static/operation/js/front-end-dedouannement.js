
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
    $(this).parents(".card").find(".card-header").find("i").toggleClass("fas fa-chevron-down fas fa-chevron-right");
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



$(document).ready(circuit('#id_Circuit'))
$("#id_Circuit").change(function(){
  if ($(this).val() == "vert") {
    console.log("Select vert");
    $("#led").removeClass("w3-yellow w3-red").addClass("w3-green")
    $("#rouge , #jaune").slideUp("normal");
  }
  else if ($(this).val() == "jaune") {
    console.log("Select jaune");
    $("#led").removeClass("w3-green w3-red").addClass("w3-yellow")
    $("#jaune").slideDown("normal");
    $("#rouge").hide("normal");
    $("#jaune").removeClass("w3-pale-red w3-pale-green").addClass("w3-pale-yellow")
  }
  else if ($(this).val() == "rouge") {
    console.log("Select rouge");
    $("#led").removeClass("w3-yellow w3-green").addClass("w3-red")
    $("#rouge, #jaune").slideDown("normal");
    $("#rouge, #jaune").removeClass("w3-pale-yellow w3-pale-green").addClass("w3-pale-red");
  }
  else {
    console.log("No selection");
    $("#led").removeClass("w3-yellow w3-green w3-red")
    $("#rouge , #jaune").hide()
  }
})

function circuit(x) {
  console.log($(x).val());

  if ($(x).val() == "vert") {
    console.log("Select vert");
    $("#led").removeClass("w3-yellow w3-red").addClass("w3-green")
    $("#rouge , #jaune").hide();
  }
  else if ($(x).val() == "jaune") {
    console.log("Select jaune");
    $("#led").removeClass("w3-green w3-red").addClass("w3-yellow")
    $("#jaune").slideDown("normal");
    $("#rouge").hide();
    $("#jaune").removeClass("w3-pale-red w3-pale-green").addClass("w3-pale-yellow")
  }
  else if ($(x).val() == "rouge") {
    console.log("Select rouge");
    $("#led").removeClass("w3-yellow w3-green").addClass("w3-red")
    $("#rouge, #jaune").slideDown("normal");
    $("#rouge, #jaune").removeClass("w3-pale-yellow w3-pale-green").addClass("w3-pale-red");
  }
  else {
    console.log("No selection");
    $("#led").removeClass("w3-yellow w3-green w3-red")
    $("#rouge , #jaune").hide()
  }
}
// Somme total
$(document).ready(function(){
  console.log('$("#id_Montant_Fret").val() = '+$("#id_Montant_Fret").val());
  console.log('$("#id_BAD_Montant").val() = '+$("#id_BAD_Montant").val());
  console.log('$("#id_Overstay_Montant").val() = '+$("#id_Overstay_Montant").val());
  let total =
  Number($("#id_BAD_Montant").val()) +
  Number($("#id_Overstay_Montant").val()) +
  Number($("#id_Surestaries_Montant").val()) +
  Number($("#id_Montant_MICTSL").val()) +
  Number($("#id_Magasinage_Montant").val()) +
  Number($("#id_DAU_Depense").val()) +
  Number($("#id_Amende_Montant").val()) +
  Number($("#id_OV_Montant").val()) +
  Number($("#id_OV_Depense").val()) +
  Number($("#id_OV_Docker").val()) +
  Number($("#id_Montant_Fret").val()) +
  Number($("#id_Immobilisation").val()) +
  Number($("#id_Autres_Montant").val()) +
  Number($("#id_Depense_Fixe").val()) +
  Number($("#id_Depense_Autre").val());

  console.log("Total = "+total);
  document.getElementById("id_Total").value = total;
})
