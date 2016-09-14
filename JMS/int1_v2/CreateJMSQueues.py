connect("weblogic", "welcome1", "t3://10.87.225.160:10101")
edit()
startEdit()

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule')
cmo=create('TDRateErrorQueue','UniformDistributedQueue')

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule/UniformDistributedQueues/TDRateErrorQueue')
cmo.setJNDIName('jms.bpm.queue.tdrate.error')
cmo.setSubDeploymentName('BPMDeployment')

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule')
cmo=create('TDRateReminderQueue','UniformDistributedQueue')

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule/UniformDistributedQueues/TDRateReminderQueue')
cmo.setJNDIName('jms.bpm.queue.tdrate.reminder')
cmo.setSubDeploymentName('BPMDeployment')

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule')
cmo=create('TDRateResponseQueue','UniformDistributedQueue')

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule/UniformDistributedQueues/TDRateResponseQueue')
cmo.setJNDIName('jms.bpm.queue.tdrate.response')
cmo.setSubDeploymentName('BPMDeployment')

cd('/JMSSystemResources/CBTResources/JMSResource/CBTResources')
cmo=create('CBTErrorDistributedQueue','UniformDistributedQueue')

cd('/JMSSystemResources/CBTResources/JMSResource/CBTResources/UniformDistributedQueues/CBTErrorDistributedQueue')
cmo.setJNDIName('jms.queue.cbt.error')
cmo.setSubDeploymentName('CBTDeployment')

cd('/JMSSystemResources/CBTResources/JMSResource/CBTResources')
cmo=create('CBTNotifyDistributedQueue','UniformDistributedQueue')

cd('/JMSSystemResources/CBTResources/JMSResource/CBTResources/UniformDistributedQueues/CBTNotifyDistributedQueue')
cmo.setJNDIName('jms.queue.cbt.notify')
cmo.setSubDeploymentName('CBTDeployment')

cd('/JMSSystemResources/CBTSKLRelease/JMSResource/CBTSKLRelease')
cmo=create('CBTAccountInquiryDistributedQueue','UniformDistributedQueue')

cd('/JMSSystemResources/CBTSKLRelease/JMSResource/CBTSKLRelease/UniformDistributedQueues/CBTAccountInquiryDistributedQueue')
cmo.setJNDIName('jms.queue.cbt.account_inquiry')
cmo.setSubDeploymentName('CBTSKLReleaseSubDeployment')

cd('/JMSSystemResources/CBTSKLRelease/JMSResource/CBTSKLRelease')
cmo=create('CBTSKLInputDistributedQueue','UniformDistributedQueue')

cd('/JMSSystemResources/CBTSKLRelease/JMSResource/CBTSKLRelease/UniformDistributedQueues/CBTSKLInputDistributedQueue')
cmo.setJNDIName('jms.queue.cbt_skl.input')
cmo.setSubDeploymentName('CBTSKLReleaseSubDeployment')

cd('/JMSSystemResources/CBTSKLRelease/JMSResource/CBTSKLRelease')
cmo=create('CBTSKLReleaseDistributedQueue','UniformDistributedQueue')

cd('/JMSSystemResources/CBTSKLRelease/JMSResource/CBTSKLRelease/UniformDistributedQueues/CBTSKLReleaseDistributedQueue')
cmo.setJNDIName('jms.queue.cbt_skl.release')
cmo.setSubDeploymentName('CBTSKLReleaseSubDeployment')

cd('/JMSSystemResources/CBTSKLRelease/JMSResource/CBTSKLRelease')
cmo=create('CBTSKLReleaseErrorDistributedQueue','UniformDistributedQueue')

cd('/JMSSystemResources/CBTSKLRelease/JMSResource/CBTSKLRelease/UniformDistributedQueues/CBTSKLReleaseErrorDistributedQueue')
cmo.setJNDIName('jms.queue.cbt_skl.release_error')
cmo.setSubDeploymentName('CBTSKLReleaseSubDeployment')

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
cmo=create('SAFRetryBiller','UniformDistributedQueue')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/UniformDistributedQueues/SAFRetryBiller')
cmo.setJNDIName('jms.queue.saf.RetryBiller')
cmo.setSubDeploymentName('SAFDeployment')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources')
cmo=create('SAFRetryErrorQueue','UniformDistributedQueue')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/UniformDistributedQueues/SAFRetryErrorQueue')
cmo.setJNDIName('jms.queue.saf.ErrorRetryBiller')
cmo.setSubDeploymentName('SAFDeployment')

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule')
cmo=create('SiskohatReversal','UniformDistributedQueue')

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule/UniformDistributedQueues/SiskohatReversal')
cmo.setJNDIName('jms.queue.siskohat.Reversal')
cmo.setSubDeploymentName('Siskohat')

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule')
cmo=create('SiskohatReversalErrorQueue','UniformDistributedQueue')

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule/UniformDistributedQueues/SiskohatReversalErrorQueue')
cmo.setJNDIName('jms.queue.siskohat.ReversalErrorQueue')
cmo.setSubDeploymentName('Siskohat')

cd('/JMSSystemResources/TokenJmsModule/JMSResource/TokenJmsModule')
cmo=create('TokenJmsQueue','UniformDistributedQueue')

cd('/JMSSystemResources/TokenJmsModule/JMSResource/TokenJmsModule/UniformDistributedQueues/TokenJmsQueue')
cmo.setJNDIName('jms.token.queue')
cmo.setSubDeploymentName('TokenJmsSubDeployment')

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
