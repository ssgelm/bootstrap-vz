from bootstrapvz.base import Task
from bootstrapvz.common import phases

class AddLVMToHost(Task):
	description = 'Adding commands required for LVM'
	phase = phases.preparation
	successors = [host.CheckExternalCommands]

	@classmethod
	def run(cls, info):
        info.host_dependencies['lvm2'] = 'lvm2'

class AddLVMPackage(Task):
	description = 'Adding LVM Package'
	phase = phases.preparation

	@classmethod
	def run(cls, info):
		info.packages.add('lvm2')
		info.packages.add('parted')

# Create LVM VG and LV

# Set root partition to LVM partition

# Fix grub?

# Fix fstab?

# Put expand-volume startup script in place

# Make sure unmount works?

