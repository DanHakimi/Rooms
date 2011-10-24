$(document).ready(function(){
	$.getJSON("http://campus-rooms.ep.io/api/v1/building/",function(data){
		for (var i=0; i < data.length; i++){
			$("<div class='building'></div>")
				.appendTo("#container")
				.append("<img src='http://placehold.it/250x150'>")
				.append($("<h2 id='b"+data[i]["id"]+"'>"+data[i]["name"]+"</h2>").click(function(){
						$.getJSON("http://campus-rooms.ep.io/api/v1/building/"+$(this).attr('id')+"/",function(data){
							for (var i=0; i < data["floors"].length; i++){
								$("<div class='floor' id='f"+data[i]["id"]+"'>"+data["floors"][i].name+"</div>").click(function(){
									
								});
							}
						}).appendTo($(this));
					})
				);
		}
	});
});