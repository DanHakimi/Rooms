var BASE_URL = "/api/v1/building/";

function bindButtons()
{
	$("nav a").click( function(){
		$(".page").hide();
		$( $(this).attr("href") ).show();
	});
}

function addVenues( venues )
{ /*
		var roomtext = "";
		for( i in venues )
		{
			roomtext = "<div class=\"grid_4\"> <div class=\"roomblock\"> <p>" +
				//You'd put a description here. +
				"</p> </div></div>"
			// Then, you bind the proper click function. Something like .click( navigateTo )
			// If it ( $(this) ) has sub-venues ( Building -> Floor -> Room or Building -> Room ),
			// navigateTo hides the current browse set, and goes down a level.
			// If it is reservable in and of itself, navigateTo hides the current 
			// browse set, and shows the room page.
		}
	}
*/ }

function readyFunction()
{
	bindButtons();
	$.getJSON( BASE_URL, addVenues ); //Adds things to the Browse page.
}

$(document).ready( readyFunction );