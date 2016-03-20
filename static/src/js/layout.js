$(document).ready(function() {
	$('#trump-background').css('min-height', $(window).height()+'px');
	$('#trump-background').css('min-width', $(window).width()+'px');

	$('#top-container').css('padding-top',($('#nav').height()+10)+'px');

	$(window).resize(function() {
		// $('#trump-background').css('min-height', $(window).height()+'px');
		$('#trump-background').css('min-width', $(window).width()+'px');
		$('#top-container').css('padding-top',($('#nav').height()+10)+'px');
	});
});