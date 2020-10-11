"	RenjiSann .vimrc 2020
" Start



" PLUGINS
call plug#begin('~/.vim/plugged')

Plug 'vim-airline/vim-airline'
Plug 'townk/vim-autoclose'


" Themes
Plug 'altercation/vim-colors-solarized'
Plug 'patstockwell/vim-monokai-tasty'
Plug 'joshdick/onedark.vim'
Plug 'octol/vim-cpp-enhanced-highlight'

call plug#end()
"End Plugins

set laststatus=2					"Change downLine
set background=dark
colorscheme onedark					"Change colorTheme


set nu						"Display lines number
set bs=2 					"Set Backspace mode to 2
set noexpandtab				"TAB inserts a tabulation instead of spaces
set hls ic					"searching highlight matching text and ignore case
set autoindent				"Auto indent new lines depending on the one above
set tabstop=4				"Make TAB length equal to 4 spaces
set softtabstop=4			"Set the number of tabs to clear when hitting backspace
set shiftwidth=4			"Set the indent shift width

syntax enable

" Section : Auto-Close
" function ClosePair(char)
"   if getline('.')[col('.') - 1] == a:char
"     return "\<Right>"
"   else
"     return a:char
"   endif
" endf
" 
" function AutoClose(enabled)
"   if (a:enabled)
"     inoremap ( ()<ESC>i
"     inoremap ) <C-r>=ClosePair(')')<CR>
"     inoremap { {}<ESC>i
"     inoremap } <C-r>=ClosePair('}')<CR>
"     inoremap [ []<ESC>i
"     inoremap ] <C-r>=ClosePair(']')<CR>
"   else
"     iunmap (
"     iunmap )
"     iunmap {
"     iunmap }
"     iunmap [
"     iunmap ]
"   endif
" endfunction
" 
" command AutoCloseEnable  call AutoClose(1)
" command AutoCloseDisable call AutoClose(0)
" AutoCloseEnable
" End Section : Auto-Close



" End
" ## added by OPAM user-setup for vim / base ## 93ee63e278bdfc07d1139a748ed3fff2 ## you can edit, but keep this line
let s:opam_share_dir = system("opam config var share")
let s:opam_share_dir = substitute(s:opam_share_dir, '[\r\n]*$', '', '')

let s:opam_configuration = {}

function! OpamConfOcpIndent()
  execute "set rtp^=" . s:opam_share_dir . "/ocp-indent/vim"
endfunction
let s:opam_configuration['ocp-indent'] = function('OpamConfOcpIndent')

function! OpamConfOcpIndex()
  execute "set rtp+=" . s:opam_share_dir . "/ocp-index/vim"
endfunction
let s:opam_configuration['ocp-index'] = function('OpamConfOcpIndex')

function! OpamConfMerlin()
  let l:dir = s:opam_share_dir . "/merlin/vim"
  execute "set rtp+=" . l:dir
endfunction
let s:opam_configuration['merlin'] = function('OpamConfMerlin')

let s:opam_packages = ["ocp-indent", "ocp-index", "merlin"]
let s:opam_check_cmdline = ["opam list --installed --short --safe --color=never"] + s:opam_packages
let s:opam_available_tools = split(system(join(s:opam_check_cmdline)))
for tool in s:opam_packages
  " Respect package order (merlin should be after ocp-index)
  if count(s:opam_available_tools, tool) > 0
    call s:opam_configuration[tool]()
  endif
endfor
" ## end of OPAM user-setup addition for vim / base ## keep this line
" ## added by OPAM user-setup for vim / ocp-indent ## a2a13cf3f40489342f8b7e2ba2a9e663 ## you can edit, but keep this line
if count(s:opam_available_tools,"ocp-indent") == 0
  source "/home/renji/.opam/default/share/ocp-indent/vim/indent/ocaml.vim"
endif
" ## end of OPAM user-setup addition for vim / ocp-indent ## keep this line
