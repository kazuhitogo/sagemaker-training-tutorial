import subprocess, os, json
from time import sleep
from icecream import ic

output_dir = os.environ.get('SM_OUTPUT_DIR')
ic(output_dir)
output_data_dir = os.environ.get('SM_OUTPUT_DATA_DIR')
ic(output_data_dir)
output_intermediate_dir = os.environ.get('SM_OUTPUT_INTERMEDIATE_DIR')
ic(output_intermediate_dir)
model_dir = os.environ.get('SM_MODEL_DIR')
ic(model_dir)

channels_list = json.loads(os.environ.get('SM_CHANNELS'))
ic(channels_list)
channels_dict = {}
for channel in channels_list:
    channels_dict[channel] = os.environ.get(f'SM_CHANNEL_{channel.upper()}')
ic(channels_dict)

# * SM_CHANNEL_{channel_name}
hps = json.loads(os.environ.get('SM_HPS'))
ic(hps)
# * SM_HP_{hyperparameter_name}
gpus = os.environ.get('SM_NUM_GPUS')
ic(gpus)
cpus = os.environ.get('SM_NUM_CPUS')
ic(cpus)



def exec_cmd(cmd):
    res = subprocess.run(cmd.split(' '),stdout=subprocess.PIPE)
    print(f'result : {cmd}')
    print(res.stdout.decode('utf-8'))

with open(os.path.join(output_dir,'output.txt'),'wt') as f:
    f.write(os.path.join(output_dir,'output.txt'))

with open(os.path.join(output_data_dir,'data.txt'),'wt') as f:
    f.write(os.path.join(output_data_dir,'data.txt'))

with open(os.path.join(model_dir,'model.txt'),'wt') as f:
    f.write(os.path.join(model_dir,'model.txt'))

with open(os.path.join(output_intermediate_dir,'1.txt'),'at') as f:
    f.write('a')
sleep(1)
with open(os.path.join(output_intermediate_dir,'1.txt'),'at') as f:
    f.write('b')
sleep(60)
with open(os.path.join(output_intermediate_dir,'1.txt'),'at') as f:
    f.write('c')
with open(os.path.join(output_intermediate_dir,'1.txt'),'wt') as f:
    f.write('d')
with open(os.path.join(output_intermediate_dir,'2.txt'),'at') as f:
    f.write('e')
    
exec_cmd('pip freeze')
exec_cmd('printenv')
exec_cmd('df -h')
exec_cmd('whoami')
exec_cmd('pwd')
exec_cmd('which python')
exec_cmd('python -version')
exec_cmd('cat /proc/version')
exec_cmd('findmnt')
exec_cmd('ls -la /opt/ml/')
exec_cmd('ls -la /opt/ml/input/')
exec_cmd('ls -la /opt/ml/input/config/')
exec_cmd('ls -la /opt/ml/code/')
exec_cmd('ls -la /opt/ml/errors/')
exec_cmd('ls -la /opt/ml/model/')
exec_cmd('ls -la /opt/ml/output/')
exec_cmd('ls -la /opt/ml/output/data/')
exec_cmd('ls -la /opt/ml/output/intermediate/')
exec_cmd('cat /opt/ml/input/config/debughookconfig.json')
exec_cmd('cat /opt/ml/input/config/hyperparameters.json')
exec_cmd('cat /opt/ml/input/config/init-config.json')
exec_cmd('cat /opt/ml/input/config/inputdataconfig.json')
exec_cmd('cat /opt/ml/input/config/metric-definition-regex.json')
exec_cmd('cat /opt/ml/input/config/profilerconfig.json')
exec_cmd('cat /opt/ml/input/config/resourceconfig.json')
exec_cmd('cat /opt/ml/input/config/trainingjobconfig.json')
exec_cmd('cat /opt/ml/input/config/upstreamoutputdataconfig.json')


exec_cmd('ls -la /tmp/')
exec_cmd('mount -l')


exit()