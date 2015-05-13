function upV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/up/'+id
    });
    $('#up').remove();
};

function UupV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/uUp/'+id
    });
    $('#up').remove();
};

function dV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/dw/'+id
    });
    $('#up').remove();
};

function UdV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/uDw/'+id
    });
    $('#up').remove();
};
