connect("weblogic", "welcome1", "t3://10.87.225.160:10101")
edit()
startEdit()

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule')
cmo.createConnectionFactory('BPMConnFactory_NonXA')

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule/ConnectionFactories/BPMConnFactory_NonXA')
cmo.setJNDIName('jms.bpm.cfNonXA')

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule/ConnectionFactories/BPMConnFactory_NonXA/SecurityParams/BPMConnFactory_NonXA')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule/ConnectionFactories/BPMConnFactory_NonXA/ClientParams/BPMConnFactory_NonXA')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule/ConnectionFactories/BPMConnFactory_NonXA/TransactionParams/BPMConnFactory_NonXA')
cmo.setXAConnectionFactoryEnabled(false)

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule/ConnectionFactories/BPMConnFactory_NonXA')
cmo.setDefaultTargetingEnabled(true)

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule')
cmo.createConnectionFactory('BPMConnFactory')

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule/ConnectionFactories/BPMConnFactory')
cmo.setJNDIName('jms.bpm.cfXA')

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule/ConnectionFactories/BPMConnFactory/SecurityParams/BPMConnFactory')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule/ConnectionFactories/BPMConnFactory/ClientParams/BPMConnFactory')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule/ConnectionFactories/BPMConnFactory/TransactionParams/BPMConnFactory')
cmo.setXAConnectionFactoryEnabled(true)

cd('/JMSSystemResources/BPMModule/JMSResource/BPMModule/ConnectionFactories/BPMConnFactory')
cmo.setDefaultTargetingEnabled(true)

cd('/JMSSystemResources/CBTResources/JMSResource/CBTResources')
cmo.createConnectionFactory('CBTConnectionFactory_NonXA')

cd('/JMSSystemResources/CBTResources/JMSResource/CBTResources/ConnectionFactories/CBTConnectionFactory_NonXA')
cmo.setJNDIName('jms.cbt.cfNonXA')

cd('/JMSSystemResources/CBTResources/JMSResource/CBTResources/ConnectionFactories/CBTConnectionFactory_NonXA/SecurityParams/CBTConnectionFactory_NonXA')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/CBTResources/JMSResource/CBTResources/ConnectionFactories/CBTConnectionFactory_NonXA/ClientParams/CBTConnectionFactory_NonXA')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/CBTResources/JMSResource/CBTResources/ConnectionFactories/CBTConnectionFactory_NonXA/TransactionParams/CBTConnectionFactory_NonXA')
cmo.setXAConnectionFactoryEnabled(false)

cd('/JMSSystemResources/CBTResources/JMSResource/CBTResources/ConnectionFactories/CBTConnectionFactory_NonXA')
cmo.setDefaultTargetingEnabled(true)

cd('/JMSSystemResources/CBTSKLRelease/JMSResource/CBTSKLRelease')
cmo.createConnectionFactory('CBTSKLReleaseConnFactory')

cd('/JMSSystemResources/CBTSKLRelease/JMSResource/CBTSKLRelease/ConnectionFactories/CBTSKLReleaseConnFactory')
cmo.setJNDIName('jms.cbt_skl_release.cfNonXA')

cd('/JMSSystemResources/CBTSKLRelease/JMSResource/CBTSKLRelease/ConnectionFactories/CBTSKLReleaseConnFactory/SecurityParams/CBTSKLReleaseConnFactory')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/CBTSKLRelease/JMSResource/CBTSKLRelease/ConnectionFactories/CBTSKLReleaseConnFactory/ClientParams/CBTSKLReleaseConnFactory')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/CBTSKLRelease/JMSResource/CBTSKLRelease/ConnectionFactories/CBTSKLReleaseConnFactory/TransactionParams/CBTSKLReleaseConnFactory')
cmo.setXAConnectionFactoryEnabled(false)

cd('/JMSSystemResources/CBTSKLRelease/JMSResource/CBTSKLRelease/ConnectionFactories/CBTSKLReleaseConnFactory')
cmo.setDefaultTargetingEnabled(true)

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources')
cmo.createConnectionFactory('SMS CF')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/ConnectionFactories/SMS CF')
cmo.setJNDIName('jms.sms.cf')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/ConnectionFactories/SMS CF/SecurityParams/SMS CF')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/ConnectionFactories/SMS CF/ClientParams/SMS CF')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/ConnectionFactories/SMS CF/TransactionParams/SMS CF')
cmo.setXAConnectionFactoryEnabled(false)

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/ConnectionFactories/SMS CF')
cmo.setDefaultTargetingEnabled(true)

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources')
cmo.createConnectionFactory('SAFConnectionFactory-XA')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/ConnectionFactories/SAFConnectionFactory-XA')
cmo.setJNDIName('jms.saf.cfXA')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/ConnectionFactories/SAFConnectionFactory-XA/SecurityParams/SAFConnectionFactory-XA')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/ConnectionFactories/SAFConnectionFactory-XA/ClientParams/SAFConnectionFactory-XA')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/ConnectionFactories/SAFConnectionFactory-XA/TransactionParams/SAFConnectionFactory-XA')
cmo.setXAConnectionFactoryEnabled(true)

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/ConnectionFactories/SAFConnectionFactory-XA')
cmo.setDefaultTargetingEnabled(true)

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources')
cmo.createConnectionFactory('SAFConnectionFactory-NonXA')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/ConnectionFactories/SAFConnectionFactory-NonXA')
cmo.setJNDIName('jms.saf.cfNonXA')

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/ConnectionFactories/SAFConnectionFactory-NonXA/SecurityParams/SAFConnectionFactory-NonXA')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/ConnectionFactories/SAFConnectionFactory-NonXA/ClientParams/SAFConnectionFactory-NonXA')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/ConnectionFactories/SAFConnectionFactory-NonXA/TransactionParams/SAFConnectionFactory-NonXA')
cmo.setXAConnectionFactoryEnabled(false)

