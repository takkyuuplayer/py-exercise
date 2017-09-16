augroup QuickRunGo
  autocmd!

  let g:quickrun_config['python'] = {}
  let g:quickrun_config['python']['command'] = 'make'
  let g:quickrun_config['python']['cmdopt'] = 'run'
  let g:quickrun_config['python']['exec'] = '%c %o SRC=@%'
augroup END

