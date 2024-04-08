#!/usr/bin/node
// a script that prints a message depending of the number of arguments passed

if (Process.argv.length === 2) {
	console.log('No argument');
} else if (Process.argv.length === 3) {
	console.log('Argument found');
} else {
	console.log('Argument found');
}
