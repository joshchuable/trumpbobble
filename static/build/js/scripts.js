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
$(document).ready(function() {
	$('#trump-background').css('min-height', $(window).height()+'px');
	$('#trump-background').css('min-width', $(window).width()+'px');
	$(window).resize(function() {
		$('#trump-background').css('min-height', $(window).height()+'px');
		$('#trump-background').css('min-width', $(window).width()+'px');
	});
});