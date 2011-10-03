$(document).ready(function(){
	$("nav a").click(function(){
		$(".page").hide();
		$($(this).attr("href")).show();
	});
});
