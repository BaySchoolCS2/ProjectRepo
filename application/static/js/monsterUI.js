function SmD(){//show monsters dialog
  $('#mDialog').load('/monstersUI')
  $('#mDialog').show();
  //$('#mBtn').text('Cancel')
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
