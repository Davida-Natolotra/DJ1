function Print(){
  Popup($('.invoice')[0].outerHTML);
  function Popup(data) {
    window.print();
    return true;
  }
}

function ExportPdf() {
  kendo.drawing.drawDOM("#myCanvas", {
    paperSize: "A4",
    margin: {
      top: "2cm",
      bottom: "1cm",
      left:"2cm",
      right:"2cm",
      keepTogether: ".prevent-split"
    },
    scale: 0.5,
    // height: 500
  }).then(function(group) {
    kendo.drawing.pdf.saveAs(group, "Exported.pdf")
  });
}
