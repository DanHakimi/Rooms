function home () {
	console.log("home");
	$("#browse").hide();
	$("#inbox").hide();
	$("#home").show();
}
function browse() {
	$("#home").hide();
	$("#inbox").hide();
	$("#browse").show();
}
function inbox () {
	$("#home").hide();
	$("#browse").hide();
	$("#inbox").show();
}

function readyFunction (){
	$(".hidden").hide();
	$("#homelink").click( home );
	$("#browselink").click( browse );
	$("#inboxlink").click( inbox );
}
jQuery( readyFunction );
