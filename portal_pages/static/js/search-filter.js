$(document).ready(function(){
    $(".collapsed").hide();
    $(".tagsheader").click(function(e){ // toggle tag collapse/uncollapse
        tagtype = $(e.target).attr("class").split(" ")[1]; // ie. countries
        if ($(".tags."+tagtype).hasClass("uncollapsed")) {
            $(".tags."+tagtype).hide("500");
            $(".tags."+tagtype).removeClass("uncollapsed");
            $(".tags."+tagtype).addClass("collapsed");
        }
        else {
            $(".tags."+tagtype).show("500");
            $(".tags."+tagtype).removeClass("collapsed");
            $(".tags."+tagtype).addClass("uncollapsed");
        }
    });
});
