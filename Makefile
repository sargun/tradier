.PHONY: all
all: libraries/python/urllib3 libraries/python/asyncio

SPECS := $(wildcard specs/*)
libraries/python/urllib3: $(SPECS) Makefile
	rm -rf libraries/python/urllib3
	openapi-generator generate -i ./specs/tradier.yaml -g python -o libraries/python/urllib3 --package-name tradier_urllib3 -p library=urllib3 -p projectName=tradier_urllib3

libraries/python/asyncio: $(SPECS) Makefile
	rm -rf libraries/python/asyncio
	openapi-generator generate -i ./specs/tradier.yaml -g python -o libraries/python/asyncio --package-name tradier_asyncio -p library=asyncio -p projectName=tradier_asyncio
