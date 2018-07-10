#!/usr/local/bin/ruby

seq = File.read("input.txt").rstrip()
length = seq.length

sum = 0
i = 0
while i <= length - 1
	j = (i + 1) % length
	if seq[i] == seq[j]
		sum += Integer(seq[i])
	end
	i += 1
end
puts sum

sum = 0
i = 0
half = length / 2
while i <= length - 1
	j = (i + half) % length
	if seq[i] == seq[j]
		sum += Integer(seq[i])
	end
	i += 1
end
puts sum
