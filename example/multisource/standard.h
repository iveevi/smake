#ifndef STANDARD_H_
#define STANDARD_H_

#include "chip.h"

/* This file contains common
 * chips, for the convenience of
 * other users: instead of having
 * to create these chips from
 * bottom up, they can use higher
 * level chips or the chip they want
 * to make itself. */

namespace combinational {

	class __not : public chip {
	public:
		__not() : chip("not", {1}, {1}, [](const pack_t &in, pack_t &out) {
			out[0][0] = !in[0][0];
		}) {}
	};


	class __and : public chip {
	public:
		__and() : chip("and", {2}, {1}, [](const pack_t &in, pack_t &out) {
			out[0][0] = in[0][0] & in[0][1];
		}) {}
	};

	class __or : public chip {
	public:
		__or() : chip("or", {2}, {1}, [](const pack_t &in, pack_t &out) {
			out[0][0] = in[0][0] | in[0][1];
		}) {}
	};

}

#endif
