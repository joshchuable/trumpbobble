$(document).ready(function() {
	$('#trump-background').css('min-height', $(window).height()+'px');
	$('#trump-background').css('min-width', $(window).width()+'px');
	$(window).resize(function() {
		$('#trump-background').css('min-height', $(window).height()+'px');
		$('#trump-background').css('min-width', $(window).width()+'px');
	});
});

// $('#main').css('background-size', $(window).width()+'px'+$(window).height()+'px');