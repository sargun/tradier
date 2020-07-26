.PHONY: all
all: libraries/python/urllib3 libraries/python/asyncio

SPECS := $(wildcard specs/*)
libraries/python/urllib3: $(SPECS) Makefile
	rm -rf libraries/python/urllib3
	openapi-generator generate -i ./specs/tradier.yaml -g python --additional-properties projectName=tradier_urllib3 -o libraries/python/urllib3 --package-name tradier_urllib3

libraries/python/asyncio: $(SPECS) Makefile
	rm -rf libraries/python/asyncio
	openapi-generator generate -i ./specs/tradier.yaml -g python --additional-properties projectName=tradier_asyncio,library=asyncio --library asyncio -o libraries/python/asyncio --package-name tradier_asyncio
