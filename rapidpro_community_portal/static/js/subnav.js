function loadSubNav(subnavType) {
    subnavHeadersArray = [];
    subnavLinksArray = [];
    subnavSelected = "";
    if(window.location.pathname == "/stories/") {
        clearAllNavClasses();
        document.getElementById('nav_stories').className = 'selected';
        subnavHeadersArray = [];
        subnavLinksArray = [];
        subnavTargetArray = [];
    }
    else if(window.location.pathname == "/blog/") {
        clearAllNavClasses();
        document.getElementById('nav_connect').className = 'selected';
        if(subnavType == "") {
            subnavType = "connect";
        }
        subnavSelected = "Blog";
    }
    switch(subnavType) {
        case "learn":
            subnavHeadersArray = ["Knowledge Base", "Videos", "Online Courses"];
            subnavLinksArray = ["http://rapidpro1.uservoice.com/knowledgebase", "https://www.youtube.com/channel/UCtGk7u6DLHjeWn0P4AEpBKA", "/"];
            subnavTargetArray = ["_blank", "_blank", "_blank"];
            clearAllNavClasses();
            document.getElementById('nav_learn').className = 'selected';                           
            break;
        case "connect":
            subnavHeadersArray = ["User Forum", "Blog"];
            subnavLinksArray = ["http://rapidpro1.uservoice.com/", "/blog/"];
            subnavTargetArray = ["_blank", ""];
            clearAllNavClasses();
            document.getElementById('nav_connect').className = 'selected';
            break;
    }
    subnavHTML = "<a href='#'></a>";
    for (var i = 0; i < subnavHeadersArray.length; i++) {
        subnavHTML = subnavHTML + "<a href='" + subnavLinksArray[i] + "' target='" + subnavTargetArray[i] + "'";
        if (subnavHeadersArray[i] == subnavSelected) {
            subnavHTML = subnavHTML + "class='selected'";
        }
        subnavHTML = subnavHTML + ">" + subnavHeadersArray[i] + "</a>";
    }
    document.getElementById("subnav_right").innerHTML = subnavHTML;
}
function clearAllNavClasses() {
    document.getElementById('nav_learn').className = '';
    document.getElementById('nav_connect').className = '';
    document.getElementById('nav_stories').className = '';
}