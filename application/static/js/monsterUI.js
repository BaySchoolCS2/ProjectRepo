var Mload = true;

function SmD(){//show monsters dialog
  if (Mload){
    $('#mDialog').load('/monstersUI');
  };
  $('#mDialog').show();
  Mload = false;
};

function HmD(){//hide monsters dialog
  $('#mDialog').hide();
};

function sA(){//show advanced options
  $('#advanced').show();
  $('#easy').hide();
};

function hA(){//hide advanced options
  $('#easy').show();
  $('#advanced').hide();
};
