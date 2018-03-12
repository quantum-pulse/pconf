set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'git://git.wincent.com/command-t.git'
Plugin 'rust-lang/rust.vim'
call vundle#end()            " required

set tags=./TAGS

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

filetype plugin indent on   

map <silent> <F3> :NERDTreeToggle <CR>
map <silent> <F4> :TlistToggle <CR>
map <silent> <F6> :!/home/rking/.vimcustoms/./compiler.py --gdb <CR>
map <silent> <F7> :!/home/rking/.vimcustoms/./compiler.py --val <CR>
map <silent> <F8> :!/home/rking/.vimcustoms/./compiler.py '%:p:h' <CR>
