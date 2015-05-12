function upV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/up/'+id
    });
    out = JSON.parse(out);
    console.log(out.responseText);
    $('#up').remove();
};

function UupV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/uUp/'+id
    });
    out = JSON.parse(out);
    console.log(out);
    $('#up').remove();
};
