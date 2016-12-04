Ordovim
--------

> OrdoEmacs, on the other hand, works exactly like regular Emacs, except that it encrypts everything before writing it out to disk. At no time is plaintext ever laid down on a disk by OrdoEmacs--the only place it exists in its plain, readable form is in the pixels on the screen, and in the volatile RAM of the computer, whence it vanishes the moment power is shut down. Not only that, but it's coupled to a screensaver that uses the little built-in CCD camera in the laptop to check to see if you are actually there. It can't recognize your face, but it can tell whether or not a vaguely human-shaped form is sitting in front of it, and if that vaguely human-shaped form goes away, even for a fraction of a second, it will drop into a screen-saver that will blank the display and freeze the machine until such time as you type in a password, or biometrically verify your identity through voice recognition.

An (embarrassingly bad) attempt at creating a clone of Ordoemacs from Neal Stephenson's [Cryptonomicon](https://www.goodreads.com/book/show/816.Cryptonomicon) in Vim. It doesn't even come close to what Ordoemacs actually offers, besides the encryption part.

How to use
----------

Ordovim consists of a Python script and a few lines of Vimscript.

1. Clone this repository (which only consists of one Python file).
2. Add the following lines to your .vimrc file:
```Vimscript

function! s:OrdDecrypt()
	! python3 /path/to/ordo.py -d  %
	let fname=expand('%:p:r')
	bwipeout %
	exec 'e '.fname
endfunction

au BufDelete,VimLeave *.ordo !python3 /path/to/ordo.py -e  %
au BufRead *.ordo.enc call s:OrdDecrypt()
```
For encryption:

    1. Open or edit the file to be encrypted with the extension `.ordo`. Close Vim or delete the buffer
    to automatically encrypt the file.
    2. Enter your password at the prompt.
    3. Ensure the file you want to encrypt is in the current buffer when you close or delete the buffer.
    Ordovim only encrypts the file in the current buffer, regardless of where your `.ordo` file is.
Your file will now be encrypted and saved with the extension `.ordo.enc`. The plaintext file is deleted from
disk.

For decryption:

    1. Simply open or edit the file that has the extension `.ordo.enc`.
    2. Enter the password you used at the prompt.
Your file will now be decrypted and opened for editing as a `.ordo` file. The corresponding `.ordo.enc` file 
is deleted after decryption.

Warnings
-------

There might be some strange behaviour that I haven't caught yet. Be careful how you use it!
