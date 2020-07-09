tradier_python: ./specs/tradier.yaml
	openapi-generator generate -i ./specs/tradier.yaml -g python --package-name tradier_python -p generateSourceCodeOnly=true
