$(document).ready(function(){
	$.getJSON("/api/v1/building/",function(data){
		for (var i=0; i < data.length; i++){
			$("<h2>"+data[i]["name"]+"</h2>").appendTo("#container");
		}
	});
});