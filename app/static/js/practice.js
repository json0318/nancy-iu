$("#datepicker").datepicker();
$("#dialog").dialog();
/*$('a#send').bind('click', function() {
	var msg = $("#msg").val();
	$.getJSON($SCRIPT_ROOT + '/_chat', {
		msg: msg #$('input[name="msg"]').val()
	}, function(data) {
		$("#result").text(data.result);
	});
	return false;
	#alert(msg);
});*/

function chat(){
	/**$(destElem).html('<img src="{{ url_for('static', filename='loading.gif') }}">');*/
	$.getJSON($SCRIPT_ROOT + '/_chat', {
		msg: $('input[name="msg"]').val()
	}).done(function(response) {
		$("#result").html(response)
	}).fail(function() {
		$("#result").html("{{ Error: Could not contact server. }}");
	});
}