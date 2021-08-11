#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")
value = cmd.split()
if value[0] == "1":
    deployment_name = value[2]
    image_name = value[1]
    cmd = "kubectl create deployment " + (deployment_name) + " --image=" + (image_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)
elif value[0] == "2":
    pod_name = value[2]
    image_name = value[1]
    cmd = "kubectl run " + (pod_name) + " --image=" + (image_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)
elif value[0] == "3":
    pod_name = value[1]
    cmd = "kubectl delete pod " + (pod_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)
elif value[0] == "4":
    deployment_name = value[1]
    cmd = "kubectl delete deployment " + (deployment_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)
elif value[0] == "5":
    deployment_name = value[1]
    port_no = value[2]
    Expose_type =  value[3]
    cmd = "kubectl expose deployment " + (deployment_name) + " --port=" + (port_no) + " --type=" + (Expose_type)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)
elif value[0] == "6":
    deployment_name = value[1]
    replica = value[2]
    cmd = "kubectl scale deployment " + (deployment_name) + " --replicas=" + (replica)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)
elif value[0] == "7":
    cmd = "sudo kubectl get pods --kubeconfig admin.conf"
    output = subprocess.getoutput(cmd)
    print(output)
elif value[0] == "8":
    cmd = "kubectl get deployments --kubeconfig admin.conf"
    output = subprocess.getoutput("sudo " + cmd)
    print(output)
elif value[0] == "9":
    cmd = "kubectl get svc --kubeconfig admin.conf"
    output = subprocess.getoutput(cmd)
    print(output)
elif value[0] == "10":
    cmd = "kubectl delete all --all --kubeconfig admin.conf"
    output = subprocess.getoutput("sudo " + cmd)
    print(output)
elif value[0] == "404":
    print("command not found")
