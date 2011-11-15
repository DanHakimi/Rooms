var BASE_URL = "/api/v1/building/";

function bindButtons()
{
	$("nav a").click( function(){
		$(".page").hide();
		$( $(this).attr("href") ).show();
	});
}

function createNavigateToFunction( venue )
{
	/* Returns a function with the following specifications:
		 * If it ( $(this) ) has sub-venues ( Building -> Floor -> Room or Building -> Room ),
		 * navigateTo hides the current browse set, and goes down a level.
		 * If it is reservable in and of itself, navigateTo hides the current 
		 * browse set, and shows the room page. */
	
	return ( function(){
		/* Note that this function is an onclick function.
			and that "this" refers to the div being clicked */
		if( $(this).floors )
		{
		}
		else if( venues[i].rooms )
		{
		}
	});
}

function addVenues( venues, parent ) 
{
	var roomtext = "";
	
	for( i in venues )
	{
		name = venues[i].name;
		if ( parent )
		{ id = parent + "_" + venues[i].id; }
		else
		{ id = venues[i].id; }
		
		description = ""
		if(venues[i].description)
		{ description = venues[i].description; }
		
		roomtext = "<div class=\"grid_4 level_" + level + "\" + id=\"" + id + "\">" +
			"<div class=\"roomblock\">" +
				"<p>" + name + "</p>" +
			"</div></div>";
		$("#browse").html( $("#browse").html() + roomtext );
		
		if(venues[i].floors)
		{
			addVenues( venues[i].floors, parent = id );
		}
		else if( venues[i].rooms )
		{
			addVenues( venues[i].rooms, parent = id );
		}
		
		$("#"+id).click( createNavigateToFunction( venues[i] ) )
	}
}

function readyFunction()
{
	bindButtons();
	$.getJSON( BASE_URL, function(v){ addVenues( v, "" ); } ); //Adds things to the Browse page.
}

$(document).ready( readyFunction );