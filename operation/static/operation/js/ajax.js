$('#Exportateur').change(function (e) {
    e.preventDefault();
    if ($(this).val() != "") {
        var ExportateurName = $("[value~=" + $(this).val() + "]").text();
        $.ajax({
            type: 'GET',
            url: "{% url 'ExportateurData'%}",
            data: {
                "ExportateurName": ExportateurName,
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function (response) {
                var ExportateurIdBSC = response.ExportateurIdBSC;
                document.getElementById("ExportateurIdBSC").value = ExportateurIdBSC;
            },
            error: function (response) {
                console.log("ERROR" + response);
            }
        })
    } else {
        document.getElementById("ExportateurIdBSC").value = "";
    }
})
$('#Importateur').change(function (e) {
    e.preventDefault();
    if ($(this).val() != "") {
        var ImportateurName = $("[value~=" + $(this).val() + "]").text();
        $.ajax({
            type: 'GET',
            url: "{% url 'ImportateurData'%}",
            data: {
                "ImportateurName": ImportateurName,
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function (response) {
                var ImportateurIdBSC = response.ImportateurIdBSC;
                var DomBanque = response.DomBanque;
                document.getElementById("ImportateurIdBSC").value = ImportateurIdBSC;
                document.getElementById("DomBanque").value = DomBanque;
            },
            error: function (response) {
                console.log("ERROR" + response);
            }
        })
    } else {
        document.getElementById("ImportateurIdBSC").value = "";
    }
})