cd('/JMSSystemResources/SAFResources/JMSResource/SAFResources/ConnectionFactories/SAFConnectionFactory-NonXA')
cmo.setDefaultTargetingEnabled(true)

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule')
cmo.createConnectionFactory('SiskohatConnectionFactory-NonXA')

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule/ConnectionFactories/SiskohatConnectionFactory-NonXA')
cmo.setJNDIName('jms.siskohat.cfNonXA')

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule/ConnectionFactories/SiskohatConnectionFactory-NonXA/SecurityParams/SiskohatConnectionFactory-NonXA')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule/ConnectionFactories/SiskohatConnectionFactory-NonXA/ClientParams/SiskohatConnectionFactory-NonXA')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule/ConnectionFactories/SiskohatConnectionFactory-NonXA/TransactionParams/SiskohatConnectionFactory-NonXA')
cmo.setXAConnectionFactoryEnabled(false)

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule/ConnectionFactories/SiskohatConnectionFactory-NonXA')
cmo.setDefaultTargetingEnabled(true)

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule')
cmo.createConnectionFactory('SiskohatConnectionFactory-XA')

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule/ConnectionFactories/SiskohatConnectionFactory-XA')
cmo.setJNDIName('jms.siskohat.cfXA')

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule/ConnectionFactories/SiskohatConnectionFactory-XA/SecurityParams/SiskohatConnectionFactory-XA')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule/ConnectionFactories/SiskohatConnectionFactory-XA/ClientParams/SiskohatConnectionFactory-XA')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule/ConnectionFactories/SiskohatConnectionFactory-XA/TransactionParams/SiskohatConnectionFactory-XA')
cmo.setXAConnectionFactoryEnabled(true)

cd('/JMSSystemResources/SiskohatModule/JMSResource/SiskohatModule/ConnectionFactories/SiskohatConnectionFactory-XA')
cmo.setDefaultTargetingEnabled(true)

cd('/JMSSystemResources/TokenJmsModule/JMSResource/TokenJmsModule')
cmo.createConnectionFactory('TokenJmsCF')

cd('/JMSSystemResources/TokenJmsModule/JMSResource/TokenJmsModule/ConnectionFactories/TokenJmsCF')
cmo.setJNDIName('jms.token.cf')

cd('/JMSSystemResources/TokenJmsModule/JMSResource/TokenJmsModule/ConnectionFactories/TokenJmsCF/SecurityParams/TokenJmsCF')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/TokenJmsModule/JMSResource/TokenJmsModule/ConnectionFactories/TokenJmsCF/ClientParams/TokenJmsCF')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/TokenJmsModule/JMSResource/TokenJmsModule/ConnectionFactories/TokenJmsCF/TransactionParams/TokenJmsCF')
cmo.setXAConnectionFactoryEnabled(false)

cd('/JMSSystemResources/TokenJmsModule/JMSResource/TokenJmsModule/ConnectionFactories/TokenJmsCF')
cmo.setDefaultTargetingEnabled(true)

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules')
cmo.createConnectionFactory('WNAConnFactory')

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules/ConnectionFactories/WNAConnFactory')
cmo.setJNDIName('jms.wna.cf')

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules/ConnectionFactories/WNAConnFactory/SecurityParams/WNAConnFactory')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules/ConnectionFactories/WNAConnFactory/ClientParams/WNAConnFactory')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules/ConnectionFactories/WNAConnFactory/TransactionParams/WNAConnFactory')
cmo.setXAConnectionFactoryEnabled(false)

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules/ConnectionFactories/WNAConnFactory')
cmo.setDefaultTargetingEnabled(true)

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules')
cmo.createConnectionFactory('WNAConnFactory_XA')

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules/ConnectionFactories/WNAConnFactory_XA')
cmo.setJNDIName('jms.wna.cfXA')

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules/ConnectionFactories/WNAConnFactory_XA/SecurityParams/WNAConnFactory_XA')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules/ConnectionFactories/WNAConnFactory_XA/ClientParams/WNAConnFactory_XA')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules/ConnectionFactories/WNAConnFactory_XA/TransactionParams/WNAConnFactory_XA')
cmo.setXAConnectionFactoryEnabled(true)

cd('/JMSSystemResources/WNAModules/JMSResource/WNAModules/ConnectionFactories/WNAConnFactory_XA')
cmo.setDefaultTargetingEnabled(true)

save()
activate()

