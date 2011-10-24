$(document).ready(function(){
	$.getJSON("/api/v1/building/",function(buildings_data){
		for (var i=0; i < buildings_data.length; i++){
			$("<div class='building'></div>")
				.appendTo("#container")
				.append($("<h2 id='b"+buildings_data[i].id+"'>"+buildings_data[i].name+"</h2>").click(function(){
						$.getJSON("/api/v1/building/"+$(this).attr('id').substring(1)+"/",function(building_data){
							for (var i=0; i < building_data.floors.length; i++){
								$("<div class='floor' id='b"+building_data.id+"f"+building_data.floors[i].id+"'>"+building_data.floors[i].name+"</div>").click(function(){
									$.getJSON("/api/v1/building/"+$(this).attr('id').substring(1).split('f')[0]+"/floor/"+$(this).attr('id').split('f')[1]+"/",function(floor_data){
										for (var i=0; i<floor_data.rooms.length; i++){
									//		$("<div class='room'><h3>"+floor_data.rooms[i].name+"</h3><p>Capactiy: "+floor_data.rooms[i].capacity+"</p></div>").appendTo($(this));
										}
									});
								}).appendTo($("#b"+building_data.id).parent());
							}
						});
					})
				).append("<img src='http://placehold.it/250x150'>");
		}
	});
});