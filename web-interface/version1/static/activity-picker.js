$("body").append("<div class=\"activity-picker-container\"><ul><li data=\"clicks\">Clicks</li><li data=\"keystrokes\">Keystrokes</li><li data=\"Steps\">Steps</li><li data=\"Exercise\">Exercise</li><li data=\"Sleep\">Sleep</li><li data=\"Miles\">Miles</li><li data=\"weight\">Weight</li><li data=\"Safari\">Safari</li><li data=\"Google Chrome\">Chrome</li><li data=\"Songs\">Songs</li><li data=\"iTunes\">iTunes</li><li data=\"Spotify\">Spotify</li><li data=\"Photoshop CC\">Photoshop</li><li data=\"After Effects CC\">After Effects</li><li data=\"Adobe Illustrator CC 2015\">Illustrator</li><li data=\"GitHub Desktop\">GitHub</li><li data=\"Terminal\">Terminal</li><li data=\"Xcode\">Xcode</li><li data=\"Pages\">Pages</li><li data=\"Keynote\">Keynote</li><li data=\"Microsoft Excel\">Excel</li><li data=\"Microsoft Word\">Word</li><li data=\"Messenger\">Messenger</li><li data=\"Mail\">Mail</li><li data=\"Polymail\">Polymail</li><li data=\"Messages\">Messages</li><li data=\"Excel\">Fusion 360</li><li data=\"Finder\">Finder</li></ul></div>");

	$(document).ready(function(){
		var pickerOpen = false;
		var selectedAct;
		$("li").click(function(){
			$(selectedAct).val($(this).attr("data"));
			$(selectedAct).text($(this).attr("data"));
			closePicker();
			$("#other-controls > button").click();
		});
		$('#activity1,#activity2,#activity3').click(function(){
			selectedAct = this;
			togglePicker();
		});
		function closePicker(){
			$(".activity-picker-container").animate({
			    right: "-201.5",
			  }, {
				    duration: 300,
				    specialEasing: {
				      top: "easeInOutCubic"
				    }}, function() {
			    
			  });
				pickerOpen = true;
		}
		function togglePicker(){
			if(pickerOpen == true){
				openPicker();
			}else{
				closePicker();
			}
		}
		function openPicker(){
			$(".activity-picker-container").animate({
			    right: "0px",
			  }, {
				    duration: 300,
				    specialEasing: {
				      top: "easeInOutCubic"
				    }}, function() {
			    
			  });

				pickerOpen = false;
		}
	});