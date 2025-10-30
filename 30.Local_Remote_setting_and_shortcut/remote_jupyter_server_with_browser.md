
https://stackoverflow.com/questions/69244218/how-to-run-a-jupyter-notebook-through-a-remote-server-on-local-machine

1) in server 

jupyter notebook --no-browser --port=9999

2) in windows powder terminal 

ssh -NfL localhost:9999:localhost:9999 gao@192.168.1.189

# only once
# 3) in sever 2nd termina
#jupyter server list >> text.txt

4)  http://localhost:9999/
and input torken and creat a password