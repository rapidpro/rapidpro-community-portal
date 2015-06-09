var parentElements = [
    document.getElementById('parent_learn'),
    document.getElementById('parent_connect')
];

var subnavElements = [
    document.getElementById('subnav_learn'),
    document.getElementById('subnav_connect')
];

console.log('subnavvv');

function subNav(id,parent) {
    for(var i = 0; i< subnavElements.length; i++) {
        console.log(subnavElements[i].id);
        if(subnavElements[i].id === 'subnav_' + id){
            subnavElements[i].classList.remove('hidden');
        }else{
            subnavElements[i].classList.add('hidden');
        }
    }
    for(var i = 0; i< parentElements.length; i++) {
        parentElements[i].classList.remove('selected');
    }
    console.log(parent);
    parent.classList.add('selected');
}
