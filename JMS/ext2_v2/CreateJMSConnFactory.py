connect("weblogic", "welcome1", "t3://10.87.225.163:10401")
edit()
startEdit()

cd('/JMSSystemResources/ESBDBResources/JMSResource/ESBDBResources')
cmo.createConnectionFactory('ESBDBConnectionFactory_NonXA')

cd('/JMSSystemResources/ESBDBResources/JMSResource/ESBDBResources/ConnectionFactories/ESBDBConnectionFactory_NonXA')
cmo.setJNDIName('jms.esbdb.cfNonXA')

cd('/JMSSystemResources/ESBDBResources/JMSResource/ESBDBResources/ConnectionFactories/ESBDBConnectionFactory_NonXA/SecurityParams/ESBDBConnectionFactory_NonXA')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/ESBDBResources/JMSResource/ESBDBResources/ConnectionFactories/ESBDBConnectionFactory_NonXA/ClientParams/ESBDBConnectionFactory_NonXA')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/ESBDBResources/JMSResource/ESBDBResources/ConnectionFactories/ESBDBConnectionFactory_NonXA/TransactionParams/ESBDBConnectionFactory_NonXA')
cmo.setXAConnectionFactoryEnabled(false)

cd('/JMSSystemResources/ESBDBResources/JMSResource/ESBDBResources/ConnectionFactories/ESBDBConnectionFactory_NonXA')
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

cd('/JMSSystemResources/SMSResources/JMSResource/SMSResources')
cmo.createConnectionFactory('SMSConnectionFactory_NonXA')

cd('/JMSSystemResources/SMSResources/JMSResource/SMSResources/ConnectionFactories/SMSConnectionFactory_NonXA')
cmo.setJNDIName('jms.sms.cf')

cd('/JMSSystemResources/SMSResources/JMSResource/SMSResources/ConnectionFactories/SMSConnectionFactory_NonXA/SecurityParams/SMSConnectionFactory_NonXA')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/SMSResources/JMSResource/SMSResources/ConnectionFactories/SMSConnectionFactory_NonXA/ClientParams/SMSConnectionFactory_NonXA')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/SMSResources/JMSResource/SMSResources/ConnectionFactories/SMSConnectionFactory_NonXA/TransactionParams/SMSConnectionFactory_NonXA')
cmo.setXAConnectionFactoryEnabled(false)

cd('/JMSSystemResources/SMSResources/JMSResource/SMSResources/ConnectionFactories/SMSConnectionFactory_NonXA')
cmo.setSubDeploymentName('SMSDeployment')

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

