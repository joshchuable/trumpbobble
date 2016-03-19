$(document).ready(function() {
	$('#order-now-form').hide();
	$('.order-now').click(function() {
		var form = $('#order-now-form');
		if(form.is(':visible')) {
			form.fadeOut();
		} else {
			form.fadeIn();
		}
	});
});