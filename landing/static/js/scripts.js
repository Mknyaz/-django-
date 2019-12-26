$(document).ready(function(){
  var form = $('#form_date_master')
  console.log(form);
  form.on('submit', function(e){
    e.preventDefault();
    console.log('123');
    var date = new Date($('#date'));
    console.log(date);
    var master_id
    var master_name
  })
});
