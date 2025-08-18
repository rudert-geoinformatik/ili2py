MODEL_TARGETS=$(shell find ./models -type f -name "*.ili" | sed 's/.ili$$/.imd/')


$(MODEL_TARGETS):
	ili2c -oIMD16 --out "$@" $(subst .imd,.ili,"$@")

.PHONY: recreate-imd
recreate-imd: $(MODEL_TARGETS)

clean-all:
	rm -f $(MODEL_TARGETS)
