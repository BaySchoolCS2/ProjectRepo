function upV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/up/'+id
    });
    $('#up').hide();
    $('#unUp').show();
};

function UupV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/uUp/'+id
    });
    $('#unUp').hide();
    $('#up').show();
};

function dV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/dw/'+id
    });
    $('#down').hide();
    $('#unDown').show();
};

function UdV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/uDw/'+id
    });
    $('#unDown').hide();
    $('#down').show();
};
