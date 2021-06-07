// get list of referance items from database
var itemList = [];
fetch("/getitems")
	.then((response) => response.json())
	.then((data) => (itemList = data.item_list));

// suggest items from list
function autocomplete() {}

// var forms = document
// 	.querySelectorAll('[id^="id_testitem_set-"]')
// 	.querySelectorAll("[id$=part_description]");
