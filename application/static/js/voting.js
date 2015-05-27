function upV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/up/'+id
    });
    $('#up').hide();
    $('#down').hide();
    $('#unUp').show();
};

function UupV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/uUp/'+id
    });
    $('#unUp').hide();
    $('#down').show();
    $('#up').show();
};

function dV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/dw/'+id
    });
    $('#down').hide();
    $('#up').hide();
    $('#unDown').show();
};

function UdV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/uDw/'+id
    });
    $('#unDown').hide();
    $('#up').show();
    $('#down').show();
};
