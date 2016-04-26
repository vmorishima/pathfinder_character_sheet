///**
// * Created by wmorishima on 4/25/2016.
// */
//$(function() {
//    $( "#roll20" ).click(function() {
//        function roll20(modifier) {
//            return Math.floor(Math.random() * 20) + 1 + modifier;
//        }
//        $( "#output" ).text(roll20(4));
//    });
//});

function roll20(modifier, stat) {
            var num = Math.floor(Math.random() * 20) + 1 + modifier;
            id = stat + 'output';
            console.log(id);
            document.getElementById(id).value=num;
        }

$('.collapse').collapse();