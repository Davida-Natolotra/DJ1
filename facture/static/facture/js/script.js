function Print(){
  Popup($('.invoice')[0].outerHTML);
  function Popup(data) {
    window.print();
    return true;
  }
}

function ExportPdf() {
  let factnum = $('#factnum').html();
  console.log("factnum = "+factnum);
  var filename;
  if ($('#ptitle').html() === 'Prévisualisation du BL'){
    filename = "BL";
  }
  else if ($('#ptitle').html() === 'Prévisualisation de la facture'){
    filename = "Facture";
  }
  var name = filename+'-'+factnum+".pdf";
  console.log('name ='+name);
  kendo.drawing.drawDOM("#myCanvas", {
    paperSize: "A4",
    margin: {
      top: "1cm",
      bottom: "1cm",
      left:"1cm",
      right:"1cm",
      keepTogether: ".prevent-split"
    },
    scale: 0.7,
    // height: 500
  }).then(function(group) {
    kendo.drawing.pdf.saveAs(group, name)
  });
}
