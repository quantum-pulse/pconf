set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'git://git.wincent.com/command-t.git'
Plugin 'rust-lang/rust.vim'
Plugin 'peterhoeg/vim-qml'
call vundle#end()            " required

set tags=tags,./tags

set rtp+=~/.vim/bundle/The-NERD-tree
set rtp+=~/.vim/bundle/taglist.vim
set rtp+=~/.vim/bundle/YouCompleteMe
set rtp+=~/.vim/bundle/Conque-GDB
set rtp+=~/.vim/bundle/taglist-plus
set rtp+=~/.vim/bundle/Tagbar
set rtp+=~/.vim/bundle/ctrlp.vim
set rtp+=~/.vim/bundle/ProjectTag
set rtp+=~/.vim/bundle/cscope_plus.vim
set rtp+=~/.vim/bundle/autoload_cscope.vim

set number
let Tlist_Use_Right_Window = 1
set tabstop=8 softtabstop=0 expandtab shiftwidth=4 smarttab
filetype plugin indent on

fun! ToggleNERDTreeWithRefresh()
    :NERDTreeToggle
    if(exists("b:NERDTreeType") == 1)
        call feedkeys("R")
    endif
endf

if has('cscope')
  set cscopetag cscopeverbose

  cnoreabbrev csa cs add
  cnoreabbrev csf cs find
  cnoreabbrev csk cs kill
  cnoreabbrev csr cs reset
  cnoreabbrev css cs show
  cnoreabbrev csh cs help

  command -nargs=0 Cscope cs add $VIMSRC/src/cscope.out $VIMSRC/src
endif

map <silent> <c-c> :!$HOME/.vimcustoms/./compiler.py --compile <CR>
map <silent> <c-l> :call ToggleNERDTreeWithRefresh()<cr>
map <silent> <c-l><c-r> :!echo "reloading tags" && ctags -R --c++-kinds=+p --fields=+iaS --extra=+q .<CR>
map <silent> <F3> :NERDTreeToggle <CR>
map <silent> <F4> :TlistToggle <CR>
map <silent> <F5> :grep! "\<<cword>\>" . -irnH --color --include=\*{cpp,cxx,c,h,hxx,hpp}<CR>:copen<CR>
map <silent> <F6> :!$HOME/.vimcustoms/./compiler.py --debug '%:t'<CR>
map <silent> <F7> :!$HOME/.vimcustoms/./compiler.py --val <CR>
map <silent> <F8> :!$HOME/.vimcustoms/./compiler.py '%:p:h' '%:p' <CR>
map <silent> <F9> :!$HOME/.vimcustoms/./compiler.py --args <CR>
