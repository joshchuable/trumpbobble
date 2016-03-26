$(document).ready(function() {
	var option = '';
	for (var i=1;i<100;i++){
	   option += '<option value="'+ i + '">' + i + '</option>';
	}
	$('#product-quantity-items').append(option);
});

$(document).ready(function() {
	update_subtotal();
	$('#product-quantity-items').change(function() {
		update_subtotal();
	});
});

function update_subtotal() {
	var subtotal = 0;
	$('.checkout-table > #product-info').each(function() {
		var quantity = parseFloat($(this).find('option:selected').val());
		var price = parseFloat($(this).find('.product-price > #price').text());
		var amount = (quantity * price);
		subtotal += amount;
	});

	var subtotal_two = parseFloat(subtotal).toFixed(2);
	$('#order-subtotal').text(subtotal_two);
	var subtotal_fix = parseInt((parseFloat($('#order-subtotal').text()) * 100).toFixed(0));
	$('#stripe-button').attr('data-amount',subtotal_fix);
	$('#order-form-remix').attr('action','/charge/'+subtotal_fix);
}

// $(document).ready(function() {
// 	$('#stripe-button > button').click(function() {
// 		var subtotal_fix = parseInt((parseFloat($('#order-subtotal').text()) * 100).toFixed(0));
// 		console.log(subtotal_fix);
// 		$('#stripe-button').attr('data-amount',subtotal_fix);
// 		console.log($('#stripe-button').attr('data-amount',subtotal_fix));
// 	});
// });

$(document).ready(function() {
	console.log($('#stripe-button').attr('data-amount'));
});

// <script>
//   var handler = StripeCheckout.configure({
//     key: 'pk_test_gZGO4hFofN2dMsUz5cAexmAz',
//     image: '/img/documentation/checkout/marketplace.png',
//     locale: 'auto',
//     token: function(token) {
//       // Use the token to create the charge with a server-side script.
//       // You can access the token ID with `token.id`
//     }
//   });

//   $('#customButton').on('click', function(e) {
//     // Open Checkout with further options
//     handler.open({
//       name: 'Demo Site',
//       description: '2 widgets',
//       amount: 2000
//     });
//     e.preventDefault();
//   });

//   // Close Checkout on page navigation
//   $(window).on('popstate', function() {
//     handler.close();
//   });
// </script>