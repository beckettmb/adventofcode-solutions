#!/usr/bin/node


var fs = require('fs');
var lines = fs.readFileSync('../input.txt', 'utf8').match(/[^\r\n]+/g);

var checksum = 0;
for(var i = 0; i < lines.length; i++)
{
	var items = lines[i].split('\t');
	var max = items[0];
	var min = items[0];
	for(var j = 1; j < items.length; j++)
	{
		if(parseInt(items[j]) > parseInt(max))
			max = items[j];
		else if(parseInt(items[j]) < parseInt(min))
			min = items[j];
	}
	checksum += parseInt(max) - parseInt(min)
}
console.log(checksum);

checksum = 0;
for(var i = 0; i < lines.length; i++)
{
	var items = lines[i].split('\t');
	for(var j = 0; j < items.length; j++)
	{
		for(var k = 0; k < items.length; k++)
		{
			if(items[j] == items[k])
				continue;
			item1 = parseInt(items[j]);
			item2 = parseInt(items[k]);
			if(item1 > item2)
			{
				if((item1 % item2) == 0)
				{
					checksum += item1 % item2;
					break;
				}
			}
			if(item2 > item1)
			{
				if((item2 % item1) == 0)
				{
					checksum += item2 / item1;
					break;
				}
			}
		}
	}
}
console.log(checksum);
