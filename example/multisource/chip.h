#ifndef CHIP_H_
#define CHIP_H_

#include <bitset>
#include <functional>
#include <string>
#include <vector>

// Typedefs
typedef std::vector <std::vector <bool>> pack_t;
typedef std::vector <bool> row;
typedef std::vector <size_t> specs;
typedef std::function <void (const pack_t &, pack_t &)> circuit;

/* Display Examples (ASCII)

   +-----+
   |     |
1 -+     |
   | and +- 1
1 -+     |
   |     |
   +-----+
   
   +----+
   |    |
0 -+    |
   | or +- 1
1 -+    |
   |    |
   +----+
   
   +-----+
   |     |
1 -+ not +- 0
   |     |
   +-----+

*/

/**
 * @brief Represents an
 * arbitrary chip, with
 * I as input and O as
 * output.
 */
class chip {
public:
	enum label {
		l_immediate,
		l_graph,
	};

	struct node {
		specs bits_in;
		specs bits_out;
		circuit transformer;
	};

	static std::string unpack(const pack_t &);
protected:
	specs input;
	specs output;

private:
	label type;

	node *graph;
	
	circuit functor;

	std::string name;
public:
	chip(const std::string &);

	chip(const std::string &, const specs &, const specs &);
	chip(const std::string &, const specs &, const specs &, const circuit &);

	size_t pins() const;
	size_t pins_in() const;
	size_t pins_out() const;

	const specs &specs_in() const;
	const specs &specs_out() const;

	std::string print(const pack_t &) const;

	const pack_t &get(const pack_t &) const;
	const pack_t &operator()(const pack_t &) const;
};

#endif
