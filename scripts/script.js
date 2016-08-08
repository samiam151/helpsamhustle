// NAV
var box = $('.box');
$.get('templates/where.html', function(data){
   box.html(data);
}).fail(function(req){
   console.log(req.status + ' ' + req.statusText);
});


$('.nav_button').on('click', function(e){
   e.preventDefault();
   var url = 'templates/' + $(e.target).data('url') + '.html';

   $.get(url, function(data){
      box.html(data);
   }).fail(function(req){
      console.log(req.status + ' ' + req.statusText);
   });
});
