fcitx5-table-lekhika =>  nepali input method for fcitx

##Description

Lekhika (https://khumnath.com.np/posts/2023-11-27-post3) table for fcitx.   
testing on browser is available now at https://khumnath.com.np/lekhika.js/

##How to install

if you can manage to install fcitx devlopment packeges
```bash
mkdir build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
make
sudo make install
```
if you want to just install
download https://github.com/khumnath/fcitx5-table-lekhika/files/13526606/release.zip and run install.sh .

## Roadmap

- [x] basic nepali typing.
- [x] create table maker script.
- [X] create html5 input with lekhika schemes.
- [ ] make installable package.
- [ ] add word prediction.
- [ ] add more dictionary.
- [ ] and more to do as i experiment.:smile:

## problems

 main branch is now fully working. i am testing with words suggestion table. some autocorrect words are disturbing typing. i am working on it.

## contribution

contributions are welcome. dictionary and other improvements can be made as find difficulties when typing.
