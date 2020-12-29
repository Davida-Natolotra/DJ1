function Kajy() {
  var Facture_OT_Honoraire = parseFloat($("#id_Facture_OT_Honoraire").val().replace(/ /g, ''));
  console.log("Facture_OT_Honoraire test = " + Facture_OT_Honoraire);
  if (!$("#id_Facture_OT_Honoraire").val()) {
    Facture_OT_Honoraire = 0;
  }
  var Facture_Autres_Montant = parseFloat($("#id_Facture_Autres_Montant").val().replace(/ /g, ''));
  if (!$("#id_Facture_Autres_Montant").val()) {
    Facture_Autres_Montant = 0
  }

  var Facture_BAD_Montant = parseFloat($("#id_Facture_BAD_Montant").val().replace(/ /g, ''));
  if (!$("#id_Facture_BAD_Montant").val()) {
    Facture_BAD_Montant = 0
  }

  var Facture_Overstay_Montant = parseFloat($("#id_Facture_Overstay_Montant").val().replace(/ /g, ''));
  if (!$("#id_Facture_Overstay_Montant").val()) {
    Facture_Overstay_Montant = 0
  }

  var Facture_Surestaries_Montant = parseFloat($("#id_Facture_Surestaries_Montant").val().replace(/ /g, ''));
  if (!$("#id_Facture_Surestaries_Montant").val()) {
    Facture_Surestaries_Montant = 0
  }

  var Facture_Debarquement = parseFloat($("#id_Facture_Debarquement").val().replace(/ /g, ''));
  if (!$("#id_Facture_Debarquement").val()) {
    Facture_Debarquement = 0
  }

  var Facture_Magasinage_Montant = parseFloat($("#id_Facture_Magasinage_Montant").val().replace(/ /g, ''));
  if (!$("#id_Facture_Magasinage_Montant").val()) {
    Facture_Magasinage_Montant = 0
  }

  var Facture_Droit_Compromis = parseFloat($("#id_Facture_Droit_Compromis").val().replace(/ /g, ''));
  if (!$("#id_Facture_Droit_Compromis").val()) {
    Facture_Droit_Compromis = 0
  }

  var Facture_Amende_Montant = parseFloat($("#id_Facture_Amende_Montant").val().replace(/ /g, ''));
  if (!$("#id_Facture_Amende_Montant").val()) {
    Facture_Amende_Montant = 0
  }

  var Facture_OV_Montant = parseFloat($("#id_Facture_OV_Montant").val().replace(/ /g, ''));
  if (!$("#id_Facture_OV_Montant").val()) {
    Facture_OV_Montant = 0
  }

  var Facture_OV_Docker = parseFloat($("#id_Facture_OV_Docker").val().replace(/ /g, ''));
  if (!$("#id_Facture_OV_Docker").val()) {
    Facture_OV_Docker = 0
  }

  var Facture_Montant_Fret = parseFloat($("#id_Facture_Montant_Fret").val().replace(/ /g, ''));
  if (!$("#id_Facture_Montant_Fret").val()) {
    Facture_Montant_Fret = 0
  }

  var Facture_Immobilisation = parseFloat($("#id_Facture_Immobilisation").val().replace(/ /g, ''));
  if (!$("#id_Facture_Immobilisation").val()) {
    Facture_Immobilisation = 0
  }

  var sousTotal = Facture_OT_Honoraire + Facture_Autres_Montant + Facture_BAD_Montant + Facture_Overstay_Montant + Facture_Surestaries_Montant + Facture_Debarquement + Facture_Magasinage_Montant + Facture_Droit_Compromis + Facture_Amende_Montant + Facture_OV_Montant + Facture_OV_Docker + Facture_Montant_Fret + Facture_Immobilisation;
  document.getElementById("id_Facture_SousTotal").value = sousTotal;

  var tax = parseFloat($("#id_Tax").val());

  var total = sousTotal + (sousTotal * tax / 100);
  document.getElementById("id_TotalFacture").value = total;
}

function KajyMoto(){
  var PT = parseFloat($("#id_PV").val().replace(/ /g, ''));
  console.log("PT test = " + PT);
  if (!$("#id_PV").val()) {
    PT = 0;
  }
  var PUHT = PT/1.2;
  var TVA = 0.2*PUHT;
  document.getElementById('id_PU_HT').value = PUHT;
  document.getElementById('id_TVA').value = TVA;
}
