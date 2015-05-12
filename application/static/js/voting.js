function upV(){
    id = $('#pid').val();
    out = $.ajax({
<<<<<<< HEAD
        url:'/up/'+id
    });
    out = JSON.parse(out);
    console.log(out.responseText);
    $('#up').remove();
=======
        url:'/up'+id
    });
    if (out==='true'){
        $('#up').remove();
    }else{
        $('.flashes').html("<li><b>Don't upvote multiple times</b></li>")
        $('#up').remove();
        console.log('FAIL');
    };
>>>>>>> adb5fa61f560f0cb8abe32f4c34d48ae7e4952d0
};

function UupV(){
    id = $('#pid').val();
    out = $.ajax({
<<<<<<< HEAD
        url:'/uUp/'+id
    });
    out = JSON.parse(out);
    console.log(out);
    $('#up').remove();
=======
        url:'/uUp'+id
    });
    if (out==='true'){
        $('#up').remove();
    }else{
        $('.flashes').html("<li><b>Don't upvote multiple times</b></li>")
        $('#up').remove();
        console.log('FAIL');
    };
>>>>>>> adb5fa61f560f0cb8abe32f4c34d48ae7e4952d0
};
