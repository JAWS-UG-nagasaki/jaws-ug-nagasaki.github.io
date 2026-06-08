.PHONY: help html clean serve devserver publish

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                '
	@echo '   make html                           (re)generate the web site      '
	@echo '   make clean                          remove the generated files     '
	@echo '   make serve [PORT=8000]               serve site at http://localhost:PORT'
	@echo '   make devserver [PORT=8000]           start/restart develop_server.sh'
	@echo '   make publish                        generate using production settings'
	@echo '                                                                       '

html:
	source .venv/bin/activate && pelican content -s pelicanconf.py

clean:
	[ ! -d output ] || rm -rf output

serve:
	cd output && python3 -m http.server $(PORT)

devserver:
	$(MAKE) clean
	$(MAKE) html
	$(MAKE) serve

publish:
	source .venv/bin/activate && pelican content -s publishconf.py
