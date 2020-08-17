$(document).click(function(){
  var sousTotal =
  Number($("#id_Facture_OT_Honoraire").val()) +
  Number($("#id_Facture_Autres_Montant").val()) +
  Number($("#id_Facture_BAD_Montant").val()) +
  Number($("#id_Facture_Overstay_Montant").val()) +
  Number($("#id_Facture_Surestaries_Montant").val()) +
  Number($("#id_Facture_Debarquement").val()) +
  Number($("#id_Facture_Magasinage_Montant").val()) +
  Number($("#id_Facture_Droit_Compromis").val()) +
  Number($("#id_Facture_Amende_Montant").val()) +
  Number($("#id_Facture_OV_Montant").val()) +
  Number($("#id_Facture_OV_Docker").val()) +
  Number($("#id_Facture_Montant_Fret").val()) +
  Number($("#id_Facture_Immobilisation").val());
  document.getElementById("id_Facture_SousTotal").value = sousTotal;


  var tax = Number($("#id_Tax").val());

  var total = sousTotal+ (sousTotal*tax/100);
  document.getElementById("id_TotalFacture").value = total;
})

$(document).ready(Kajy());
function Kajy(){
  var sousTotal =
  Number($("#id_Facture_OT_Honoraire").val()) +
  Number($("#id_Facture_Autres_Montant").val()) +
  Number($("#id_Facture_BAD_Montant").val()) +
  Number($("#id_Facture_Overstay_Montant").val()) +
  Number($("#id_Facture_Surestaries_Montant").val()) +
  Number($("#id_Facture_Debarquement").val()) +
  Number($("#id_Facture_Magasinage_Montant").val()) +
  Number($("#id_Facture_Droit_Compromis").val()) +
  Number($("#id_Facture_Amende_Montant").val()) +
  Number($("#id_Facture_OV_Montant").val()) +
  Number($("#id_Facture_OV_Docker").val()) +
  Number($("#id_Facture_Montant_Fret").val()) +
  Number($("#id_Facture_Immobilisation").val());
  document.getElementById("id_Facture_SousTotal").value = sousTotal;


  var tax = Number($("#id_Tax").val());

  var total = sousTotal+ (sousTotal*tax/100);
  document.getElementById("id_TotalFacture").value = total;
}
