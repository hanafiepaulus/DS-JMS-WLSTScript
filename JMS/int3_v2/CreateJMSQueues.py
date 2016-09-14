connect("weblogic", "welcome1", "t3://10.87.225.160:10501")
edit()
startEdit()

cd('/JMSSystemResources/batchResources/JMSResource/batchResources')
cmo=create('BatchDistributedErrorQueue','UniformDistributedQueue')

cd('/JMSSystemResources/batchResources/JMSResource/batchResources/UniformDistributedQueues/BatchDistributedErrorQueue')
cmo.setJNDIName('dist.jms.queue.batch.error')
cmo.setSubDeploymentName('batchSubdeployment')

cd('/JMSSystemResources/batchResources/JMSResource/batchResources')
cmo=create('BatchDistributedLoadQueue','UniformDistributedQueue')

cd('/JMSSystemResources/batchResources/JMSResource/batchResources/UniformDistributedQueues/BatchDistributedLoadQueue')
cmo.setJNDIName('dist.jms.queue.batch.Load')
cmo.setSubDeploymentName('batchSubdeployment')

cd('/JMSSystemResources/batchResources/JMSResource/batchResources')
cmo=create('BatchDistributedQueue','UniformDistributedQueue')

cd('/JMSSystemResources/batchResources/JMSResource/batchResources/UniformDistributedQueues/BatchDistributedQueue')
cmo.setJNDIName('dist.jms.queue.batch.Request')
cmo.setSubDeploymentName('batchSubdeployment')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources')
cmo=create('SAFErrorQueue','UniformDistributedQueue')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/UniformDistributedQueues/SAFErrorQueue')
cmo.setJNDIName('jms.queue.saf.Error')
cmo.setSubDeploymentName('SAFDeployment')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources')
cmo=create('SMS Alert Queue','UniformDistributedQueue')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/UniformDistributedQueues/SMS Alert Queue')
cmo.setJNDIName('jms.queue.sms.Alert')
cmo.setSubDeploymentName('SAFDeployment')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources')
cmo=create('SAFRetryQueue','UniformDistributedQueue')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/UniformDistributedQueues/SAFRetryQueue')
cmo.setJNDIName('jms.queue.saf.Retry')
cmo.setSubDeploymentName('SAFDeployment')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources')
cmo=create('SAFReversalQueue','UniformDistributedQueue')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/UniformDistributedQueues/SAFReversalQueue')
cmo.setJNDIName('jms.queue.saf.Reversal')
cmo.setSubDeploymentName('SAFDeployment')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources')
cmo=create('SMSAlertHealthStateQueue','UniformDistributedQueue')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/UniformDistributedQueues/SMSAlertHealthStateQueue')
cmo.setJNDIName('jms.queue.sms.AlertHealthState')
cmo.setSubDeploymentName('SAFDeployment')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources')
cmo=create('DCMSAlert','UniformDistributedQueue')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/UniformDistributedQueues/DCMSAlert')
cmo.setJNDIName('jms.queue.dcmssms.Alert')
cmo.setSubDeploymentName('SAFDeployment')

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules')
cmo=create('UpdWNATrxErrorQueue','UniformDistributedQueue')

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules/UniformDistributedQueues/UpdWNATrxErrorQueue')
cmo.setJNDIName('jms.queue.wna.UpdateTrxError')
cmo.setSubDeploymentName('WNADeployment')

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules')
cmo=create('UpdWNATrxQueue','UniformDistributedQueue')

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules/UniformDistributedQueues/UpdWNATrxQueue')
cmo.setJNDIName('jms.queue.wna.UpdateTrx')
cmo.setSubDeploymentName('WNADeployment')

save()
activate()
