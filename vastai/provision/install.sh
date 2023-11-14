pip install --upgrade vastai;

set -ex

export AIHOME=~/.virtualenvs/ai

# rm -rf $AIHOME

# pip3 install pew
pew new ai -d 
pew in ai pip3 install  ipython vastai --upgrade

pushd $AIHOME

popd

pew workon ai
