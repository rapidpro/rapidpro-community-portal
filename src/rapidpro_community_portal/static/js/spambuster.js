//requires jquery
$(function(){
    $('.topyenoh').css({
        "display": "None",
        "position": "absolute",
        "left": "9999px"
    })
    $("form").each(function(){
        var $this = $(this)
        var honeypot = $this.find(".topyenoh")
        if(honeypot.length){
           $this.find('input, select').focus(function(){
                honeypot.find('input[name=company_company_email]').val('nine')
           })
        }
    })
})