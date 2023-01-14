import os
import sys

from azure.mgmt.compute import ComputeManagementClient

managed_disk = ComputeManagementClient.disks.get('AmaroResource', 'myDisk')

async_snapshot_creation = ComputeManagementClient.snapshots.begin_create_or_update(
        'my_resource_group',
        'mySnapshot',
        {
            'location': 'westus',
            'creation_data': {
                'create_option': 'Copy',
                'source_uri': managed_disk.id
            }
        }
    )
snapshot = async_snapshot_creation.result()
