// NAV
var box = $('.box');
$.get('templates/where.html', function(data){
   box.html(data);
}).fail(function(jqXHR){
   console.log(jqXHR.status + ' ' + jqXHR.statusText);
});


$('.nav_button').on('click', function(e){
   e.preventDefault();
   var url = 'templates/' + $(e.target).data('url') + '.html';

   $.get(url, function(data){
      box.html(data);
   }).fail(function(jqXHR){
      console.log(jqXHR.status + ' ' + jqXHR.statusText);
   });
});
