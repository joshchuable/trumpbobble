$(document).ready(function() {
	$('.jumbotron').css('min-height', $(window).height()+'px');
	$('.jumbotron').css('min-width', $(window).width()+'px');

	$('#top-container').css('padding-top',($('#nav').height()+10)+'px');

	$(window).resize(function() {
		// $('#trump-background').css('min-height', $(window).height()+'px');
		$('.jumbotron').css('min-width', $(window).width()+'px');
		$('#top-container').css('padding-top',($('#nav').height()+10)+'px');
	});
});

$(document).ready(function (){
    $("#page-bottom").click(function (){
        $('html, body').animate({
            scrollTop: $('#scroll-end').offset().top
        }, 2000);
        $(this).hide();
    });
});