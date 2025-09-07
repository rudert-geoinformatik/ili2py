MODEL_TARGETS=$(shell find ./models -type f -name "*.ili" | sed 's/.ili$$/.imd/')
ILI2C_EXECUTABLE ?= ili2c


$(MODEL_TARGETS):
	$(ILI2C_EXECUTABLE) -oIMD16 --out "$@" $(subst .imd,.ili,"$@")

.PHONY: recreate-imd
recreate-imd: $(MODEL_TARGETS)

clean-all:
	rm -f $(MODEL_TARGETS)
