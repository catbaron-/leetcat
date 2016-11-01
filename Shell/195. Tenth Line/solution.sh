# How would you print just the 10th line of a file?

# For example, assume that file.txt has the following content:
#  Line 1
#  Line 2
#  Line 3
#  Line 4
#  Line 5
#  Line 6
#  Line 7
#  Line 8
#  Line 9
#  Line 10
# Your script should output the tenth line, which is:
#  Line 10

# Read from the file file.txt and output the tenth line to stdout.
lines=$(wc -l file.txt|cut -d " " -f1)
if [ 10 -gt $lines ]
then
	echo ""
else
	head -10 file.txt|tail -1
fi
