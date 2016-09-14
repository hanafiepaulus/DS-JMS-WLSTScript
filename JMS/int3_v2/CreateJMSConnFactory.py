connect("weblogic", "welcome1", "t3://10.87.225.160:10501")
edit()
startEdit()

cd('/JMSSystemResources/batchResources/JMSResource/batchResources')
cmo.createConnectionFactory('BatchConnectionFactory')

cd('/JMSSystemResources/batchResources/JMSResource/batchResources/ConnectionFactories/BatchConnectionFactory')
cmo.setJNDIName('jms.batch.cf')

cd('/JMSSystemResources/batchResources/JMSResource/batchResources/ConnectionFactories/BatchConnectionFactory/SecurityParams/BatchConnectionFactory')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/batchResources/JMSResource/batchResources/ConnectionFactories/BatchConnectionFactory/ClientParams/BatchConnectionFactory')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/batchResources/JMSResource/batchResources/ConnectionFactories/BatchConnectionFactory/TransactionParams/BatchConnectionFactory')
cmo.setXAConnectionFactoryEnabled(false)

cd('/JMSSystemResources/batchResources/JMSResource/batchResources/ConnectionFactories/BatchConnectionFactory')
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

