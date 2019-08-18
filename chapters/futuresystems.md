# Romeo


Apply for an account on futuresyste,s.org and make sure you uploaded your public key

Than with your `user` name log in as 

```
ssh user@juliet.futuresystems.org
user@juliet.futuresystems.org: Permission denied (publickey,gssapi-keyex,gssapi-with-mic,hostbased).
```


There are two separate GPU partitions in slurm, these can be seen in the
output of the 'sinfo' command:

```
PARTITION  AVAIL  TIMELIMIT  NODES   GRES  STATE NODELIST
romeo         up   infinite      4  gpu:8    mix r-[001-004]
volta         up   infinite      2  gpu:8    mix r-[005-006]
```

* `romeo` partition has K-80 GPUs. 
* `volta` partition has V-100 GPUs

GPUs in these partitions are defined in Slurm as "generic reservable"
items (gres) and seen under the GRES heading.

When allocated by slurm, the environment variables
CUDA_VISIBLE_DEVICES and GPU_DEVICE_ORDINAL are set.

Here is an interactive example using `srun` to allocate 2 GPUs on
node r-005, and start a shell, starting from Juliet login node.

```
ssh user@julia.futuresystems.org
[user@j-login1 ~]$ srun -p volta -w r-005 --gres gpu:2 --pty bash
[user@r-005 ~]$ echo $CUDA_VISIBLE_DEVICES
2,3

[user@r-005 ~]$ echo $GPU_DEVICE_ORDINAL
2,3
```

The values of those environment variables correspond to the GPUs
(`/dev/nvidiaN` devices) allocated. However there is nothing currently
restricting users to their allocated GPUs. We can maybe do this with
cgroups but it is more configuration and may require a Slurm
upgrade. For now it is cooperative.

This would also work for a batch script submitted with the
`sbatch` command. HOWEVER, note that if you allocate a node with
`salloc`, and then use ssh to login to the node, these
environment variables are not set.