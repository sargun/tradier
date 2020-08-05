.PHONY: all
all: libraries/python/urllib3 libraries/python/asyncio libraries/go

SPECS := $(wildcard specs/*)
libraries/python/urllib3: $(SPECS) Makefile
	rm -rf libraries/python/urllib3
	openapi-generator generate -i ./specs/tradier.yaml -g python --additional-properties projectName=tradier_urllib3 -o libraries/python/urllib3 --package-name tradier_urllib3

libraries/python/asyncio: $(SPECS) Makefile
	rm -rf libraries/python/asyncio
	openapi-generator generate -i ./specs/tradier.yaml -g python --additional-properties projectName=tradier_asyncio,library=asyncio --library asyncio -o libraries/python/asyncio --package-name tradier_asyncio

libraries/go: $(SPECS) Makefile
	rm -rf libraries/go
	openapi-generator generate -i ./specs/tradier.yaml -g go --package-name tradier -o libraries/go --additional-properties projectName=tradier --git-user-id sargun --git-repo-id tradier
