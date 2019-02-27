function validateForm() {
    var headline = document.getElementById("headline").value;
    var long_text = document.getElementById("long_text").value;
    var brief_text = document.getElementById("brief_text").value;
    var errorarray = new Array();
    var error = false;
    if ( headline == "" ) {
        errorarray.push("Titel");
        error = true;
    }
    if ( long_text == "" ) {
        errorarray.push("Driftinformation för mejl och Wordpress");
        error = true;
    }
    if ( brief_text == "" ) {
        errorarray.push("Driftinformation för Twitter och SMS");
        error = true;
    }
    if ( error ) {
        alert("Följande fält måste vara ifyllda: " + errorarray.toString());
        return false;
    }
}
