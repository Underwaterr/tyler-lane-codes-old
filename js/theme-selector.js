
$(document).ready(function() {
	$('.theme-selector').click(function (){
	   $('#theme').attr('href','css/bootstrap-' + this.id + '.css');
	});
});
