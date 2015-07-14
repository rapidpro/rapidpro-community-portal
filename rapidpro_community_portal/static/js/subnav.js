function loadSubNav(subnavType) {
    subnavHeadersArray = [];
    subnavLinksArray = [];
    subnavTargetArray = [];
    subnavSelected = "";
    if(window.location.pathname == "/stories/") {
        clearAllNavClasses();
        document.getElementById('nav_stories').className = 'selected';
    }
    else if(window.location.pathname == "/blog/") {
        clearAllNavClasses();
        document.getElementById('nav_connect').className = 'selected';
        if(subnavType == "") {
            subnavType = "connect";
        }
        subnavSelected = "Blog";
    }
    else if(window.location.pathname == "/videos/") {
        clearAllNavClasses();
        document.getElementById('nav_learn').className = 'selected';
        if(subnavType == "") {
            subnavType = "learn";
        }
        subnavSelected = "Videos";
    }
    else if(window.location.pathname == "/deployment-toolkit/") {
        clearAllNavClasses();
        document.getElementById('nav_learn').className = 'selected';
        if(subnavType == "") {
            subnavType = "learn";
        }
        subnavSelected = "Deployment&nbsp;Toolkit";
    }
    else if(window.location.pathname == "/online-courses/") {
        clearAllNavClasses();
        document.getElementById('nav_learn').className = 'selected';
        if(subnavType == "") {
            subnavType = "learn";
        }
        subnavSelected = "Online&nbsp;Courses";
    }
    switch(subnavType) {
        case "learn":
            subnavHeadersArray = ["Knowledge&nbsp;Base", "Videos", "Online&nbsp;Courses", "Deployment&nbsp;Toolkit"];
            subnavLinksArray = ["http://knowledge.rapidpro.io/knowledgebase", "/videos/", "/online-courses/", "/deployment-toolkit/"];
            subnavTargetArray = ["", "", "", ""];
            clearAllNavClasses();
            document.getElementById('nav_learn').className = 'selected';
            break;
        case "connect":
            subnavHeadersArray = ["User&nbsp;Forum", "Blog"];
            subnavLinksArray = ["http://knowledge.rapidpro.io/", "/blog/"];
            subnavTargetArray = ["", ""];
            clearAllNavClasses();
            document.getElementById('nav_connect').className = 'selected';
            break;
    }
    subnavHTML = "";
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
