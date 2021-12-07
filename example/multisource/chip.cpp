#include <iostream>
#include <sstream>

#include "chip.h"

std::string chip::unpack(const pack_t &in)
{
	std::string out;

	size_t counter = 0;

	for (auto row : in) {
		out += std::to_string(counter++) + ":\t[";
		for (auto i : row)
			out += (i ? "1" : "0");

		out += "]";
		if (counter == in.size())
			break;

		out += "\n";
	}

	return out;
}

chip::chip(const std::string &str, const specs &in, const specs &out)
	: name(str), input(in), output(out) {}

chip::chip(const std::string &str, const specs &in, const specs &out, const circuit &c)
	: name(str), input(in), output(out), type(l_immediate)
{
	functor = c;
}

size_t chip::pins() const
{
	size_t counter = 0;

	for (size_t i : input)
		counter += i;

	for (size_t i : output)
		counter += i;

	return counter;
}

size_t chip::pins_in() const
{
	size_t counter = 0;

	for (size_t i : input)
		counter += i;

	return counter;
}

size_t chip::pins_out() const
{
	size_t counter = 0;

	for (size_t i : output)
		counter += i;

	return counter;
}

const specs &chip::specs_in() const
{
	return input;
}

const specs &chip::specs_out() const
{
	return output;
}

std::string chip::print(const pack_t &in) const
{
	std::ostringstream oss;

	pack_t out = get(in);

	size_t len = name.length() + 2;

	oss << '+' << std::string(len, '-') << '+' << std::endl;
	oss << "| " << name << " |" << std::endl;
	oss << '+' << std::string(len, '-') << '+';

	return oss.str();
}

const pack_t &chip::get(const pack_t &in) const
{
        if (type != l_immediate) {
                std::cout << "[CHIP]: Only immediate modes are available." << std::endl;
                return in;
        }

        pack_t *out = new pack_t(output.size());

        for (size_t i = 0; i < output.size(); i++)
                (*out)[i].assign(output[i], false);

        functor(in, *out);

        return *out;
}

const pack_t &chip::operator()(const pack_t &in) const
{
        if (type != l_immediate) {
                std::cout << "[CHIP]: Only immediate modes are available." << std::endl;
                return in;
        }

        pack_t *out = new pack_t(output.size());

        for (size_t i = 0; i < output.size(); i++)
                (*out)[i].assign(output[i], false);

        functor(in, *out);

        return *out;
}
