$(document).ready(function() {
	$('#main').css('min-height', $(window).height()+'px');
	$('#main').css('min-width', $(window).width()+'px');
	$(window).resize(function() {
		$('#main').css('min-height', $(window).height()+'px');
		$('#main').css('min-width', $(window).width()+'px');
	});
});

// $('#main').css('background-size', $(window).width()+'px'+$(window).height()+'px');