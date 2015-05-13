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
