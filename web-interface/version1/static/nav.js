$("body").append("<div class=\"nav\" style=\"-webkit-backdrop-filter: blur(10px); z-index: 5; background-color: rgba(0,0,0,0.5); display: flex; align-items: center; justify-content: center; height: 100vh; width:100vw; position: absolute; top:-105%; left:0;\"><div class=\"apps\"><div class=\"app\" id=\"overview-link\"><h4>RINGS</h4></div><div class=\"app\" id=\"line-link\"><h4>LINE</h4></div><div class=\"app\" id=\"scatter-link\"><h4>SCATTER</h4></div></div></div>");
$("body").append("<div id=\"nav-icon4\"><span></span><span></span><span></span></div>");

	$(".app").on( "mouseover", function() {
		$(this).addClass("outline-border");
	});
	$(".app").on( "mouseout", function() {
		$(this).removeClass("outline-border");
	});
	$("#overview-link").on( "click", function() {
		window.location.href = "/version1/overview";
	});
	$("#line-link").on( "click", function() {
		window.location.href = "/version1/linegraph";
	});
	$("#scatter-link").on( "click", function() {
		window.location.href = "/version1/scatterplot";
	});
	$(document).ready(function(){
		var navOpen = false;
		$('#nav-icon1,#nav-icon2,#nav-icon3,#nav-icon4').click(function(){
			$(this).toggleClass('open');
			if(navOpen == true){
				$(".nav").animate({
			    top: "-105%",
			  }, {
				    duration: 700,
				    specialEasing: {
				      top: "easeInOutCubic"
				    }}, function() {
			    
			  });

				navOpen = false;
			}else{
				$(".nav").animate({
			    top: "0",
			  }, {
				    duration: 700,
				    specialEasing: {
				      top: "easeInOutCubic"
				    }}, function() {
			    
			  });
				navOpen = true;
			}
		});
	});