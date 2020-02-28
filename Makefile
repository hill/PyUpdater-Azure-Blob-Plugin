.PHONY: build deploy deploy-test

build: clean
	python setup.py sdist bdist_wheel

deploy-test: clean build
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

deploy: clean build
	git push
	twine upload dist/*

clean:
	rm -rf ./build
	rm -rf ./dist
	rm -rf ./PyUpdater_Azure_Blob_Plugin.egg-info