#ifndef CLOCK_H_
#define CLOCK_H_

#include <chrono>
#include <thread>

#include "aug_chip.h"
#include "chip.h"

// Sequential chips
namespace sequential {
	
	const double eps = 1E-10;

	/* =======================
	 * Clock memory structure
	 * =======================
	 *
	 * Contains a boolean for the
	 * actual signal, and a thread
	 * that mutates it every [millis]
	 * milliseconds. */
	template <size_t millis>
	struct clk_mem {
		bool go;
		std::thread timer;

		clk_mem() : go(true) {
			timer = std::thread([&] {
				while (true) {
					go = false;
					std::this_thread::sleep_for
							(std::chrono::milliseconds(millis));
					
					go = true;
					std::this_thread::sleep_for
							(std::chrono::milliseconds(millis));
				}
			});
		}

		~clk_mem() {
			timer.detach();
		}
	};

	/* ===========
	 * Clock class
	 * ===========
	 *
	 * Sends a high signal with a
	 * period of [2 * millis] milliseconds
	 * for a duraction of [millis]
	 * milliseconds. */
	template <size_t millis>
	class clk : public aug_chip <clk_mem <millis> *> {
	public:
		clk() : aug_chip <clk_mem <millis> *> ("clock", {1}, {1},
			[&](const pack_t &in, pack_t &out, clk_mem <millis> *data) {
				if (data->go)
					out[0][0] = true;
				else
					out[0][0] = false;
			}, new clk_mem <millis> ()) {}

		~clk() {
			delete this->data;
		}

		bool operator()() const {
			return this->data->go;
		}
	};

	template <size_t millis>
	struct dff_mem {
		bool go;
		bool prev;
		std::thread timer;

		dff_mem() : go(true) {
			timer = std::thread([&] {
				while (true) {
					go = false;
					std::this_thread::sleep_for
							(std::chrono::milliseconds(millis));
					
					go = true;
					std::this_thread::sleep_for
							(std::chrono::milliseconds(millis));
				}
			});
		}

		~dff_mem() {
			timer.detach();
		}
	};
	
	template <size_t millis>
	class dff : public aug_chip <dff_mem <millis> *> {
	public:
		dff() : aug_chip <dff_mem <millis> *> ("flip-flop", {1}, {1},
			[&](const pack_t &in, pack_t &out, clk_mem <millis> *data) {
				out[0][0] = false;

				if (data->go) {
					out[0][0] = data->prev;
					data->prev = in[0][0];
				}
			}, new dff_mem <millis> ()) {}

		~dff() {
			delete this->data;
		}

		bool operator()(const pack_t &in) const {
			return this->get(in)[0][0];
		}
	};
}

#endif
