autocmd BufWritePost *.html silent !python3 generate.py
autocmd BufWritePost *.css silent !python3 generate.py
autocmd BufReadPost  *.html set spell
