for f in test*; do
    if [ -d "$f" ]; then
        echo "$f is a directory"
        cd $f
        echo `pwd`
        bash -x ./launch.sh
       cd .. 
       sleep 2
    fi
done
