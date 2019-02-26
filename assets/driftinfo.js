function validateForm() {
    var headline = document.forms["usrform"]["headline"].value;
    var long_text = document.forms["usrform"]["long_text"].value;
    var brief_text = document.forms["usrform"]["brief_text"].value;
    var username = document.forms["usrform"]["username"].value;
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
    if ( username == "" ) {
        errorarray.push("Användarnamn");
        error = true;
    }
    if ( error ) {
        alert("Följande fält måste vara ifyllda: " + errorarray.toString());
        return false;
    }
}
