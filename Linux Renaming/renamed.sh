#! /bin/bash

if [ ! -r _e -a ! -r _c ]; then echo $4 > _e; echo $3 > _s; echo $2 > _c ; echo $1 > _n; 
	find . -name "*.$(cat _e)" -print0 | xargs -0 -I{} bash -c 'mv -n "{}" "$(cat _n) $(cat _c).$(cat _e)";
	echo $[ $(cat _c) + $(cat _s) ] > _c'; rm -f _e _c _n _s;
fi

