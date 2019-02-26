function validateForm() {
    var headline = document.getElementById("headline").value;
    var long_text = document.getElementById("long_text").value;
    var brief_text = document.getElementById("brief_text").value;
    var username = document.getElementById("username").value;
    var errorarray = new Array();
    var error = false;
    alert("headline: " + headline + " long_text: " + long_text + " brief_text: "  + brief_text + " username: " + username);
    if ( headline == "" ) {
        errorarray.push("Titel");
        error = true;
    }
    if ( long_text == "" ) {
        errorarray.push("Driftinformation f&ouml;r mejl och Wordpress");
        error = true;
    }
    if ( brief_text == "" ) {
        errorarray.push("Driftinformation f&ouml;r Twitter och SMS");
        error = true;
    }
    if ( username == "" ) {
        errorarray.push("Anv&auml;ndarnamn");
        error = true;
    }
    if ( error ) {
        alert("F&ouml;ljande f&auml;lt m&aring;ste vara ifyllda: " + errorarray.toString());
        return false;
    }
}
