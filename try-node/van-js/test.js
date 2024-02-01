// function range(from, to) {
// 	let r = Object.create(range.methods);

// 	r.from = from;
// 	r.to = to;

// 	return r;
// }

// range.methods = {
// 	includes(x) { return this.from <= x && x <= this.to; },
// 	*[Symbol.iterator]() {
// 		for (let x = Math.ceil(this.from); x <= this.to; x ++) yield x;
// 	},

// 	toString() { return "(" + this.from + "..." + this.to + ")"; }
// }


//older way to create classes
// function Range(from, to) {
// 	this.from = from;
// 	this.to = to;
// }

// Range.prototype = {
// 	includes: function(x) {return this.from <= x && x <= this.to},
// 	[Symbol.iterator]: function*() {
// 		for (let x = Math.ceil(this.from); x <= this.to; x++) yield x;
// 	},
// 	toString: function() { return `(${this.from} ... ${this.to})`; }
// }



class Range {
	constructor(from, to) {
		this.from = from;
		this.to = to;
	}

	includes(x) {
		return this.from <= x && x <= this.to
	}

	*[Symbol.iterator]() {
		for (let x = Math.ceil(this.from); x <= this.to; x++) {
			yield x;
		}
	}

	toString() {return `(${this.from}...${this.to})`}

	static parse(s) {
		let matches = s.match(/^\((\d+)\.\.\.(\d+)\)$/);
		if (!matches) {
			throw new TypeError(`Cannot parse Range from "${s}".`)
		}
		return new Range(parseInt(matches[1]), parseInt(matches[2]));
		}
}

let r = new Range(1, 60000)
console.log(r instanceof Range)

class Complex {
	constructor (real, imaginary) {
		this.real = real;
		this.imaginary = imaginary;
	}

	plus(other) {
		return new Complex(this.real + other.real, this.imaginary + other.imaginary)
	}
}