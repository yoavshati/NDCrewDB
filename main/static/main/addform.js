var itemName = document.getElementById("id_part_description");
var itemList = [];

itemName.setAttribute("list", "part-list");
itemName.setAttribute("onkeyup", "updateDataList(itemName,itemList)");
itemName.setAttribute("onchange", "fillFields()");

fetch("/getitems")
	.then((response) => response.json())
	.then((data) => (itemList = data.item_list));

// on keyup of part input
function updateDataList(element = itemName, list = itemList) {
	let searchName = element.value;
	let shortList = [];
	let options = "";
	let i = 0;

	while (i <= 9 && i < list.length) {
		if (list[i].includes(searchName)) {
			shortList.push(list[i]);
		}
		i += 1;
	}

	for (let name of shortList) {
		options += `<option value="${name}">`;
	}

	document.getElementById("part-list").innerHTML = options;
}

// on change of part input
async function fillFields() {
	try {
		const response = await fetch("/getitem/" + itemName.value);
		const data = await response.json();

		document.getElementById("id_test_method").value = data.test_method;
		document.getElementById("id_literature_code").value = data.literature_code;
		document.getElementById("id_testing_hours").value = data.testing_hours;
	} catch {}
}
