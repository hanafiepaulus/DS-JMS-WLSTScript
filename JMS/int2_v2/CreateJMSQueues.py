connect("weblogic", "welcome1", "t3://10.87.225.161:10201")
edit()
startEdit()

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
