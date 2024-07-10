from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import subprocess


def run_scripts_asynchronously(script_directory, scripts):

    total = len(scripts)
    channel_layer = get_channel_layer()
    for i, script in enumerate(scripts):
        progress = (i + 0.5) / total * 100
        async_to_sync(channel_layer.group_send)(
            'progress_group',  # This must match the group name used in the consumer
            {
                'type': 'progress_message',  # This must match the handler method name in the consumer
                'progress': progress
            }
        )


        subprocess.run(['python', script], cwd=script_directory)
        progress = (i + 1) / total * 100
        async_to_sync(channel_layer.group_send)(
            'progress_group',  # This must match the group name used in the consumer
            {
                'type': 'progress_message',  # This must match the handler method name in the consumer
                'progress': progress
            }
        )


def run_scripts_asynchronously2(script_directory, scripts):

    total = len(scripts)
    channel_layer = get_channel_layer()
    for i, script in enumerate(scripts):
        process = subprocess.Popen(['python', script], cwd=script_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        #print(process.stdout)
        for line in process.stdout:
            print(line)
            if line.startswith("Completed: "):
                # Parse the progress from the line
                progress = float(line.split(":")[1].strip()[:-1])
                #print(progress)
                async_to_sync(channel_layer.group_send)(
                    'progress_group',  # This must match the group name used in the consumer
                    {
                        'type': 'progress_message',  # This must match the handler method name in the consumer
                        'progress': progress
                    }
                )


