$(document).ready(function() {
	var option = '';
	for (var i=0;i<100;i++){
	   option += '<option value="'+ i + '">' + i + '</option>';
	}
	$('#product-quantity-items').append(option);
});

$(document).ready(function() {
	$('#product-quantity-items').change(function() {
		update_subtotal();
	});
});

function update_subtotal() {
	var subtotal = 0;
	$('#order-table > tbody > tr').each(function() {
		var quantity = $(this).find('option:selected').val();
		var price = $(this).find('.product-price > .price').val();
		var amount = (quantity * price);
		subtotal += amount;
	});

	$('#order-subtotal').text(subtotal);
}