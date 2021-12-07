#ifndef AUG_CHIP_H_
#define AUG_CHIP_H_

#include <utility>

#include "chip.h"

template <class T>
class aug_chip : public chip {
public:
	using aug_circuit = std::function
		<void (const pack_t &, pack_t &, T)>;
protected:
	T data;

	aug_circuit afunctor;
public:
	aug_chip(const std::string &, const specs &,
			const specs &, const aug_circuit &, T);

	const pack_t &get(const pack_t &);
	const pack_t &operator()(const pack_t &);
};

template <class T>
aug_chip <T> ::aug_chip(const std::string &str, const specs &ins,
		const specs &outs, const aug_circuit &cs, T init)
		: chip(str, ins, outs), afunctor(cs), data(init) {}

template <class T>
const pack_t &aug_chip <T> ::get(const pack_t &in)
{
        pack_t *out = new pack_t(output.size());

        for (size_t i = 0; i < output.size(); i++)
                (*out)[i].assign(output[i], false);

        afunctor(in, *out, data);

        return *out;
}

template <class T>
const pack_t &aug_chip <T> ::operator()(const pack_t &in)
{
        pack_t *out = new pack_t(output.size());

        for (size_t i = 0; i < output.size(); i++)
                (*out)[i].assign(output[i], false);

        afunctor(in, *out, data);

        return *out;
}

#endif
