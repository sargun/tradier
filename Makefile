all: tradier_python
tradier_python: $(wildcard specs/*)
	openapi-generator generate -i ./specs/tradier.yaml -g python --package-name tradier_python -p generateSourceCodeOnly=true
