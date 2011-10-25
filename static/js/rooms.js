var BASE_URL = "/api/v1/building/";
$(document).ready(function(){
	$.getJSON(BASE_URL,function(buildings_data){
		for (var i=0; i < buildings_data.length; i++){
			$("<div class='building' id='b"+buildings_data[i].id+"'><h2>"+buildings_data[i].name+"</h2><div class='floors'></div></div>").data("url",BASE_URL+buildings_data[i].id+"/").click(function(){
				if ($(".floors",$(this)).children().length==0){
					$.getJSON($(this).data("url"),function(building_data){
						for (var i=0; i < building_data.floors.length; i++){
							$("<div class='floor' id='b"+building_data.id+"f"+building_data.floors[i].id+"'><h3>"+building_data.floors[i].name+"</h3><div class='rooms'></div></div>").data("url",BASE_URL+building_data.id+"/floor/"+building_data.floors[i].id+"/").click(function(){
								if ($(".rooms",$(this)).children().length==0){
									$.getJSON($(this).data("url"),function(floor_data){
										for (var i=0; i<floor_data.rooms.length; i++){
											$("<div class='room' id='b"+building_data.id+"f"+floor_data.id+"r"+floor_data.floors[i].id+"'><h4>"+floor_data.rooms[i].name+"</h4><div class='details'><p>Capactiy: "+floor_data.rooms[i].capacity+"</p></div></div>").hide().appendTo("#b"+building_data.id+"f"+floor_data.id+" .rooms");
										}
									});
								}
								$("#b"+building_data.id+"f"+floor_data.id+" .rooms").toggle(500);
							}).hide().appendTo("#b"+building_data.id+" .floors");
						}
					});
				}
				$("#b"+building_data.id+" .floors").toggle(500);
			}).appendTo("#buildings");
		}
	});
});	