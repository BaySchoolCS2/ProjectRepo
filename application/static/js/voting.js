function upV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/up'+id
    });
    if (out==='true'){
        $('#up').remove();
    }else{
        $('.flashes').html("<li><b>Don't upvote multiple times</b></li>")
        $('#up').remove();
        console.log('FAIL');
    };
};

function UupV(){
    id = $('#pid').val();
    out = $.ajax({
        url:'/uUp'+id
    });
    if (out==='true'){
        $('#up').remove();
    }else{
        $('.flashes').html("<li><b>Don't upvote multiple times</b></li>")
        $('#up').remove();
        console.log('FAIL');
    };
};
