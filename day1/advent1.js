#!/usr/bin/node


function getsum(seq, length, dist)
{
	var sum = 0;
	for(var i = 0; i < length; i++)
	{
		var j = (i + dist) % length;
		if(seq[i] == seq[j])
			sum += parseInt(seq[i]);
	}
	return sum;
}

var fs = require('fs');
var seq = fs.readFileSync("input.txt", 'utf8').replace(/\s*$/, '');
var length = seq.length;

console.log(getsum(seq, length, 1));
console.log(getsum(seq, length, length / 2));
