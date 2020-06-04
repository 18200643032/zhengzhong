import sys
import os
def docker_run(path):
    docker_cmd = "docker run -itd  --privileged -v /dockerdata/AppData:/data -v /zhengzhong:/zhengzhong  -e LANG=C.UTF-8 -e NVIDIA_VISIBLE_DEVICES=all %s /bin/bash >>1.txt" % path
    os.system(docker_cmd)
    with open('1.txt','r') as f:
        docker_id = f.readlines()[-1][0:6]
    print(docker_id)
    docker_into = "docker exec -it %s python3 /zhengzhong/1.py" % (docker_id)
    os.system(docker_into)
docker_run(sys.argv[1])

