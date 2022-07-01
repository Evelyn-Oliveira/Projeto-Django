$("#Area").change(function () {

    var area_id = $(this).val();
    var url = 'getsubarea/'+area_id;
    $.ajax({               
        url: url,         
        success: function (data) { 
          console.log(data)
          $(".subarea").html(data); 
        }  
      });
    
});

$('body').on('change', '#SubArea', function () {

  var id = $(this).val();
  var url = 'getjobs/' + id;
  $.ajax({
    url: url,
    success: function (data) {
      $(".trabarea").html(data);
    }
  });
})

$('body').on('change', '#TrabdaArea', function () {
    var resumo_id = $(this).val();
    var url = 'getabstract/'+resumo_id;
    $.ajax({                       
        url: url,                    
        success: function (data) { 
          $(".textAreacss").html(data); 
        }
      });
});

$('select').on('change', function() {
    $('option').prop('disabled', false); //reset all the disabled options on every change event
    $('select').each(function() { //loop through all the select elements
      var val = this.value;
      $('select').not(this).find('option').filter(function() { //filter option elements having value as selected option
        return this.value === val;
      }).prop('disabled', true); //disable those option elements
    });
  }).change();


  function Mudarestado(el) {
    var display = document.getElementById(el).style.display;
    if (display == "none")
      document.getElementById(el).style.display = 'block';
    else
      document.getElementById(el).style.display = 'none';
  }

  /*
  var btn = document.getElementById('btn-div');
  var errologin = document.querySelector('.container');
  
  btn.addEventListener('click', function(){
    if(errologin.style.display==='block'){
      errologin.style.display = 'none';
    } else{
      errologin.style.display = 'block';
    }
  
  });
  */

/*$(document).ready(function() {
    $(function() {
        $( "#some_flag" ).dialog({
            modal: true,
            closeOnEscape: false,
            dialogClass: "no-close",
            resizable: false,
            draggable: false,
            width: 600,
            buttons: [
                {
                    text: "OK",
                    click: function() {
                    $( this ).dialog( "close" );
                    }
                }
            ]
        });
    });
});
*/

$("#success-alert").fadeTo(2000, 500).slideUp(500, function(){
    $("#success-alert").alert('close');
});

$(document).ready(function() {
    $("#success-alert").hide();
    $("#myWish").click(function showAlert() {
      $("#success-alert").fadeTo(2000, 500).slideUp(500, function() {
        $("#success-alert").slideUp(500);
      });
    });
  });

  