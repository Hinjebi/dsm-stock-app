window.onload = function() {
    var selItem = sessionStorage.getItem("SelItem");  
    $('#ticker').val(selItem);
    }
    $('#ticker').change(function() { 
        var selVal = $(this).val();
        sessionStorage.setItem("SelItem", selVal);
    });